import pytest

@pytest.mark.usefixtures("setup_zoom")
class TestCoordsTransformer:
    @pytest.fixture(scope="class")
    def coords_transformer(self):
        from src.coords_transformer import CoordsTransformer
        yield CoordsTransformer

    def test_convert_lng_zoom_to_x(self, coords_transformer, sample_point):
        assert coords_transformer.convert_lng_zoom_to_x(sample_point.lng) == pytest.approx(sample_point.x)

    def test_convert_lat_zoom_to_y(self, coords_transformer, sample_point):
        assert coords_transformer.convert_lat_zoom_to_y(sample_point.lat) == pytest.approx(sample_point.y)

    def test_convert_x_zoom_to_lng(self, coords_transformer, sample_point):
        assert coords_transformer.convert_x_zoom_to_lng(sample_point.x) == pytest.approx(sample_point.lng, abs=1e-5)

    def test_convert_y_to_lat(self, coords_transformer, sample_point):
        assert coords_transformer.convert_y_to_lat(sample_point.y) == pytest.approx(sample_point.lat, abs=1e-5)
