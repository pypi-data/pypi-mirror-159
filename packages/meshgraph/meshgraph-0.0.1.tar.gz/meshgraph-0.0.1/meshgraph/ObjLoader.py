from meshgraph.Graph import Graph
from meshgraph.Node import Node


def _load_file_content(path):
    with open(path) as f:
        lines = [line for line in f]
        return lines


def _parse_vertex_line(line, graph):
    coordinates = line.split()
    new_node = Node(float(coordinates[1]),
                    float(coordinates[2]),
                    float(coordinates[3]))
    new_node.index = len(graph.nodes)
    graph.add_node(new_node)


def _get_vert_index_from_group(vert_group):
    str_index = vert_group.split('/')[0]
    return int(str_index)-1


def _get_vertices_from_face_line(line):
    split_line = line.split()
    verts_indexes = []
    for i in range(1, len(split_line)):
        verts_indexes.append(_get_vert_index_from_group(split_line[i]))
    return verts_indexes


def _link_mutual_neighbors(graph, a, b):
    graph.get_node(a).add_neighbor(graph.get_node(b))
#   undirected graph:
    graph.get_node(b).add_neighbor(graph.get_node(a))


def _solve_graph_neighbors(face_vertices_indexes, graph):
    for i in range(0, len(face_vertices_indexes) - 1):
        _link_mutual_neighbors(graph, face_vertices_indexes[i], face_vertices_indexes[i + 1])
#   link first and last (loop the face vertices):
    _link_mutual_neighbors(graph, face_vertices_indexes[0], face_vertices_indexes[-1])


def _parse_face_line(line, graph):
    face_vertices_indexes = _get_vertices_from_face_line(line)
    _solve_graph_neighbors(face_vertices_indexes, graph)


def _parse_line(line, graph):
    line = line.strip()
    if line.startswith('v '):
        _parse_vertex_line(line, graph)
    elif line.startswith('f '):
        _parse_face_line(line, graph)


def _fill_graph_from_lines(lines, graph):
    for line in lines:
        _parse_line(line, graph)
    print("Graph loaded, %s verts." % len(graph.nodes))
    

def load_graph_from_string(content):
    graph = Graph()
    _fill_graph_from_lines(content.splitlines(), graph)
    return graph


def load_graph_from_file(file_path):
    graph = Graph()
    lines = _load_file_content(file_path)
    _fill_graph_from_lines(lines, graph)
    return graph
