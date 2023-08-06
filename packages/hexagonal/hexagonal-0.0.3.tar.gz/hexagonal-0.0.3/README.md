# Hexagonal

`hexagonal` provides hexagonal vectors.

## Usage

```python
>>> import hexagonal
```

Create a vector from cube coordinates, with x + y + z = 0. x is
south-east-ish, y is north and z is south-west-ish.

```python
>>> v = hexagonal.Vec(x=4, y=3, z=-7)
>>> v
Vec(4, 3, -7)
```

Coordinates can be accessed, but not modified. `hexagonal.Vec` is
immutable.

```python
>>> v.x
4
>>> v.y
3
>>> v.z
-7
```

The `z` coordinate is optional.

```python
>>> u = hexagonal.Vec(4, 5)
```

Arithmetic is supported.

```python
>>> v + u
Vec(8, 8, -16)
>>> v - u
Vec(0, -2, 2)
```

`abs` gives the hexagonal distance to the vector, i.e. the radius of the
hexagon on which it sits.

```python
>>> abs(u)
9
```
