import re
import weakref
from pathlib import Path
from typing import TYPE_CHECKING, Iterable, List, Set, Tuple, TypeVar, Union

import numpy as np
from magicclass import (
    MagicTemplate,
    bind_key,
    do_not_record,
    field,
    magicclass,
    magicmenu,
    magictoolbar,
    nogui,
    set_design,
    set_options,
    vfield,
)
from magicclass.types import Bound, OneOf, SomeOf
from magicclass.widgets import Figure, Separator
from napari.layers import Image, Shapes

from . import _optimizer as _opt
from ._spline import Measurement, Spline
from ._table_stack import TableStack
from ._types import weight

if TYPE_CHECKING:
    from magicclass.fields import MagicValueField
    from magicgui.widgets import ComboBox

ICON_DIR = Path(__file__).parent / "_icon"
ICON_KWARGS = dict(text="", min_width=42, min_height=42)

# global metadata keys
TARGET_IMG_LAYERS = "target-image-layer"

ROI_ID = "ROI-ID"
SOURCE = "source"
IMAGE_AXES = "axes"

ROI_FMT = "[{" + ROI_ID + "}]"


@magicclass
class FilamentAnalyzer(MagicTemplate):
    """
    Filament Analyzer widget.

    Attributes
    ----------
    target_filament : Shapes
        The target Shapes layer.
    target_image : Image
        The target Image layer. Fitting/analysis will be performed on this
        layer.
    """

    def _get_available_filament_id(self, w=None) -> List[int]:
        if self.target_filaments is None:
            return []
        return list(range(self.target_filaments.nshapes))

    _tablestack = field(TableStack, name="Filament Analyzer Tables")
    target_filaments: "MagicValueField[ComboBox, Shapes]" = vfield(Shapes)
    target_image: "MagicValueField[ComboBox, Image]" = vfield(Image)
    filament = vfield(OneOf[_get_available_filament_id])

    # fmt: off
    @magictoolbar
    class Tools(MagicTemplate):
        @magicmenu
        class Layers(MagicTemplate):
            def open_image(self): ...
            def open_filaments(self): ...
            def add_filaments(self): ...

            @magicmenu
            class Import(MagicTemplate):
                def from_roi(self): ...
            sep0 = field(Separator)
            def save_filaments(self): ...
            sep1 = field(Separator)
            def create_total_intensity(self): ...
            # def export_roi(self): ...

        @magicmenu
        class Parameters(MagicTemplate):
            """
            Global parameters of Filament Analyzer.

            Attributes
            ----------
            lattice_width : int
                The width of the image lattice along a filament.
            dx : float
                Delta x of filament clipping and extension.
            sigma_range : (float, float)
                The range of sigma to be used for fitting.

            """
            lattice_width = vfield(17, options={"min": 5, "max": 49}, record=False)  # noqa
            dx = vfield(5.0, options={"min": 1, "max": 50.0}, record=False)
            sigma_range = vfield((0.5, 5.0), record=False)
            target_image_filter = vfield(True, record=False)

        @magicmenu
        class Others(MagicTemplate):
            def create_macro(self): ...
            def send_widget_to_viewer(self): ...

    @magicclass(widget_type="tabbed")
    class Tabs(MagicTemplate):
        @magicclass(layout="horizontal")
        class Spline(MagicTemplate):
            def __post_init__(self):
                self.margins = (2, 2, 2, 2)

            @magicclass(widget_type="groupbox")
            class Left(MagicTemplate):
                def extend_left(self): ...
                def extend_and_fit_left(self): ...
                def clip_left(self): ...
                def clip_left_at_inflection(self): ...

            @magicclass(widget_type="frame")
            class Both(MagicTemplate):
                def fit_filament(self): ...
                def delete_current(self): ...
                def undo_spline(self): ...
                def clip_at_inflections(self): ...

            @magicclass(widget_type="groupbox")
            class Right(MagicTemplate):
                def extend_right(self): ...
                def extend_and_fit_right(self): ...
                def clip_right(self): ...
                def clip_right_at_inflection(self): ...

        @magicclass(widget_type="scrollable")
        class Measure(MagicTemplate):
            def measure_properties(self): ...
            def plot_profile(self): ...
            def plot_curvature(self): ...
            def kymograph(self): ...

    # fmt: on

    @magicclass
    class Output(MagicTemplate):
        plt = field(Figure)

        def __post_init__(self):
            self._xdata = []
            self._ydata = []
            self.min_height = 200

        @do_not_record
        def view_data(self):
            """View plot data in a table."""
            xlabel = self.plt.ax.get_xlabel() or "x"
            ylabel = self.plt.ax.get_ylabel() or "y"
            if isinstance(self._ydata, list):
                data = {xlabel: self._xdata}
                for i, y in enumerate(self._ydata):
                    data[f"{ylabel}-{i}"] = y
            else:
                data = {xlabel: self._xdata, ylabel: self._ydata}
            tstack = self.find_ancestor(FilamentAnalyzer)._tablestack
            tstack.add_table(data, name="Plot data")
            tstack.show()

        def _plot(self, x, y, clear=True, **kwargs):
            if clear:
                self.plt.cla()
            self.plt.plot(x, y, **kwargs)
            self._xdata = x
            if clear:
                self._ydata = y
            else:
                if isinstance(self._ydata, list):
                    self._ydata.append(y)
                else:
                    self._ydata = [self._ydata, y]

        def _set_labels(self, x: str, y: str):
            self.plt.xlabel(x)
            self.plt.ylabel(y)

    def __init__(self):
        self._last_target_filaments = None
        self._color_default = np.array([0.973, 1.000, 0.412, 1.000])
        self._last_data: Tuple[int, np.ndarray] = None
        self._dims_slider_changing = False
        self._nfilaments = 0

    def _get_idx(self, w=None) -> Union[int, Set[int]]:
        if self.target_filaments is None:
            return 0
        sel = self.target_filaments.selected_data
        if len(sel) == 0:
            return self.target_filaments.nshapes - 1
        return sel

    @property
    def last_target_filaments(self) -> Union[Shapes, None]:
        if self._last_target_filaments is None:
            return None
        return self._last_target_filaments()

    @last_target_filaments.setter
    def last_target_filaments(self, val: Union[Shapes, None]):
        if val is None:
            self._last_target_filaments = None
            return

        if not isinstance(val, Shapes):
            raise TypeError(
                f"Cannot set type {type(val)} to `last_target_filaments`."
            )
        self._last_target_filaments = weakref.ref(val)

    @target_filaments.connect
    def _on_change(self):
        # old parameters
        _sl = self.parent_viewer.dims.current_step[:-2]
        _fil = self.filament
        if self.last_target_filaments is not None:
            _mode = self.last_target_filaments.mode
            _toggle_target_images(self.last_target_filaments, False)
        else:
            _mode = "pan_zoom"

        self._last_data = None
        _toggle_target_images(self.target_filaments, True)
        self.last_target_filaments = self.target_filaments
        self.parent_viewer.layers.selection = {self.target_filaments}

        self._filter_image_choices()
        cbox: ComboBox = self["filament"]
        cbox.reset_choices()

        # restore old parameters
        self.target_filaments.mode = _mode
        if _fil in cbox.choices:
            cbox.value = _fil
        self.parent_viewer.dims.set_current_step(np.arange(len(_sl)), _sl)

    @filament.connect
    def _on_filament_change(self, idx: int):
        data = self.target_filaments.data[idx]
        _sl, _ = _split_slice_and_path(data)
        self._dims_slider_changing = True
        self.parent_viewer.dims.set_current_step(np.arange(len(_sl)), _sl)
        self._dims_slider_changing = False
        self.target_filaments.selected_data = {idx}

        props = self.target_filaments.current_properties
        next_id = self.target_filaments.nshapes
        props[ROI_ID] = next_id
        self.target_filaments.current_properties = props

    def _filter_image_choices(self):
        if not self.Tools.Parameters.target_image_filter:
            return
        target_image_widget: ComboBox = self["target_image"]
        if target_image_widget.value is None:
            return
        cbox_idx = target_image_widget.choices.index(target_image_widget.value)
        img_layers = _get_connected_target_image_layers(self.target_filaments)
        if len(img_layers) > 0:
            target_image_widget.choices = img_layers
            cbox_idx = min(cbox_idx, len(img_layers) - 1)
            target_image_widget.value = target_image_widget.choices[cbox_idx]

    @Tools.Layers.wraps
    def open_image(self, path: Path):
        """Open a TIF."""
        path = Path(path)
        from tifffile import TiffFile

        with TiffFile(path) as tif:
            series0 = tif.series[0]
            axes = getattr(series0, "axes", "")
            img: np.ndarray = tif.asarray()
        self._add_image(img, axes, path)

    def _add_image(self, img: np.ndarray, axes: str, path: Path):
        if "C" in axes:
            ic = axes.find("C")
            nchn = img.shape[ic]
            axis_labels: Tuple[str] = tuple(c for c in axes if c != "C")
            img_layers: List[Image] = self.parent_viewer.add_image(
                img,
                channel_axis=ic,
                name=[f"[C{i}] {path.stem}" for i in range(nchn)],
                metadata={IMAGE_AXES: axis_labels, SOURCE: path},
            )
        else:
            axis_labels = tuple(axes)
            _layer = self.parent_viewer.add_image(
                img,
                name=path.stem,
                metadata={IMAGE_AXES: axis_labels, SOURCE: path},
            )
            img_layers = [_layer]

        self._add_filament_layer(img_layers, path.stem)
        ndim = self.parent_viewer.dims.ndim
        if ndim == len(axis_labels):
            self.parent_viewer.dims.set_axis_label(
                list(range(ndim)), axis_labels
            )

    @Tools.Layers.wraps
    @set_options(path={"mode": "d"})
    def open_filaments(self, path: Path):
        """Open a directory with csv files as a filament layer."""
        import pandas as pd

        path = Path(path)

        all_csv: List[np.ndarray] = []
        for p in path.glob("*.csv"):
            df = pd.read_csv(p)
            all_csv.append(df.values)
        self._load_filament_coordinates(all_csv, f"[F] {path.stem}")

    def _load_filament_coordinates(self, data: List[np.ndarray], name: str):
        ndata = len(data)
        layer_paths = self.parent_viewer.add_shapes(
            data,
            edge_color=self._color_default,
            name=name,
            shape_type="path",
            edge_width=0.5,
            properties={ROI_ID: np.arange(ndata, dtype=np.uint32)},
            text=dict(string=ROI_FMT, color="white", size=8),
        )

        self._set_filament_layer(layer_paths)
        layer_paths.current_properties = {ROI_ID: ndata}
        self.target_filaments.metadata[TARGET_IMG_LAYERS] = list(
            filter(lambda x: isinstance(x, Image), self.parent_viewer.layers)
        )

    @Tools.Layers.wraps
    def add_filaments(self):
        images = self.target_filaments.metadata[TARGET_IMG_LAYERS]
        name = self.target_filaments.name.lstrip("[F] ")
        return self._add_filament_layer(images, name)

    def _add_filament_layer(self, images: List[Image], name: str):
        """Add a Shapes layer for the target image."""
        # check input images
        ndim: int = _get_unique_value(img.ndim for img in images)
        axes: Tuple[str] = _get_unique_value(
            img.metadata[IMAGE_AXES] for img in images
        )
        layer = self.parent_viewer.add_shapes(
            ndim=ndim,
            edge_color=self._color_default,
            name=f"[F] {name}",
            metadata={IMAGE_AXES: axes, TARGET_IMG_LAYERS: images},
            edge_width=0.5,
            properties={ROI_ID: 0},
            text=dict(string=ROI_FMT, color="white", size=8),
        )

        return self._set_filament_layer(layer)

    def _set_filament_layer(self, new_filaments_layer: Shapes):
        @new_filaments_layer.events.set_data.connect
        def _on_data_changed(e):
            if (
                self.target_filaments is not new_filaments_layer
                or self.target_filaments._is_moving
                or self._dims_slider_changing
            ):
                return
            # delete undo history
            self._last_data = None

            # update current filament ROI ID
            next_id = self.target_filaments.nshapes
            if self._nfilaments >= next_id:
                features = self.target_filaments.features
                features[ROI_ID] = np.arange(next_id)
                self.target_filaments.features = features
            props = self.target_filaments.current_properties
            props[ROI_ID] = next_id
            self.target_filaments.current_properties = props
            self["filament"].reset_choices()
            next_id = self.target_filaments.nshapes
            try:
                self.filament = next_id - 1
            except Exception:
                pass

            self._nfilaments = next_id

        new_filaments_layer.current_properties = {ROI_ID: 0}
        self.target_filaments = new_filaments_layer
        if self.last_target_filaments is None:
            self.last_target_filaments = new_filaments_layer

        new_filaments_layer.mode = "add_path"

        return new_filaments_layer

    @Tools.Layers.Import.wraps
    @set_design(text="From ImageJ ROI")
    def from_roi(self, path: Path):
        """Import ImageJ Roi zip file as filaments."""
        from roifile import ROI_TYPE, roiread

        path = Path(path)
        rois = roiread(path)
        if not isinstance(rois, list):
            rois = [rois]

        shapes = self.target_filaments
        axes = shapes.metadata[IMAGE_AXES]

        for roi in rois:
            if roi.roitype not in (ROI_TYPE.LINE, ROI_TYPE.POLYLINE):
                raise ValueError(f"ROI type {roi.roitype.name} not supported")
            # load coordinates
            yx: np.ndarray = roi.coordinates()[:, ::-1]
            p = roi.position
            t = roi.t_position if "T" in axes else -1
            z = roi.z_position if "Z" in axes else -1

            d = np.array([x - 1 for x in [p, t, z] if x > 0])
            stacked = np.stack([d] * yx.shape[0], axis=0)
            multi_coords = np.concatenate([stacked, yx], axis=1)
            self.target_filaments.add_paths(multi_coords)

    @Tools.Layers.wraps
    @set_options(path={"mode": "w"})
    def save_filaments(self, layer: Shapes, path: Path):
        """Save a Shapes layer as a directory of CSV files."""
        import datetime
        import json

        import magicclass as mcls
        import napari
        import pandas as pd

        from . import __version__

        path = Path(path)
        path.mkdir(exist_ok=True)
        labels = self.parent_viewer.dims.axis_labels
        roi_id = layer.features[ROI_ID]

        # save filaments
        for idx in range(layer.nshapes):
            data: np.ndarray = layer.data[idx]
            ndim = data.shape[1]
            df = pd.DataFrame(data, columns=list(labels[-ndim:]))
            df.to_csv(
                path / f"Filament-{roi_id[idx]}.csv",
                index=False,
                float_format="%.3f",
            )

        # save other info
        info = {
            "versions": {
                "napari-filaments": __version__,
                "napari": napari.__version__,
                "magicclass": mcls.__version__,
            },
            "date": datetime.datetime.now().isoformat(sep=" "),
            "images": _get_image_sources(layer),
        }
        with open(path / "info.json", "w") as f:
            json.dump(info, f, indent=2)
        return None

    def _update_paths(
        self, idx: int, spl: Spline, current_slice: Tuple[int, ...] = ()
    ):
        if idx < 0:
            idx += self.target_filaments.nshapes
        if spl.length() > 1000:
            raise ValueError("Spline is too long.")
        sampled = spl.sample(interval=1.0)
        if current_slice:
            sl = np.stack([np.array(current_slice)] * sampled.shape[0], axis=0)
            sampled = np.concatenate([sl, sampled], axis=1)

        hist = self.target_filaments.data[idx]
        self._replace_data(idx, sampled)
        self._last_data = (idx, hist)

    def _fit_i_2d(self, width, img, coords) -> Spline:
        spl = Spline.fit(coords, degree=1, err=0.0)
        length = spl.length()
        interv = min(8.0, length / 4)
        rough = spl.fit_filament(
            img, width=width, interval=interv, spline_error=0.0
        )
        return rough.fit_filament(img, width=7, spline_error=3e-2)

    @Tabs.Spline.Both.wraps
    @set_design(**ICON_KWARGS, icon=ICON_DIR / "fit.png")
    @bind_key("F1")
    def fit_filament(
        self,
        image: Bound[target_image],
        idx: Bound[_get_idx] = -1,
        width: Bound[Tools.Parameters.lattice_width] = 9,
    ):
        """Fit current spline to the image."""
        if not isinstance(image, Image):
            raise TypeError("'image' must be a Image layer.")
        self.target_filaments._finish_drawing()
        indices = _arrange_selection(idx)
        for i in indices:
            data: np.ndarray = self.target_filaments.data[i]
            current_slice, data = _split_slice_and_path(data)
            fit = self._fit_i_2d(width, image.data[current_slice], data)
            self._update_paths(i, fit, current_slice)

    def _get_slice_and_spline(
        self, idx: int
    ) -> Tuple[Tuple[int, ...], Spline]:
        data: np.ndarray = self.target_filaments.data[idx]
        current_slice, data = _split_slice_and_path(data)
        if data.shape[0] < 4:
            data = Spline.fit(data, degree=1, err=0).sample(interval=1.0)
        spl = Spline.fit(data, err=0.0)
        return current_slice, spl

    @Tabs.Spline.Both.wraps
    @set_design(**ICON_KWARGS, icon=ICON_DIR / "undo.png")
    def undo_spline(self):
        """Undo the last spline fit."""
        if self._last_data is None:
            return
        self._replace_data(*self._last_data)

    def _replace_data(self, idx: int, new_data: np.ndarray):
        """Replace the idx-th data to the new one."""
        data = self.target_filaments.data
        data[idx] = new_data
        self.target_filaments.data = data
        self._last_data = None
        self.filament = idx

    @Tabs.Spline.Left.wraps
    @set_design(**ICON_KWARGS, icon=ICON_DIR / "ext_l.png")
    def extend_left(
        self, idx: Bound[_get_idx] = -1, dx: Bound[Tools.Parameters.dx] = 5.0
    ):
        """Extend spline at the starting edge."""
        idx = _assert_single_selection(idx)
        current_slice, spl = self._get_slice_and_spline(idx)
        out = spl.extend_left(dx)
        self._update_paths(idx, out, current_slice)

    @Tabs.Spline.Right.wraps
    @set_design(**ICON_KWARGS, icon=ICON_DIR / "ext_r.png")
    def extend_right(
        self, idx: Bound[_get_idx] = -1, dx: Bound[Tools.Parameters.dx] = 5.0
    ):
        """Extend spline at the ending edge."""
        idx = _assert_single_selection(idx)
        current_slice, spl = self._get_slice_and_spline(idx)
        out = spl.extend_right(dx)
        self._update_paths(idx, out, current_slice)

    @Tabs.Spline.Left.wraps
    @set_design(**ICON_KWARGS, icon=ICON_DIR / "extfit_l.png")
    def extend_and_fit_left(
        self,
        image: Bound[target_image],
        idx: Bound[_get_idx] = -1,
        dx: Bound[Tools.Parameters.dx] = 5.0,
    ):
        """Extend spline and fit to the filament at the starting edge."""
        idx = _assert_single_selection(idx)
        current_slice, spl = self._get_slice_and_spline(idx)
        fit = spl.extend_filament_left(
            image.data[current_slice], dx, width=11, spline_error=3e-2
        )
        self._update_paths(idx, fit, current_slice)

    @Tabs.Spline.Right.wraps
    @set_design(**ICON_KWARGS, icon=ICON_DIR / "extfit_r.png")
    def extend_and_fit_right(
        self,
        image: Bound[target_image],
        idx: Bound[_get_idx] = -1,
        dx: Bound[Tools.Parameters.dx] = 5.0,
    ):
        """Extend spline and fit to the filament at the ending edge."""
        idx = _assert_single_selection(idx)
        current_slice, spl = self._get_slice_and_spline(idx)
        fit = spl.extend_filament_right(
            image.data[current_slice], dx, width=11, spline_error=3e-2
        )
        self._update_paths(idx, fit, current_slice)

    @Tabs.Spline.Left.wraps
    @set_design(**ICON_KWARGS, icon=ICON_DIR / "clip_l.png")
    def clip_left(
        self, idx: Bound[_get_idx] = -1, dx: Bound[Tools.Parameters.dx] = 5.0
    ):
        """Clip spline at the starting edge."""
        idx = _assert_single_selection(idx)
        current_slice, spl = self._get_slice_and_spline(idx)
        start = dx / spl.length()
        fit = spl.clip(start, 1.0)
        self._update_paths(idx, fit, current_slice)

    @Tabs.Spline.Right.wraps
    @set_design(**ICON_KWARGS, icon=ICON_DIR / "clip_r.png")
    def clip_right(
        self, idx: Bound[_get_idx] = -1, dx: Bound[Tools.Parameters.dx] = 5.0
    ):
        """Clip spline at the ending edge."""
        idx = _assert_single_selection(idx)
        current_slice, spl = self._get_slice_and_spline(idx)
        stop = 1.0 - dx / spl.length()
        fit = spl.clip(0.0, stop)
        self._update_paths(idx, fit, current_slice)

    @Tabs.Spline.Left.wraps
    @set_design(**ICON_KWARGS, icon=ICON_DIR / "erf_l.png")
    def clip_left_at_inflection(
        self,
        image: Bound[target_image],
        idx: Bound[_get_idx] = -1,
    ):
        """Clip spline at the inflection point at starting edge."""
        idx = _assert_single_selection(idx)
        current_slice, spl = self._get_slice_and_spline(idx)
        fit = spl.clip_at_inflection_left(
            image.data[current_slice],
            callback=self._show_fitting_result,
        )
        self._update_paths(idx, fit, current_slice)

    @Tabs.Spline.Right.wraps
    @set_design(**ICON_KWARGS, icon=ICON_DIR / "erf_r.png")
    def clip_right_at_inflection(
        self,
        image: Bound[target_image],
        idx: Bound[_get_idx] = -1,
    ):
        """Clip spline at the inflection point at ending edge."""
        idx = _assert_single_selection(idx)
        current_slice, spl = self._get_slice_and_spline(idx)
        fit = spl.clip_at_inflection_right(
            image.data[current_slice],
            callback=self._show_fitting_result,
        )
        self._update_paths(idx, fit, current_slice)

    @Tabs.Spline.Both.wraps
    @set_design(**ICON_KWARGS, icon=ICON_DIR / "erf2.png")
    @bind_key("F2")
    def clip_at_inflections(
        self,
        image: Bound[target_image],
        idx: Bound[_get_idx] = -1,
    ):
        """Clip spline at the inflection points at both ends."""
        indices = _arrange_selection(idx)
        for i in indices:
            current_slice, spl = self._get_slice_and_spline(i)
            out = spl.clip_at_inflections(
                image.data[current_slice],
                callback=self._show_fitting_result,
            )
            self._update_paths(i, out, current_slice)

    def _show_fitting_result(self, opt: _opt.Optimizer, prof: np.ndarray):
        """Callback function for error function fitting"""
        sg_min, sg_max = self.Tools.Parameters.sigma_range
        if isinstance(opt, (_opt.GaussianOptimizer, _opt.ErfOptimizer)):
            valid = sg_min <= opt.params.sg <= sg_max
        elif isinstance(opt, _opt.TwosideErfOptimizer):
            valid0 = sg_min <= opt.params.sg0 <= sg_max
            valid1 = sg_min <= opt.params.sg1 <= sg_max
            valid = valid0 and valid1
        else:
            raise NotImplementedError
        ndata = prof.size
        xdata = np.arange(ndata)
        ydata = opt.sample(xdata)
        self.Output._plot(xdata, prof, color="gray", alpha=0.7, lw=1)
        self.Output._plot(xdata, ydata, clear=False, color="red", lw=2)
        if not valid:
            self.Output.plt.text(
                0, np.min(ydata), "Sigma out of range.", color="crimson"
            )
        self.Output._set_labels("Data points", "Intensity")

    @Tabs.Measure.wraps
    def measure_properties(
        self,
        image: Bound[target_image],
        properties: SomeOf[Measurement.PROPERTIES] = ("length", "mean"),
        slices: bool = False,
    ):
        """Measure properties of all the splines."""
        import pandas as pd

        if slices:
            # Record slice numbers in columns such as "index_T"
            ndim = len(image.data.shape)
            labels = self.parent_viewer.dims.axis_labels[-ndim:-2]
            sl_data = {f"index_{lname}": [] for lname in labels}
        else:
            sl_data = {}
        data = {p: [] for p in properties}

        image_data = image.data
        for idx in range(self.target_filaments.nshapes):
            sl, spl = self._get_slice_and_spline(idx)
            measure = Measurement(spl, image_data[sl])
            for v, s0 in zip(sl_data.values(), sl):
                v.append(s0)
            for k, v in data.items():
                v.append(getattr(measure, k)())

        sl_data.update(data)
        tstack = self._tablestack
        tstack.add_table(sl_data, name=self.target_filaments.name)
        tstack.show()
        return pd.DataFrame(sl_data)

    @Tabs.Measure.wraps
    def plot_curvature(
        self,
        idx: Bound[_get_idx] = -1,
    ):
        """Plot curvature of filament."""
        _, spl = self._get_slice_and_spline(idx)
        length = spl.length()
        x = np.linspace(0, 1, int(spl.length()))
        cv = spl.curvature(x)
        self.Output._plot(x * length, cv)
        self.Output._set_labels("Position (px)", "Curvature")

    @Tabs.Measure.wraps
    def plot_profile(
        self,
        image: Bound[target_image],
        idx: Bound[_get_idx] = -1,
    ):
        """Plot intensity profile."""
        current_slice, spl = self._get_slice_and_spline(idx)
        prof = spl.get_profile(image.data[current_slice])
        length = spl.length()
        x = np.linspace(0, 1, int(length)) * length
        self.Output._plot(x, prof)
        self.Output._set_labels("Position (px)", "Intensity")

    def _get_axes(self, w=None):
        return self.parent_viewer.dims.axis_labels[:-2]

    @Tabs.Measure.wraps
    def kymograph(
        self,
        image: Bound[target_image],
        time_axis: OneOf[_get_axes],
        idx: Bound[_get_idx] = -1,
    ):
        """Plot kymograph."""
        current_slice, spl = self._get_slice_and_spline(idx)
        if isinstance(time_axis, str):
            t0 = image.metadata[IMAGE_AXES].index(time_axis)
        else:
            t0 = time_axis
        ntime = image.data.shape[t0]
        profiles: List[np.ndarray] = []
        for t in range(ntime):
            t1 = t0 + 1
            sl = current_slice[:t0] + (t,) + current_slice[t1:]
            prof = spl.get_profile(image.data[sl])
            profiles.append(prof)
        kymo = np.stack(profiles, axis=0)
        plt = Figure()
        plt.imshow(kymo, cmap="gray")
        plt.show()

    @Tools.Layers.wraps
    @set_options(wlayers={"layout": "vertical", "label": "weight x layer"})
    def create_total_intensity(self, wlayers: List[Tuple[weight, Image]]):
        """Create a total intensity layer from multiple images."""
        weights = [t[0] for t in wlayers]
        imgs = [t[1].data for t in wlayers]
        names = [t[1].name for t in wlayers]
        tot = sum(w * img for w, img in zip(weights, imgs))

        outs = set()
        for name in names:
            matched = re.findall(r"\[.*\] (.+)", name)
            if matched:
                outs.add(matched[0])
        if len(outs) == 1:
            new_name = f"[Total] {outs.pop()}"
        else:
            new_name = f"[Total] {outs.pop()} etc."

        tot_layer = self.parent_viewer.add_image(
            tot, name=new_name, visible=False
        )

        # update target images
        for layer in self.parent_viewer.layers:
            if not isinstance(layer, Shapes):
                continue
            # if all the input images belongs to the same shapes layer, update
            # the target image list.
            img_layers = _get_connected_target_image_layers(layer)
            target_names = [target.name for target in img_layers]
            if all(img_name in target_names for img_name in names):
                img_layers.append(tot_layer)

    # TODO: how to save at subpixel resolution?
    # @Tools.Layers.wraps
    # @set_options(path={"mode": "w", "filter": ".zip"})
    # def export_roi(self, layer: Shapes, path: Path):
    #     """Export filament layer as a ImageJ ROI.zip file."""
    #
    #     from roifile import roiwrite, ImagejRoi, ROI_TYPE, ROI_OPTIONS
    #     roilist: List[ImagejRoi] = []
    #     multi_labels = self.parent_viewer.dims.axis_labels[:-2]
    #     roi_id = layer.features[ROI_ID]
    #     for i, data in enumerate(layer.data):
    #         multi, coords = _split_slice_and_path(data)
    #         n = len(multi)
    #         dim_kwargs = {
    #             f"{l.lower()}_position": p + 1
    #             for l, p in zip(multi_labels[-n:], multi)
    #         }
    #         h, w = np.max(coords, axis=0)
    #         edge_kwargs = dict(
    #             left=0,
    #             top=0,
    #             right=int(w) + 2,
    #             bottom=int(h) + 2,
    #             n_coordinates=coords.shape[0],
    #         )
    #         roi = ImagejRoi(
    #             roitype=ROI_TYPE.POLYLINE,
    #             options=ROI_OPTIONS.SUB_PIXEL_RESOLUTION,
    #             # integer_coordinates=coords[:, ::-1].astype(np.uint16) + 1,
    #             subpixel_coordinates=coords[:, ::-1] + 1,
    #             name=f"Filament-{roi_id[i]}",
    #             **dim_kwargs,
    #             **edge_kwargs,
    #         )
    #         roilist.append(roi)
    #     roiwrite(path, roilist)

    @Tabs.Spline.Both.wraps
    @set_design(**ICON_KWARGS, icon=ICON_DIR / "del.png")
    def delete_current(self, idx: Bound[_get_idx]):
        """Delete selected (or the last) path."""
        if isinstance(idx, int):
            idx = {idx}
        self.target_filaments.selected_data = idx
        self.target_filaments.remove_selected()
        if len(idx) == 1 and self.target_filaments.nshapes > 0:
            self.filament = min(
                list(idx)[0], len(self.target_filaments.data) - 1
            )
            self.target_filaments.selected_data = {self.filament}

    @Tools.Others.wraps
    @do_not_record
    def create_macro(self):
        """Create an executable Python script."""
        import macrokit as mk

        new = self.macro.widget.duplicate()
        v = mk.Expr("getattr", [mk.symbol(self), "parent_viewer"])
        new.value = self.macro.format([(mk.symbol(self.parent_viewer), v)])
        new.show()
        return None

    @Tools.Others.wraps
    @do_not_record
    def send_widget_to_viewer(self):
        self.parent_viewer.update_console({"ui": self})

    @nogui
    @do_not_record
    def get_spline(self, idx: int) -> Spline:
        _, spl = self._get_slice_and_spline(idx)
        return spl


