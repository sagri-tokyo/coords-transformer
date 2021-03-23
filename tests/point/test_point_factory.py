import pytest
from src.point.factory import *

def test_create_from_x_y_zoom(sample_point):
	assert create_from_x_y_zoom(x=sample_point.x, y=sample_point.y).__dict__ == pytest.approx(sample_point.__dict__)

def test_create_from_lat_lng_zoom(sample_point):
	assert create_from_lat_lng_zoom(lat=sample_point.lat, lng=sample_point.lng).__dict__ == pytest.approx(sample_point.__dict__)
