import pytest

@pytest.mark.usefixtures("setup_zoom")
class TestCoordinatesTransformer:
    @pytest.fixture(scope="class")
    def coordinates_transformer(self):
        from coordinates_transformer import CoordinatesTransformer
        yield CoordinatesTransformer

    def test_convert_lng_zoom_to_x(self, coordinates_transformer, sample_point):
        assert coordinates_transformer.convert_lng_zoom_to_x(sample_point.lng) == pytest.approx(sample_point.x)

    def test_convert_lat_zoom_to_y(self, coordinates_transformer, sample_point):
        assert coordinates_transformer.convert_lat_zoom_to_y(sample_point.lat) == pytest.approx(sample_point.y)

    def test_convert_x_zoom_to_lng(self, coordinates_transformer, sample_point):
        assert coordinates_transformer.convert_x_zoom_to_lng(sample_point.x) == pytest.approx(sample_point.lng, abs=1e-5)

    def test_convert_y_to_lat(self, coordinates_transformer, sample_point):
        assert coordinates_transformer.convert_y_to_lat(sample_point.y) == pytest.approx(sample_point.lat, abs=1e-5)
