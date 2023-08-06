from meshgraph.Vec3 import Vec3


class Node:
    """
    Node representing a vertex in Euclidian space

    ...

    Attributes
    ----------
    pos : Vec3
        The coordinates of the Node
    neighbors : Set[Node]
        The set containing the neighbors of the current node

    Methods
    -------
    add_neighbor(node: Node)
        Adds new node to the neighbors

    """

    __slots__ = ('pos', '_index', 'neighbors')

    def __init__(self, x, y, z, index=None):
        self.pos = Vec3(x, y, z)
        self._index = index
        self.neighbors = set()

    @property
    def index(self) -> int:
        return self._index

    @index.setter
    def index(self, value):
        self._index = value

    def add_neighbor(self, node: 'Node'):
        """Add new Node instance to neighbors"""
        self.neighbors.add(node)

    def __str__(self):
        return "V" + str(self._index) \
            + str(self.pos)

    def __repr__(self):
        return str(self)
