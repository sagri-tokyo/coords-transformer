import pytest
from coords_transformer.point.factory import *
from coords_transformer.constants import ZOOM


def test_create_from_x_y_zoom(sample_point):
    assert create_from_x_y_zoom(
        sample_point.x, sample_point.y, ZOOM).__dict__ == pytest.approx(sample_point.__dict__)


def test_create_from_lat_lng_zoom(sample_point):
    assert create_from_lat_lng_zoom(
        sample_point.lat, sample_point.lng, ZOOM).__dict__ == pytest.approx(sample_point.__dict__)
