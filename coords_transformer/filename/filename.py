from dataclasses import dataclass


@dataclass(frozen=True)
class FileName:
    lng: float
    lat: float
    idx: int
    size: int
    path: str
    zoom: int


    @property
    def value(self):
        return "{}_long{}-lati{}-size{}-zoom{}".format(self.idx, self.lng, self.lat, self.size, self.zoom).replace('.', 'dot')


    @property
    def jpg(self):
        return self.value + ".jpg"


    @property
    def png(self):
        return self.value + ".png"


    @property
    def json(self):
        return self.value + ".json"


    @property
    def json_path(self):
        return self.path + self.json


    @property
    def jpg_path(self):
        return self.path + self.jpg


    @property
    def png_path(self):
        return self.path + self.png
