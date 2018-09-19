import pytest
from .depth_first import Graph


def test_graph_exists():
    assert Graph


def test_graph_adds_edge(graph_filled):
    graph_filled.add_edge('C', 'A', 77)
    assert graph_filled.graph == {
        'A': {'B': 10},
        'B': {'A': 5, 'D': 15, 'C': 20},
        'C': {'A': 77},
        'D': {'A': 5},
        'E': {},
        'F': {}
    }


def test_graph_adds_vert(graph_filled):
    graph_filled.add_vert('G')
    assert graph_filled.graph == {
        'A': {'B': 10},
        'B': {'A': 5, 'D': 15, 'C': 20},
        'C': {},
        'D': {'A': 5},
        'E': {},
        'F': {},
        'G': {},
    }


def test_has_vert(graph_filled):
    assert graph_filled.has_vert('D')


def test_doesnt_have_vert(graph_filled):
    assert not graph_filled.has_vert('Z')


def test_empty_doesnt_have_vert(graph_empty):
    assert not graph_empty.has_vert('Z')


def test_gets_no_neighbors_none(graph_filled):
    assert graph_filled.get_neighbors('Z') == []


def test_gets_no_neighbors_actual(graph_filled):
    assert graph_filled.get_neighbors('A') == {'B': 10}.keys()


def test_returns_length(graph_filled):
    assert len(graph_filled) == 6


def test_returns_length_empty(graph_empty):
    assert len(graph_empty) == 0


def test_one_vertex_confused():
    g = Graph()
    g.graph = {
        'A': {}
    }
    assert g.depth_first_graph('A') == ['A']


def test_many_vertices_works():
    g = Graph()
    g.graph = {
        'A': {'B': 1, 'C': 1},
        'B': {'A': 1, 'C': 1},
        'C': {'A': 1, 'B': 1}
    }
    assert g.depth_first_graph('A') == ['A', 'C', 'B']


def test_start_not_in_graph(graph_line):
    with pytest.raises(KeyError):
        graph_line.depth_first_graph('Q')


def test_no_start_given(graph_line):
    with pytest.raises(TypeError):
        graph_line.depth_first_graph()


def test_graph_straight_line(graph_line):
    assert graph_line.depth_first_graph('A') == ['A', 'B', 'C', 'D', 'E', 'F']


def test_graph_is_tree():
    g = Graph()
    g.graph = {
        'A': {'B': 1, 'C': 1},
        'B': {'D': 1},
        'C': {},
        'D': {}
    }
    assert g.depth_first_graph('A') == ['A', 'C', 'B', 'D']
