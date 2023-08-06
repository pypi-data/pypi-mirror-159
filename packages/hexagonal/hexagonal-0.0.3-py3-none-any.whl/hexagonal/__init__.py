"""
Hexagonal provides hexagonal vectors.

Vec is a hexagonal vector, either integer or floating-point.
"""
from __future__ import annotations

import itertools
from collections.abc import Iterator
from enum import Enum
from math import sqrt
from random import randint
from typing import Generic, NoReturn, TypeVar, overload

SQRT3 = sqrt(3)

__version__ = "0.0.3"


def positions(radius: int) -> Iterator[Vec[int]]:
    """Get an iterator of integer positions within radius."""
    for x, y in itertools.product(range(-radius, radius + 1), repeat=2):
        pos = Vec(x, y)
        if abs(pos) <= radius:
            yield pos


def random(radius: int) -> Vec[int]:
    """Get a random Vec with at most a given radius."""
    while True:
        pos = Vec(randint(-radius, radius), randint(-radius, radius))
        if abs(pos) <= radius:
            return pos


N = TypeVar("N", float, int, covariant=True)


class Vec(Generic[N]):
    """A hexagonal vector."""

    __slots__ = ("x", "y")
    x: N
    y: N

    def __init__(self, x: N, y: N = 0, z: N | None = None) -> None:
        object.__setattr__(self, "x", x)
        object.__setattr__(self, "y", y)
        if z is not None and x + y + z != 0:
            raise ValueError("x + y + z must be zero")

    @property
    def z(self) -> N:
        return -self.x - self.y

    def __setattr__(self, *_) -> NoReturn:
        raise TypeError(f"{self.__class__.__qualname__} is immutable")

    def __eq__(self, other: object, /) -> bool:
        return isinstance(other, Vec) and self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    @overload
    def __add__(self: Vec[int], other: Vec[int], /) -> Vec[int]:
        ...

    @overload
    def __add__(self: Vec[float], other: Vec[float]) -> Vec[float]:
        ...

    def __add__(self, other, /):
        return Vec(self.x + other.x, self.y + other.y)

    @overload
    def __sub__(self: Vec[int], other: Vec[int], /) -> Vec[int]:
        ...

    @overload
    def __sub__(self: Vec[float], other: Vec[float]) -> Vec[float]:
        ...

    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)

    def __neg__(self) -> Vec[N]:
        return Vec(-self.x, -self.y)

    @overload
    def __mul__(self: Vec[int], scalar: int) -> Vec[int]:
        ...

    @overload
    def __mul__(self: Vec[float], scalar: float) -> Vec[float]:
        ...

    def __mul__(self, scalar):
        return Vec(self.x * scalar, self.y * scalar)

    __rmul__ = __mul__

    def __truediv__(self, scalar: float) -> Vec[float]:
        return Vec(self.x / scalar, self.y / scalar)

    def __str__(self) -> str:
        return f"({self.x} {self.y} {self.z})"

    def __repr__(self) -> str:
        return f"{self.__class__.__qualname__}({self.x}, {self.y}, {self.z})"

    def __bool__(self) -> bool:
        return self.x != 0 or self.y != 0

    def __abs__(self) -> N:
        return max(abs(a) for a in self.to_tuple())

    def to_cartesian(self) -> tuple[float, float]:
        return (SQRT3 * (self.x - self.z) / 2, 1.5 * self.y)

    @classmethod
    def from_cartesian(cls, x, y) -> Vec[float]:
        return Vec((SQRT3 * x - y) / 3, 2 / 3 * y)

    def to_tuple(self) -> tuple[N, N, N]:
        return (self.x, self.y, self.z)

    def round(self) -> Vec[int]:
        tuple_ = self.to_tuple()
        integer = [round(i) for i in tuple_]
        if sum(integer) != 0:
            diffs = [abs(i - j) for i, j in zip(tuple_, integer)]
            must_change = diffs.index(max(diffs))
            integer[must_change] = (
                -integer[(must_change + 1) % 3] + -integer[(must_change + 2) % 3]
            )
        return Vec(*integer)

    def rotate(self, angle: int, /) -> Vec[N]:
        """Return a copy rotated by angle sixths of a turn."""
        angle %= 6
        if angle == 1:
            return Vec(-self.y, -self.z)
        if angle == 2:
            return Vec(self.z, self.x)
        if angle == 3:
            return Vec(-self.x, -self.y)
        if angle == 4:
            return Vec(self.y, self.z)
        if angle == 5:
            return Vec(-self.z, -self.x)
        return self


class Direction(Enum):
    EA = Vec(1, 0, -1)
    NE = Vec(0, 1, -1)
    NW = Vec(-1, 1, 0)
    WE = Vec(-1, 0, 1)
    SW = Vec(0, -1, 1)
    SE = Vec(1, -1, 0)
