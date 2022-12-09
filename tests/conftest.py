import pytest
from coords_transformer.point.point import Point


#  Values used as parameters are on the follwing link.
#  https://www.trail-note.net/tech/coordinate/
#  全てテストケースはzoom = 17で固定
SAMPLE_POINTS = [
    Point(x=29941927, y=12046802, lng=141.242035, lat=45.178506),
    Point(x=29727726, y=13192979, lng=138.943905, lat=35.855499),
    Point(x=28941096, y=13807510, lng=130.504283, lat=30.335927),
    Point(x=11582311, y=17437262, lng=-55.735281, lat=-7.063564),
    Point(x=28701731, y=19343721, lng=127.936168, lat=-26.533028),
    Point(x=8110898, y=12745631, lng=-92.979500, lat=39.648800),
]


@pytest.fixture(params=SAMPLE_POINTS, scope="function")
def sample_point(request):
    return request.param
