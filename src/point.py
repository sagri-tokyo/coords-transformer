from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    lng: float
    lat: float
    x: int
    y: int

    def x_diff(self, polygon):
        return polygon.x - self.x

    def y_diff(self, polygon):
        return polygon.y - self.y
