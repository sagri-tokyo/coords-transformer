from src.point.point import Point
from src.coords_transformer import *
from src.constants import ZOOM

def create_from_x_y_zoom(x, y, zoom=ZOOM):
	lng = convert_x_zoom_to_lng(x, zoom)
	lat = convert_y_to_lat(y, zoom)
	return Point(x=x, y=y, lng=lng, lat=lat)

def create_from_lat_lng_zoom(lat, lng, zoom=ZOOM):
	x = convert_lng_zoom_to_x(lng, zoom)
	y = convert_lat_zoom_to_y(lat, zoom)
	return Point(x=x, y=y, lng=lng, lat=lat)
