from math import acos, cos, sin, pi, hypot
import numpy as np


class Vector2D:
    x, y = 0, 0
    magnitude = pow((x ** 2 + y ** 2), 0.5)

    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y
        self.magnitude = pow((x ** 2 + y ** 2), 0.5)
    
    def transformation(self, d):
        self.x = d.x
        self.y = d.y
        self.magnitude = pow((self.x ** 2 + self.y ** 2), 0.5)
    
    def angle(self, r, _roundUp=12):
        return round(acos(self.scalarProduct(r) / (self.magnitude * r.magnitude)) / pi * 180, _roundUp)

    def scalarProduct(self, Vx):
        return Vx.x * Vx.x + Vx.y * Vx.y

    def convertNumpyArray(self):
        return np.array(self.x, self.y)

    def normalize(self):
        return Vector2D(self.x / self.magnitude, self.y/self.magnitude)
    
    def rotateVector2D(self, angle):
        rotatedX = self.x * cos(angle) - self.y * sin(angle)
        rotatedY = self.x * sin(angle) + self.y * cos(angle)
        self.x, self,y = rotatedX, rotatedY
        return self

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.magnitude = pow((self.x ** 2 + self.y ** 2), 0.5)
        return self

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.magnitude = pow((self.x ** 2 + self.y ** 2), 0.5)
        return self

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return self.x != 0 or self.y != 0

    def __neg__(self):
        return Vector2D(-self.x, -self.y)

    def __mul__(self, other:int):
        return Vector2D(self.x * other, self.y * other)
    
    def __mul__(self, other:float):
        return Vector2D(self.x * other, self.y * other)
    
    # def __mul__(self, other):
    #     return Vector3D(0, 0, self.x * other.y - self.y * other.x)
    
    def __truediv__(self, other:float):
        return Vector2D(self.x / other, self.y / other)
    
    def __truediv__(self, other:int):
        return Vector2D(self.x / other, self.y / other)

    def convertNumpyArray(self):
        return np.array(self.x, self.y)



class Vector3D:
    x, y, z = 0, 0, 0
    magnitude = 0

    def __int__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.magnitude = 0

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.magnitude = pow((x ** 2 + y ** 2 + z ** 2), 0.5)

    def angle(self, r, _roundUp=12):
        return round(acos(self.scalarProduct(r) / (self.magnitude * r.magnitude)) / pi * 180, _roundUp)

    def scalarProduct(self, Vx):
        return self.x * Vx.x + self.y * Vx.y + self.z * Vx.z

    def normalize(self):
        self.x /= self.magnitude
        self.y /= self.magnitude
        self.z /= self.magnitude
        self.magnitude = pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        self.magnitude = pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)
        return self

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        self.magnitude = pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)
        return self

    def __abs__(self):
        return hypot(self.x, self.y, self.z)

    def __bool__(self):
        return self.x != 0 or self.y != 0 or self.z

    def __neg__(self):
        return Vector3D(-self.x, -self.y, -self.z)

    def __mul__(self, other):
        return Vector3D(self.y * other.z - self.z * other.y,
                        self.z * other.x - self.x * other.z,
                        self.x * other.y - self.y * other.x)
    
    def __mul__(self, other:int):
        return Vector2D(self.x * other, self.y * other, self.z * other)
    
    def __mul__(self, other:float):
        return Vector2D(self.x * other, self.y * other, self.z * other)
    
    def __truediv__(self, other:float):
        return Vector3D(self.x / other, self.y / other, self.z / other)
    
    def __truediv__(self, other:int):
        return Vector3D(self.x / other, self.y / other, self.z / other)
    
    def convertNumpyArray(self):
        return np.array(self.x, self.y, self.z)
