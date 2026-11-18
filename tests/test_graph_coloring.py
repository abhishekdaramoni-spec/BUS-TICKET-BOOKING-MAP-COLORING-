import pytest
from algorithms.graph_coloring import greedy_coloring, has_color_conflict, create_seat_graph

def test_two_connected_vertices():
    graph = {
        'A': ['B'],
        'B': ['A']
    }
    colors = greedy_coloring(graph)
    assert colors['A'] != colors['B']

def test_triangle_graph():
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'C'],
        'C': ['A', 'B']
    }
    colors = greedy_coloring(graph)
    # Should use 3 distinct colors
    assert len(set(colors.values())) == 3

def test_square_graph():
    graph = {
        'A': ['B', 'D'],
        'B': ['A', 'C'],
        'C': ['B', 'D'],
        'D': ['A', 'C']
    }
    colors = greedy_coloring(graph)
    # Bipartite graph should use exactly 2 colors
    assert len(set(colors.values())) == 2
    assert colors['A'] == colors['C']
    assert colors['B'] == colors['D']

class DummySeat:
    def __init__(self, num):
        self.seat_number = num

def test_bus_seat_graph_conflicts():
    seats = [DummySeat(f"{r}{c}") for r in ['A','B'] for c in ['1','2','3']]
    graph = create_seat_graph(seats)
    colors = greedy_coloring(graph)
    
    assert not has_color_conflict(graph, colors)
    # verify specifically
    assert colors['A1'] != colors['A2']
    assert colors['A1'] != colors['B1']

def test_disconnected_seats():
    graph = {
        'A1': [],
        'Z9': []
    }
    colors = greedy_coloring(graph)
    assert colors['A1'] == 0
    assert colors['Z9'] == 0

def test_rerun_algorithm():
    graph = {
        'A1': ['A2', 'B1'],
        'A2': ['A1', 'B2'],
        'B1': ['A1', 'B2'],
        'B2': ['A2', 'B1']
    }
    colors1 = greedy_coloring(graph)
    colors2 = greedy_coloring(graph)
    assert colors1 == colors2
    assert not has_color_conflict(graph, colors1)
