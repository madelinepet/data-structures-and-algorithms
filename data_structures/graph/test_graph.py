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
