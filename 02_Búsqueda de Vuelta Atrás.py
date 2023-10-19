def is_valid_assignment(graph, node, color, assignment):
    for neighbor in graph[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(graph, colors, assignment, node):
    if node is None:
        return True  # Todas las asignaciones se han realizado con éxito

    for color in colors:
        if is_valid_assignment(graph, node, color, assignment):
            assignment[node] = color
            if backtrack(graph, colors, assignment, next_node(graph, assignment)):
                return True
            assignment[node] = None

    return False

def next_node(graph, assignment):
    for node in graph:
        if assignment[node] is None:
            return node
    return None

def solve_graph_coloring(graph, colors):
    assignment = {node: None for node in graph}
    if backtrack(graph, colors, assignment, next_node(graph, assignment)):
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

result = solve_graph_coloring(graph, colors)
if result:
    print("Solución encontrada:")
    for node, color in result.items():
        print(f"Nodo {node} coloreado como {color}")
else:
    print("No se encontró una solución válida.")
