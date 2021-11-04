

from typing import overload


class Quaternion:
    def __init__(self, a, b, c, d) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def conj(self):
        return Quaternion(self.a, -self.b, -self.c, -self.d)

    def __add__(self, other):
        return Quaternion(self.a + other.a, self.b + other.b, self.c + other.c, self.d + other.d)

    def __sub__(self, other):
        return Quaternion(self.a - other.a, self.b - other.b, self.c - other.c, self.d - other.d)

    def __mul__(self, other):
        return Quaternion(self.a * other.a - self.b * other.b - self.c * other.c - self.d * other.d,
        (self.a * other.b + self.b * other.a + self.c * other.d - self.d * other.c),
        (self.a * other.c - self.b * other.d + self.c * other.a + self.d * other.b),
        (self.a * other.d + self.b * other.c - self.c * other.b + self.d * other.a))

    def __str__(self) -> str:
        return f"({f'{self.a} + ' if not self.a == 0 else ''}{self.b}i + {self.c}j + {self.d}k)"

    def __repr__(self) -> str:
        return f"({f'{self.a} + ' if not self.a == 0 else ''}{self.b}i + {self.c}j + {self.d}k)"


class Point3D(Quaternion):
    def __init__(self, x, y, z) -> None:
        super().__init__(0, x, y, z)
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
