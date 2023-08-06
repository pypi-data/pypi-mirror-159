from typing import List
from meshgraph.Node import Node


class Graph:
    """
    Undirected Graph

    ...

    Attributes
    ----------
    nodes : List[Node]
        nodes (or vertices) composing the graph

    Methods
    -------
    add_node(node)
        Adds new node to the graph
    subtract_node(sub_nodes)
        Subtracts a list of nodes from the existing nodes. It is not guaranteed that the remaining nodes are sorted
        by index. For this, use <subtract_nodes_sorted>
    subtract_nodes_sorted(sub_nodes)
        Subtracts a list of nodes from the existing nodes and sorts the remaining nodes by index
    reset_nodes_indexes()
        Resets the nodes' index. After calling this function, the first node will have index=0, the second one
        1 and so on...
    sort_nodes(sub_nodes)
        Sorts nodes by node index
    print()
        Prints all the nodes and their neighbors in a pretty format

    """

    __slots__ = ('nodes')

    def __init__(self):
        self.nodes = []

    def add_node(self, node: Node):
        self.nodes.append(node)

    def get_node(self, index: int) -> Node:
        return self.nodes[index]

    def subtract_nodes(self, sub_nodes: List[Node]):
        """Subtracts a list of nodes from the existing nodes. It is not guaranteed that the remaining nodes are sorted
        by index. For this, use <subtract_nodes_sorted>"""
        self.nodes = list(set(self.nodes) - set(sub_nodes))

    def subtract_nodes_sorted(self, sub_nodes: List[Node]):
        """Subtracts a list of nodes from the existing nodes and sorts the remaining nodes by index"""
        self.subtract_nodes(sub_nodes)
        self.sort_nodes()

    def reset_nodes_indexes(self):
        """Resets the nodes' index. After calling this function, the first node will have index=0, the second one
        1 and so on..."""
        if len(self.nodes) == 0:
            return
        current_index = 0
        for n in self.nodes:
            n.index = current_index
            current_index += 1

    def sort_nodes(self):
        """Sort nodes collection by node index"""
        self.nodes = sorted(self.nodes, key=lambda n: n.index)

    def print(self):
        """Prints a pretty string representation of the current node and its neighbors."""
        for n in self.nodes:
            print(n)
            print("\tneighbors:" + str(n.neighbors))
