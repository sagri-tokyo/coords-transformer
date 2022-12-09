import pytest
from coords_transformer.filename.filename import FileName
from coords_transformer.filename.factory import create_from_filename


SAMPLE_FILENAME_STRS = [
	"0_long141dot242035-lati45dot178506-size512-zoom17.jpg",
	"1_long138dot943905-lati35dot855499-size512-zoom17.jpg",
	"2_long130dot504283-lati30dot335927-size512-zoom17.jpg",
	"3_long-55dot735281-lati-7dot063564-size512-zoom17.jpg",
	"4_long127dot936168-lati-26dot533028-size512-zoom17.jpg",
	"5_long-92dot979500-lati39dot648800-size512-zoom17.jpg",
    ]


SAMPLE_FILENAME_OBJS = [
    FileName(lat=45.178506, lng=141.242035, idx=0, size=512, path="/", zoom=17),
	FileName(lat=35.855499, lng=138.943905, idx=1, size=512, path="/", zoom=17),
	FileName(lat=30.335927, lng=130.504283, idx=2, size=512, path="/", zoom=17),
	FileName(lng=-55.735281, lat=-7.063564, idx=3, size=512, path="/", zoom=17),
	FileName(lng=127.936168, lat=-26.533028, idx=4, size=512, path="/", zoom=17),
	FileName(lng=-92.979500, lat=39.648800, idx=5, size=512, path="/", zoom=17),
]


class TestFileNameFactory:
	def test_create_from_filename(self):
		for filename_str, filename_obj in zip(SAMPLE_FILENAME_STRS, SAMPLE_FILENAME_OBJS):
			assert create_from_filename(filename=filename_str, path=filename_obj.path) == filename_obj
