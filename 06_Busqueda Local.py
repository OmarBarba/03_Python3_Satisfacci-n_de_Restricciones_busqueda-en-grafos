import random

def is_valid_assignment(graph, node, color, assignment):
    for neighbor in graph[node]:
        if neighbor in assignment and assignment.get(neighbor) == color:
            return False
    return True


def select_variable_with_conflicts(graph, assignment):
    max_conflicts = 0
    variables_with_conflicts = []
    
    for node in graph:
        if node in assignment:
            continue

        conflicts = 0
        for neighbor in graph[node]:
            if neighbor in assignment and assignment[neighbor] == assignment[node]:
                conflicts += 1

        if conflicts > max_conflicts:
            max_conflicts = conflicts
            variables_with_conflicts = [node]
        elif conflicts == max_conflicts:
            variables_with_conflicts.append(node)

    return random.choice(variables_with_conflicts)

def min_conflicts(graph, colors, max_steps):
    assignment = {}
    
    for _ in range(max_steps):
        if len(assignment) == len(graph):
            return assignment  # Se encontró una solución válida

        node = select_variable_with_conflicts(graph, assignment)
        color_options = [color for color in colors if is_valid_assignment(graph, node, color, assignment)]

        if color_options:
            assignment[node] = random.choice(color_options)
        else:
            return None  # No se encontró una solución válida

    return None  # Límite de pasos alcanzado sin encontrar una solución válida

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
max_steps = 1000

solution = min_conflicts(graph, colors, max_steps)

if solution:
    print("Solución encontrada:")
    for node, color in solution.items():
        print(f"Nodo {node} coloreado como {color}")
else:
    print("No se encontró una solución válida dentro del límite de pasos.")
