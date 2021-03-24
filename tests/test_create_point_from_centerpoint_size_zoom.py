import pytest
from coords_transformer.constants import ZOOM, PIXEL_SIZE
from coords_transformer.point.factory import create_from_x_y_zoom
from coords_transformer.point.service import create_point_from_image_pixel_coords
from tests.conftest import SAMPLE_POINTS

HALF_PIXEL = int(PIXEL_SIZE / 2)
CTR_POINT = SAMPLE_POINTS[0]
ORIGIN_X, ORIGIN_Y = CTR_POINT.x - HALF_PIXEL, CTR_POINT.y - HALF_PIXEL
DIFFS = [{"x": 5, "y": 10}, {"x": 151, "y": 256}, {"x": 501, "y": 432}]


@pytest.mark.parametrize("diff", DIFFS)
def test_create_point_from_image_pixel_coords(diff):
    expected_point = create_from_x_y_zoom(ORIGIN_X + diff["x"], ORIGIN_Y + diff["y"], ZOOM)
    point_obj = create_point_from_image_pixel_coords(diff["x"], diff["y"], CTR_POINT, PIXEL_SIZE, ZOOM)
    assert point_obj.__dict__ == expected_point.__dict__
