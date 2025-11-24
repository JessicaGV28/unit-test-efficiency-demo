from hypothesis import given, strategies as st
from calculator import add, subtract, divide

@given(st.integers(), st.integers())
def test_add_property(a, b):
    assert add(a, b) == a + b  # Propiedad: add es conmutativa y correcta

@given(st.integers(), st.integers())
def test_subtract_property(a, b):
    assert subtract(a, b) + b == a  # Propiedad: subtract inversa de add

@given(st.floats(allow_nan=False, allow_infinity=False), st.floats(min_value=1e-10, allow_nan=False, allow_infinity=False))
def test_divide_property(a, b):
    assert divide(a, b) * b == pytest.approx(a)  # Propiedad: divide inversa de multiply, con tolerancia