def _split_slice_and_path(
    data: np.ndarray,
) -> Tuple[Tuple[int, ...], np.ndarray]:
    if data.shape[1] == 2:
        return (), data
    sl: np.ndarray = np.unique(data[:, :-2], axis=0)
    if sl.shape[0] != 1:
        raise ValueError("Spline is not in 2D")
    return tuple(sl.ravel().astype(np.int64)), data[:, -2:]


def _get_connected_target_image_layers(shapes: Shapes) -> List[Image]:
    """Return all connected target image layers."""
    return shapes.metadata.get(TARGET_IMG_LAYERS, [])


def _toggle_target_images(shapes: Shapes, visible: bool):
    """Set target images to visible or invisible."""
    img_layers = _get_connected_target_image_layers(shapes)
    for img_layer in img_layers:
        if img_layer.name.startswith("[Total]"):
            continue
        img_layer.visible = visible
    shapes.visible = visible


def _assert_single_selection(idx: Union[int, Set[int]]) -> int:
    if isinstance(idx, set):
        if len(idx) != 1:
            raise ValueError("Multiple selection")
        return idx.pop()
    return idx


def _arrange_selection(idx: Union[int, Set[int]]) -> List[int]:
    if isinstance(idx, int):
        return [idx]
    else:
        return sorted(list(idx), reverse=True)


def _get_image_sources(shapes: Shapes) -> Union[List[str], None]:
    """Extract image sources from a shapes layer."""
    img_layers = _get_connected_target_image_layers(shapes)
    if not img_layers:
        return None
    sources = []
    for img in img_layers:
        source = img.metadata.get(SOURCE) or img.source.path
        if source is not None:
            sources.append(str(source))
    if not sources:
        return None
    return sources


_V = TypeVar("_V")


def _get_unique_value(vals: Iterable[_V]) -> _V:
    s = set(vals)
    if len(s) != 1:
        raise ValueError(f"Not a unique value: {s}")
    return next(iter(s))
