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

A example of designated filename format

This has idx, longitude, latitude of center point, pixel size and zoom level.

`0_long130dot51051050424576-lati33dot25308662907951-size512-zoom17.jpg`

A example of getting a point object with world coordinate, longitude and latitude from pixel coordinate within an image.

```python
from coords_transformer.point.factory import create_from_lat_lng_zoom
from coords_transformer.point.service import create_point_from_image_pixel_coords
from coords_transformer.filename.factory import create_from_filename

# Create a Filename object from filename.
filename = "0_long130dot51051050424576-lati33dot25308662907951-size512-zoom17.jpg"
filename_obj = create_from_filename(filename)

# Create a Point object from latitude, longitude and zoom level.
# This Point obejct should be created from longitude and latitude of an image center point
center_point = create_from_lat_lng_zoom(filename_obj.lat, filename_obj.lng)

# Pass x and y pixel coordinate within an image, center_point, image pixel size and zoom level
# Then you can get a Point object
create_point_from_image_pixel_coords(5, 10, center_point, filename_obj.size, filename_obj.zoom)
```
