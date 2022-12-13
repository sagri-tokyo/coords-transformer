from coords_transformer.filename.filename import FileName
from pathlib import Path


def create_from_filename(filename: str, path: str):
	"""
	Args:
		filename: name of file in the designated format.
		path: path to file
	Returns:
		Filename object
	"""
	filename = Path(filename).stem
	idx = filename.split('_')[0]
	filename = filename.replace(f'{idx}_', '', 1)
	count_bar = filename.count('_')
	if count_bar == 3:
		lng, lat, size, zoom = filename.split('_')
		print(lng, lat, size, zoom)
	else:
		raise ValueError('期待するフォーマットは{idx}_long{lng}_lati{lat}_size{size}_zoom{zoom}です')
	
	lng = float(lng.replace('long', '').replace('dot', '.'))
	lat = float(lat.replace('lati', '').replace('dot', '.'))
	size = int(size.replace('size', ''))
	zoom = int(zoom.replace('zoom', ''))
	return FileName(lng=lng, lat=lat, idx=idx, size=size, path=path, zoom=zoom)
