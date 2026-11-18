def create_seat_graph(seats):
    """
    Generate an adjacency list graph from the list of seats.
    seats: list of seat objects (or dictionaries) with a 'seat_number' attribute (e.g., 'A1', 'B2').
    """
    graph = {}
    seat_numbers = [seat.seat_number if hasattr(seat, 'seat_number') else seat['seat_number'] for seat in seats]
    
    for seat in seat_numbers:
        graph[seat] = []
        
    for seat in seat_numbers:
        row = seat[0]
        col = int(seat[1:])
        
        # Check horizontal neighbors (same row, col +/- 1)
        left_neighbor = f"{row}{col-1}"
        right_neighbor = f"{row}{col+1}"
        
        # Check vertical neighbors (adjacent row, same col)
        prev_row = chr(ord(row) - 1)
        next_row = chr(ord(row) + 1)
        top_neighbor = f"{prev_row}{col}"
        bottom_neighbor = f"{next_row}{col}"
        
        potential_neighbors = [left_neighbor, right_neighbor, top_neighbor, bottom_neighbor]
        
        for neighbor in potential_neighbors:
            if neighbor in seat_numbers:
                if neighbor not in graph[seat]:
                    graph[seat].append(neighbor)
                    
    return graph

def greedy_coloring(graph):
    """
    Assign colors to graph vertices such that no two adjacent vertices share the same color.
    Uses the Greedy Graph Coloring Algorithm.
    """
    colors = {}
    
    for vertex in graph:
        used_colors = {colors[neighbor] for neighbor in graph[vertex] if neighbor in colors}
        
        color = 0
        while color in used_colors:
            color += 1
            
        colors[vertex] = color
        
    return colors

def has_color_conflict(graph, color_assignment):
    """
    Check if the given color assignment violates graph coloring constraints.
    Returns True if a conflict exists, False otherwise.
    """
    for vertex in graph:
        for neighbor in graph[vertex]:
            if vertex in color_assignment and neighbor in color_assignment:
                if color_assignment[vertex] == color_assignment[neighbor]:
                    return True
    return False
