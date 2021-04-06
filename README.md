# coords-transformer

coords-transformer is a library to transform pixel coordinate to latitude and longitude, and vise versa.


## Installing

Install and update using pip:

```bash
pip install coords-transformer
```

## Examples

Examples of transforming pixel coordinate to latitude and longitude, and vise versa

```python
from coords_transformer.coords_calculation import *

# Get x pixel coordinate from longitude considering zoom level
convert_lng_zoom_to_x(141.242035, 17)

# Get y pixel coordinate from longitude considering zoom level
convert_lat_zoom_to_y(45.178506, 17)

# Get longitude from x pixel coordinate considering zoom level
convert_x_zoom_to_lng(29941927, 17)

# Get latitude from y pixel coordinate considering zoom level
convert_y_zoom_to_lat(12046802, 17)
```

A example of getting a point object with world coordinate, longitude and latitude from pixel coordinate within an image.

```python
from coords_transformer.point.factory import create_from_lat_lng_zoom
from coords_transformer.point.service import create_point_from_image_pixel_coords

# Create a Point object from latitude, longitude and zoom level.
# This Point obejct should be created by longitude and latitude of an image center point
center_point = create_from_lat_lng_zoom(45.178506, 141.242035)
# image pixel size
PIXEl_SIZE = 512
ZOOM = 17

# Pass x and y pixel coordinate within an image, center_point, image pixel size and zoom level
# Then you can get a Point object
create_point_from_image_pixel_coords(5, 10, center_point, PIXEl_SIZE, ZOOM)
```
