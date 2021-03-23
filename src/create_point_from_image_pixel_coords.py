from src.point.factory import *
from src.point.point import Point
from typing import List


def create_point_from_image_pixel_coords(point: List[int], ctr_pt: Point, size : int, zoom: int) -> Point:
	diff = int(size / 2)
	origin_x = ctr_pt.x - diff
	origin_y = ctr_pt.y - diff
	x,y = point[0], point[1]
	point_obj = create_from_x_y_zoom(x=origin_x + x, y=origin_y + y, zoom=zoom)
	return point_obj
