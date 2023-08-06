import math


class Vec3:
    """
    Vector 3D representing a point in Euclidian space

    ...

    Attributes
    ----------
    x : float
        the X coordinate
    y : float
        the Y coordinate
    z : float
        the Z coordinate

    Methods
    -------
    distance(other: Vec3)
        Returns the euclidean distance between the current vec3 and the other

    """

    __slots__ = ('x', 'y', 'z')

    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def distance(self, other: 'Vec3') -> float:
        dx = (self.x - other.x)**2
        dy = (self.y - other.y)**2
        dz = (self.z - other.z)**2
        return math.sqrt(dx + dy + dz)

    def __eq__(self, other: 'Vec3'):
        return self.x == other.x \
               and self.y == other.y \
               and self.z == other.z

    def __str__(self):
        return "[" + str(self.x) \
            + "," + str(self.y) \
            + "," + str(self.z)\
            + "]"
