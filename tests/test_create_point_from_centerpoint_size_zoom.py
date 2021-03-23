import pytest
from src.constants import ZOOM, PIXEL_SIZE
from src.create_point_from_image_pixel_coords import *

SAMPLE_PIXEL_COORDS = [256, 256]

@pytest.fixture(params=SAMPLE_PIXEL_COORDS, scope="function")
def sample_pixel_coords(request):
    return request.param

def test_create_point_from_image_pixel_coords(sample_point):
	point_obj = create_point_from_image_pixel_coords(SAMPLE_PIXEL_COORDS, sample_point, PIXEL_SIZE, ZOOM)
	assert point_obj.__dict__ == pytest.approx(sample_point.__dict__)
