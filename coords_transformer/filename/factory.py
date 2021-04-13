from coords_transformer.constants import ZOOM, PIXEL_SIZE
from coords_transformer.filename.filename import FileName
import re


class FileNameFactory:
	def create_from_filename(self, filename: str, path: str, size: int = PIXEL_SIZE):
		"""
		Args:
			filename: name of file which is in designated format.
			path: path to file
			size: image file pixel size
		Returns:
			a Filename object
		"""
		dot_converted_filename = filename.replace('dot', '.')
		idx = int(re.search('^([\d\.]*)_long', dot_converted_filename).group(1))
		lng = float(re.search('long([\d\.]*)', dot_converted_filename).group(1))
		lat = float(re.search('lati([\d\.]*)', dot_converted_filename).group(1))
		size = int(re.search('size(\d*)', dot_converted_filename).group(1))
		zoom = int(re.search('zoom(\d*)', dot_converted_filename).group(1))

		return FileName(lng=lng, lat=lat, idx=idx, size=size, path=path, zoom=zoom)
