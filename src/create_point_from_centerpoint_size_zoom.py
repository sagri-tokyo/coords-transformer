from src.point.factory import *
from src.point.point import Point
from typing import List


def create_point_from_centerpoint_size_zoom(point: List[int], center_point: Point, size : int, zoom: int) -> Point:
	diff = int(size / 2)
	origin_x = center_point.x - diff
	origin_y = center_point.y - diff
	point_obj = create_from_x_y_zoom(x=origin_x + point[0],
									y=origin_y + point[1],
									zoom=zoom)
	return point_obj
