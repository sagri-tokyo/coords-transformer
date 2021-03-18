from constants import L, ZOOM
import math


class CoordinatesTransformer:
    @classmethod
    def convert_lng_zoom_to_x(cls, long, zoom=ZOOM):
        return round((2 ** (zoom + 7)) * ((long / 180) + 1))

    @classmethod
    def convert_lat_zoom_to_y(cls, lati, zoom=ZOOM):
        return round(((2 ** (zoom + 7)) / math.pi) * ((-1 * math.atanh(math.sin((math.pi / 180) * lati))) + (math.atanh(math.sin((math.pi / 180) * L)))))

    @classmethod
    def convert_x_zoom_to_lng(cls, x, zoom=ZOOM):
        return 180 * ((x / 2 ** (zoom + 7)) - 1)

    @classmethod
    def convert_y_to_lat(cls, y, zoom=ZOOM):
        atanh_value = math.sin((math.pi / 180) * L)
        tanh_value = -1 * (math.pi / (2 ** (zoom + 7))) * y + math.atanh(atanh_value)
        return (180 / math.pi) * (math.asin(math.tanh(tanh_value)))
