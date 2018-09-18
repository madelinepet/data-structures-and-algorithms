import pytest
from .get_edges import Graph
from .get_edges import get_edges


def test_graph_exists():
    assert Graph
    assert get_edges


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


def test_direct_2_verts(graph_filled_airline):
    assert graph_filled_airline
    assert get_edges(['Pandora', 'Arendelle'], graph_filled_airline) == (True, '$150')


def test_direct_3_verts(graph_filled_airline):
    assert get_edges(['Pandora', 'Arendelle', 'Metropolis'], graph_filled_airline) == (True, '$249')


def test_1_vertex_false(graph_filled_airline):
    assert get_edges(['Pandora'], graph_filled_airline) == (False, '$0')


def test_not_direct_two_verts(graph_filled_airline):
    assert get_edges(['Pandora', 'Naboo'], graph_filled_airline) == (False, '$0')


def test_not_direct_three_verts(graph_filled_airline):
    assert get_edges(['Pandora', 'Arendelle', 'Narnia'], graph_filled_airline) == (False, '$0')


def test_non_existing_verts(graph_filled_airline):
    assert get_edges(['Pandora', 'dkfjhekjrlwk'], graph_filled_airline) == (False, '$0')


def test_input_field_omitted(graph_filled_airline):
    with pytest.raises(TypeError):
        get_edges(['Pandora', 'Arendelle'])


def test_bad_input_iter_not_list(graph_filled_airline):
    assert get_edges('Pandora', graph_filled_airline) == (False, '$0')


def test_non_iter_input(graph_filled_airline):
    assert get_edges(8, graph_filled_airline) == (False, '$0')


