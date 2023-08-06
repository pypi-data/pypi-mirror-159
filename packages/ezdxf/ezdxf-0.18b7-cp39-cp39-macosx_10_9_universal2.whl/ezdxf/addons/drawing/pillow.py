#  Copyright (c) 2022, Manfred Moitzi
#  License: MIT License
from __future__ import annotations

import sys
from typing import Iterable, Tuple
import math
from ezdxf.math import Vec3, Vec2, Matrix44, AbstractBoundingBox
from ezdxf.addons.drawing.backend import Backend
from ezdxf.addons.drawing.properties import Properties
from ezdxf.addons.drawing.type_hints import Color

from ezdxf.tools.fonts import FontFace, FontMeasurements
from .config import Configuration

try:
    from PIL import Image, ImageDraw
except ImportError:
    # The original PIL package does not work with Python3!
    print(
        "require Pillow package not found, install by:\n\n"
        "    pip install Pillow"
    )
    sys.exit(1)


INCH_TO_MM = 25.6


class PillowBackend(Backend):
    def __init__(
        self,
        region: AbstractBoundingBox,
        image_size: Tuple[int, int] = None,
        resolution: float = 1.0,
        margin: int = 10,
        dpi: int = 300,
        oversampling: int = 1,
    ):
        """Experimental backend to use Pillow for image export.

        Current limitations:

            - no text support
            - no linetype support
            - no hatch pattern support
            - holes in hatches are not supported

        Args:
            region: output region of the layout in DXF drawing units
            image_size: image output size in pixels or ``None`` to be
                calculated by the region size and the `resolution`
            margin: image margin in pixels, same margin for all four borders
            resolution: pixels per DXF drawing unit, e.g. a resolution of 100
                for the drawing unit "meter" means, each pixel represents an
                area of 1cm x 1cm (1m is 100cm).
                If the `image_size` is given the `resolution` is calculated
                automatically
            dpi: output image resolution in dots per inch. The pixel width of
                lines is determined by the DXF lineweight (in mm) and this image
                resolution (dots/pixels per inch). The line width is independent
                of the drawing scale!
            oversampling: multiplier of the final image size to define the
                render canvas size (e.g. 1, 2, 3, ...), the final image will
                be scaled down by the LANCZOS method

        """
        super().__init__()
        self.region = Vec2(region.size)
        if self.region.x <= 0.0 or self.region.y <= 0.0:
            raise ValueError("drawing region is empty")
        self.extmin = Vec2(region.extmin)
        self.margin_x = float(margin)
        self.margin_y = float(margin)
        self.dpi = int(dpi)
        self.oversampling = max(int(oversampling), 1)
        # The lineweight is stored im mm,
        # line_pixel_factor * lineweight is the width in pixels
        self.line_pixel_factor = self.dpi / INCH_TO_MM  # pixel per mm
        # resolution: pixels per DXF drawing units, same resolution in all
        # directions
        self.resolution = float(resolution)
        if image_size is None:
            image_size = (
                math.ceil(self.region.x * resolution + 2.0 * self.margin_x),
                math.ceil(self.region.y * resolution + 2.0 * self.margin_y),
            )
        else:
            img_x, img_y = image_size
            if img_y < 1:
                raise ValueError(f"invalid image size: {image_size}")
            img_ratio = img_x / img_y
            region_ratio = self.region.x / self.region.y
            if img_ratio >= region_ratio:  # image fills the height
                self.resolution = (img_y - 2.0 * self.margin_y) / self.region.y
                self.margin_x = (img_x - self.resolution * self.region.x) * 0.5
            else:  # image fills the width
                self.resolution = (img_x - 2.0 * self.margin_x) / self.region.x
                self.margin_y = (img_y - self.resolution * self.region.y) * 0.5

        self.image_size = Vec2(image_size)
        self.bg_color: Color = "#000000"
        self.image_mode = "RGBA"

        # dummy values for declaration, both are set in clear()
        self.image = Image.new("RGBA", (10, 10))
        self.draw = ImageDraw.Draw(self.image)

    def configure(self, config: Configuration) -> None:
        super().configure(config)
        self.line_pixel_factor *= self.config.lineweight_scaling

    # noinspection PyTypeChecker
    def clear(self):
        x = int(self.image_size.x) * self.oversampling
        y = int(self.image_size.y) * self.oversampling
        self.image = Image.new(self.image_mode, (x, y), color=self.bg_color)
        self.draw = ImageDraw.Draw(self.image)

    def set_background(self, color: Color) -> None:
        self.bg_color = color
        self.clear()

    def width(self, lineweight: float) -> int:
        return max(int(lineweight * self.line_pixel_factor), 1)

    def pixel_loc(self, point: Vec3) -> Tuple[float, float]:
        # Source: https://pillow.readthedocs.io/en/stable/handbook/concepts.html#coordinate-system
        # The Python Imaging Library uses a Cartesian pixel coordinate system,
        # with (0,0) in the upper left corner. Note that the coordinates refer
        # to the implied pixel corners; the centre of a pixel addressed as
        # (0, 0) actually lies at (0.5, 0.5).
        x = (point.x - self.extmin.x) * self.resolution + self.margin_x
        y = (point.y - self.extmin.y) * self.resolution + self.margin_y
        return (
            x * self.oversampling,
            # (0, 0) is the top-left corner:
            (self.image_size.y - y) * self.oversampling,
        )

    def draw_point(self, pos: Vec3, properties: Properties) -> None:
        self.draw.point([self.pixel_loc(pos)], fill=properties.color)

    def draw_line(self, start: Vec3, end: Vec3, properties: Properties) -> None:
        self.draw.line(
            [self.pixel_loc(start), self.pixel_loc(end)],
            fill=properties.color,
            width=self.width(properties.lineweight),
        )

    def draw_filled_polygon(
        self, points: Iterable[Vec3], properties: Properties
    ) -> None:
        points = [self.pixel_loc(p) for p in points]
        if len(points) > 2:
            self.draw.polygon(
                points,
                fill=properties.color,
                outline=properties.color,
            )

    def draw_text(
        self,
        text: str,
        transform: Matrix44,
        properties: Properties,
        cap_height: float,
    ) -> None:
        # text is not supported yet
        pass

    def get_font_measurements(
        self, cap_height: float, font: FontFace = None
    ) -> FontMeasurements:
        # text is not supported yet
        return FontMeasurements(
            0.0, cap_height, cap_height * 0.666, cap_height * 0.333
        )

    def get_text_line_width(
        self, text: str, cap_height: float, font: FontFace = None
    ) -> float:
        # text is not supported yet
        return 0.0

    def export(self, filename: str, **kwargs) -> None:
        image = self.image
        if self.oversampling > 1:
            x = int(self.image_size.x)
            y = int(self.image_size.y)
            image = self.image.resize((x, y), resample=Image.LANCZOS)
        if not supports_transparency(filename):
            # remove alpha channel if not supported
            image = image.convert("RGB")
        dpi = kwargs.pop("dpi", self.dpi)
        image.save(filename, dpi=(dpi, dpi), **kwargs)


SUPPORT_TRANSPARENCY = [".png", ".tif", ".tiff"]


def supports_transparency(filename: str) -> bool:
    filename = filename.lower()
    return any(filename.endswith(ftype) for ftype in SUPPORT_TRANSPARENCY)
