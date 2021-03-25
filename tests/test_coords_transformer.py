import pytest
from coords_transformer.coords_calculation import *


class TestCoordsTransformer:
    def test_convert_lng_zoom_to_x(self, sample_point):
        assert convert_lng_zoom_to_x(sample_point.lng) == pytest.approx(sample_point.x)

    def test_convert_lat_zoom_to_y(self, sample_point):
        assert convert_lat_zoom_to_y(sample_point.lat) == pytest.approx(sample_point.y)

    def test_convert_x_zoom_to_lng(self, sample_point):
        assert convert_x_zoom_to_lng(sample_point.x) == pytest.approx(sample_point.lng, abs=1e-5)

    def test_convert_y_zoom_to_lat(self, sample_point):
        assert convert_y_zoom_to_lat(sample_point.y) == pytest.approx(sample_point.lat, abs=1e-5)
