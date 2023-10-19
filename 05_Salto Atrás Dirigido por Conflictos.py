def is_valid_assignment(graph, node, color, assignment):
    for neighbor in graph[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def select_unassigned_variable(graph, assignment):
    for node in graph:
        if node not in assignment:
            return node
    return None

def conflict_count(graph, node, color, assignment):
    count = 0
    for neighbor in graph[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            count += 1
    return count

def backjump(graph, colors, assignment):
    unassigned_node = select_unassigned_variable(graph, assignment)
    if unassigned_node is None:
        return True  # Todas las asignaciones se han realizado con éxito

    conflict_node = None
    for node in graph:
        if node not in assignment:
            for color in colors:
                if is_valid_assignment(graph, node, color, assignment):
                    assignment[node] = color
                    if conflict_count(graph, node, color, assignment) == 0:
                        if backjump(graph, colors, assignment):
                            return True
                    else:
                        conflict_node = node
                    assignment[node] = None

    if conflict_node is not None:
        del assignment[conflict_node]
        return backjump(graph, colors, assignment)

    return False

def solve_graph_coloring(graph, colors):
    assignment = {}  # Debes declarar la variable assignment aquí
    if backjump(graph, colors, assignment):
        print("Solución encontrada:")
        for node, color in assignment.items():
            print(f"Nodo {node} coloreado como {color}")
    else:
        print("No se encontró una solución válida.")

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

if solve_graph_coloring(graph, colors):
    print("Solución encontrada:")
    for node, color in assignment.items():
        print(f"Nodo {node} coloreado como {color}")
else:
    print("No se encontró una solución válida.")
