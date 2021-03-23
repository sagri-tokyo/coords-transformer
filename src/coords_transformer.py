from src.constants import L, ZOOM
import math


def convert_lng_zoom_to_x(lng: float, zoom: int = ZOOM):
    return round((2 ** (zoom + 7)) * ((lng / 180) + 1))

def convert_lat_zoom_to_y(lat: float, zoom: int = ZOOM):
    return round(((2 ** (zoom + 7)) / math.pi) * ((-1 * math.atanh(math.sin((math.pi / 180) * lat))) + (math.atanh(math.sin((math.pi / 180) * L)))))

def convert_x_zoom_to_lng(x: int, zoom: int = ZOOM):
    return 180 * ((x / 2 ** (zoom + 7)) - 1)

def convert_y_to_lat(y: int, zoom: int = ZOOM):
    atanh_value = math.sin((math.pi / 180) * L)
    tanh_value = -1 * (math.pi / (2 ** (zoom + 7))) * y + math.atanh(atanh_value)
    return (180 / math.pi) * (math.asin(math.tanh(tanh_value)))
