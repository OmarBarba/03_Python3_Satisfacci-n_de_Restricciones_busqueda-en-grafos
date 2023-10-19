def is_valid_assignment(graph, assignment):
    for node, color in assignment.items():
        for neighbor in graph[node]:
            if neighbor in assignment and assignment[neighbor] == color:
                return False
    return True

def graph_coloring_csp(graph, colors, assignment, node):
    if node is None:
        return True  # Todas las asignaciones se han realizado con éxito

    for color in colors:
        assignment[node] = color
        if is_valid_assignment(graph, assignment) and graph_coloring_csp(graph, colors, assignment, None):
            return True

        assignment[node] = None

    return False

def solve_graph_coloring_csp(graph, colors):
    assignment = {node: None for node in graph}
    if graph_coloring_csp(graph, colors, assignment, next(iter(graph))):
        return assignment
    else:
        return None

# Ejemplo de uso:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

colors = ['Red', 'Green', 'Blue']

result = solve_graph_coloring_csp(graph, colors)
if result:
    print("Solución encontrada:")
    for node, color in result.items():
        print(f"Nodo {node} coloreado como {color}")
else:
    print("No se encontró una solución válida.")
