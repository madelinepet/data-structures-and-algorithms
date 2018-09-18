import pytest
from .breadth_first_graph import Graph


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


def test_traversal_returns_correct_values(graph_filled):
    assert graph_filled.breadth_first_traversal('A') == ['A', 'B', 'D', 'C']


def test_traversal_of_empty_graph(graph_empty):
    assert graph_empty.breadth_first_traversal('A') == []


def test_returns_one_if_graph_one_node():
    g = Graph()
    g.graph = {
        'A': {},
    }
    assert g.breadth_first_traversal('A') == ['A']


def test_returns_two_if_graph_two_nodes():
    g = Graph()
    g.graph = {
        'A': {},
        'B': {}
    }
    assert g.breadth_first_traversal('A') == ['A']


def test_breaks_if_no_node_passed_in(graph_empty):
    assert graph_empty.breadth_first_traversal('A') == []
