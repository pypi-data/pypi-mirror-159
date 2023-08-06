<div style="text-align:center"><img src="./.media/meshgraph_icon.png" height="200"/></div>

# Intro
This project is born to easily conduct static analysis on 3D mesh geometries. Meshgraph allows you to convert 3D objects
into graphs and thus perform algorithms on them.


# How to use Meshgraph

## Install

Install the _meshgraph_ package using:

```python3  -m pip install meshgraph```

## Convert .obj to Graph

Load a .obj file and convert it to a graph using:

```python
from meshgraph import ObjLoader

graph = ObjLoader.load_graph_from_file(path_to_obj_file)
```

or use a local string:

```python
graph = ObjLoader.load_graph_from_string(obj_string)
```

## Nodes

Nodes can be accessed using:

```python
from meshgraph.Node import Node
#...
graph_nodes = graph.nodes
#Accessing by index:
node0 = graph.nodes[0]
#Or using the accessor function:
node1 = graph.get_node(1)
```

Access a node's position using:
```python
print(node0.pos)
```

Get a distance between two nodes `node0` and `node1` using:
```python
distance = node0.distance(node1)
```

Access the neighbors of a node using:
```python
node0.neighbors
```


# Copyright
Copyright(c) 2022 Sebastiano Campisi - [ianovir.com](https://ianovir.com). 
Read the LICENSE file for more details.