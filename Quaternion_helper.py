

from typing import overload


class Quaternion:
    def __init__(self, a, b, c, d) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __add__(self, other):
        return Quaternion(self.a + other.a, self.b + other.b, self.c + other.c, self.d + other.d)

    def __sub__(self, other):
        return Quaternion(self.a - other.a, self.b - other.b, self.c - other.c, self.d - other.d)

    def __str__(self) -> str:
        return f"({f'{self.a} + ' if not self.a == 0 else ''}{self.b}i + {self.c}j + {self.d}k)"

    def __repr__(self) -> str:
        return f"({f'{self.a} + ' if not self.a == 0 else ''}{self.b}i + {self.c}j + {self.d}k)"


class Point3D(Quaternion):
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)


    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"

    def __repr__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"
