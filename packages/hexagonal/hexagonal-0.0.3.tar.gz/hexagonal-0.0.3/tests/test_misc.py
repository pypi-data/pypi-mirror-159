import math

from pytest import approx
from hypothesis import given, strategies as st
from hexagonal import Direction, Vec

from . import veci


@given(veci())
def test_to_tuple(v):
    assert Vec(v.to_tuple()[0], v.to_tuple()[1]) == v


@given(veci())
def test_repr(v):
    assert eval(repr(v)) == v


@given(veci())
def test_invariant(v):
    assert v.x + v.y + v.z == 0


@given(veci())
def test_bool(v):
    assert bool(v) == (v != Vec(0, 0))


@given(st.integers())
def test_abs(n):
    assert all([abs(d.value * n) == abs(n) for d in Direction])


@given(veci())
def test_round_ints(v):
    assert v.round() == v
