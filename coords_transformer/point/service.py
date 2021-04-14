from .factory import create_from_x_y_zoom
from .point import Point


def create_point_from_image_pixel_coords(x_distance: int, y_distance: int, ctr_pt: Point, size: int, zoom: int) -> Point:
    """
    Args:
        x_distance: x pixel coordinate within the satellite image.
        y_distance: y pixel coordinate within the satellite image.
        ctr_pt: the Point object of the center point of the image.
        size: pixel image size.
        zoom: zoom level of the image.
    Returns:
        Point object
    """
    diff = int(size / 2)
    origin_x = ctr_pt.x - diff
    origin_y = ctr_pt.y - diff
    point_obj = create_from_x_y_zoom(x=origin_x + x_distance, y=origin_y + y_distance, zoom=zoom)
    return point_obj
