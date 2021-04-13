import pytest
from coords_transformer.filename.filename import FileName


SAMPLE_FILENAME_STRS = [
	"0_long141dot242035-lati45dot178506-size512-zoom17.jpg",
	"1_long138dot943905-lati35dot855499-size512-zoom17.jpg",
	"2_long130dot504283-lati30dot335927-size512-zoom17.jpg"
    ]


SAMPLE_FILENAME_OBJS = [
    FileName(lat=45.178506, lng=141.242035, idx=0, size=512, path="/", zoom=17),
	FileName(lat=35.855499, lng=138.943905, idx=1, size=512, path="/", zoom=17),
	FileName(lat=30.335927, lng=130.504283, idx=2, size=512, path="/", zoom=17)
]


class TestFileNameFactory:
	@pytest.fixture(scope="class")
	def filename_factory(self):
		from coords_transformer.filename.factory import FileNameFactory
		filename_factory = FileNameFactory()
		return filename_factory


	def test_create_from_filename(self, filename_factory):
		for filename_str, filename_obj in zip(SAMPLE_FILENAME_STRS, SAMPLE_FILENAME_OBJS):
			assert filename_factory.create_from_filename(filename=filename_str, path=filename_obj.path) == filename_obj
