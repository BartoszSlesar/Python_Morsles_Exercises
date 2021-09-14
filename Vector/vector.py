from dataclasses import dataclass, astuple


@dataclass(frozen=True)
class Vector(object):
    __slots__ = ('x', 'y', 'z')
    x: float
    y: float
    z: float

    def __iter__(self):
        yield from astuple(self)

    def __add__(self, vector):
        if isinstance(vector, Vector):
            vx, vy, vz = vector
            x = self.x + vx
            y = self.y + vy
            z = self.z + vz
            return Vector(x, y, z)
        else:
            raise TypeError("Please use only Vector clases")

    def __sub__(self, vector):
        if isinstance(vector, Vector):
            vx, vy, vz = vector
            x = self.x - vx
            y = self.y - vy
            z = self.z - vz
            return Vector(x, y, z)
        else:
            raise TypeError("Please use only Vector clases")

    def __rmul__(self, number):
        return self * number

    def __mul__(self, number):
        if isinstance(number, int):
            return Vector(self.x * number, self.y * number, self.z * number)
        else:
            raise TypeError("Please use only int values")

    def __truediv__(self, number):
        if isinstance(number, int):
            return Vector(self.x / number, self.y / number, self.z / number)
        else:
            raise TypeError("Please use only int values")


