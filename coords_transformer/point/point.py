from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    lng: float
    lat: float
    x: int
    y: int
