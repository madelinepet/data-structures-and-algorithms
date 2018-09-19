import pytest
from .depth_first import Graph


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


@pytest.fixture()
def graph_filled_airline():
    g = Graph()
    g.graph = {
        'Pandora': {'Arendelle': 150, 'Metropolis': 82},
        'Arendelle': {'Pandora': 150, 'Monstropolis': 42, 'Metropolis': 99},
        'Metropolis': {'Pandora': 82, 'Arendelle': 99, 'Monstropolis': 105, 'Naboo': 26, 'Narnia': 37},
        'Monstropolis': {'Arendelle': 42, 'Metropolis': 105, 'Naboo': 73},
        'Naboo': {'Metropolis': 26, 'Monstropolis': 73, 'Narnia': 250},
        'Narnia': {'Metropolis': 37, 'Naboo': 250}
    }
    return g


@pytest.fixture()
def graph_line():
    g = Graph()
    g.graph = {
        'A': {'B': 1},
        'B': {'C': 1},
        'C': {'D': 1},
        'D': {'E': 1},
        'E': {'F': 1},
        'F': {}
    }
    return g
