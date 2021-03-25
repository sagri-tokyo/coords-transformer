from coords_transformer.constants import L, ZOOM
import math

# These calculations are based on the follwing link.
# https://www.trail-note.net/tech/coordinate/

def convert_lng_zoom_to_x(lng: float, zoom: int = ZOOM) -> int:
    return round((2 ** (zoom + 7)) * ((lng / 180) + 1))


def convert_lat_zoom_to_y(lat: float, zoom: int = ZOOM) -> int:
    atanh_value = math.sin((math.pi / 180) * L)
    return round(((2 ** (zoom + 7)) / math.pi) * ((-1 * math.atanh(math.sin((math.pi / 180) * lat))) + (math.atanh(atanh_value))))


def convert_x_zoom_to_lng(x: int, zoom: int = ZOOM) -> float:
    return 180 * ((x / 2 ** (zoom + 7)) - 1)


def convert_y_zoom_to_lat(y: int, zoom: int = ZOOM) -> float:
    atanh_value = math.sin((math.pi / 180) * L)
    tanh_value = -1 * (math.pi / (2 ** (zoom + 7))) * y + math.atanh(atanh_value)
    return (180 / math.pi) * (math.asin(math.tanh(tanh_value)))
