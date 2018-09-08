import pytest
from .graph import Graph


@pytest.fixture()
def graph_empty():
    g = Graph()
    return g


@pytest.fixture()
def graph_filled():
    g = Graph()
    g.graph = {
        'A': {'B': 10},
        'B': {'A': 5, 'D': 15, 'C': 20},
        'C': {},
        'D': {'A': 5},
        'E': {},
        'F': {}
    }
    return g


@pytest.fixture()
def graph_filled_for_traversal():
    g = Graph()
    g.graph = {
        'A': {'B': 10, 'C': 15},
        'B': {'D': 15, 'E': 5, 'C': 2},
        'C': {'F': 50, 'G': 25},
        'D': {},
        'E': {'C': 5},
        'F': {'E': 10},
        'G': {'F': 20}
    }
    return g


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


def test_has_vert():
    pass


def test_gets_neighbors():
    pass


def test_no_input():
    pass


def test_no_neightbors():
    pass


def test_returns_length():
    pass
