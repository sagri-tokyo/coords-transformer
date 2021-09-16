import math

u""" These calculations are based on the following link.
https://www.trail-note.net/tech/coordinate/
but replaced atanh(sin((π / 180) * L)) with π.

This simplification is based on the following derivations:
L = 85.05112878
atan(sinh(π)) * 180/π = L + round_error
atanh(sin((π / 180) * atan(sinh(π)) * 180/π)) = π
"""

def convert_lng_zoom_to_x(lng: float, zoom: int) -> int:
    return round((2 ** (zoom + 7)) * ((lng / 180) + 1))


def convert_lat_zoom_to_y(lat: float, zoom: int) -> int:
    return round(((2 ** (zoom + 7)) / math.pi) * ((-1 * math.atanh(math.sin((math.pi / 180) * lat))) + math.pi))


def convert_x_zoom_to_lng(x: int, zoom: int) -> float:
    return 180 * ((x / 2 ** (zoom + 7)) - 1)


def convert_y_zoom_to_lat(y: int, zoom: int) -> float:
    tanh_value = -1 * (math.pi / (2 ** (zoom + 7))) * y + math.pi
    return (180 / math.pi) * (math.asin(math.tanh(tanh_value)))
