from pytest import approx
from hexagonal import Vec
from hypothesis import given, strategies as st

from . import veci


@given(
    st.integers(min_value=-100, max_value=100),
    st.integers(min_value=-100, max_value=100),
)
def test_inverse(x, y):
    v = Vec(x, y)
    assert Vec.from_cartesian(*v.to_cartesian()).to_tuple() == approx(v.to_tuple())


@given(
    st.integers(min_value=-100, max_value=100),
    st.integers(min_value=-100, max_value=100),
)
def test_inverse_other_way(x, y):
    assert Vec.from_cartesian(x, y).to_cartesian() == approx((x, y))


@given(
    st.integers(min_value=-100, max_value=100),
    st.integers(min_value=-100, max_value=100),
    st.integers(min_value=-100, max_value=100),
    st.integers(min_value=-100, max_value=100),
)
def test_cartesian_addition(x1, y1, x2, y2):
    u = Vec(x1, y1)
    v = Vec(x2, y2)
    assert (u + v).to_cartesian() == approx(
        tuple(u.to_cartesian()[i] + v.to_cartesian()[i] for i in range(2))
    )
