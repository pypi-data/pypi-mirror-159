from hypothesis import strategies as st

from hexagonal import Vec


@st.composite
def veci(draw, x=st.integers(), y=st.integers()) -> Vec[int]:
    return Vec(draw(x), draw(y))
