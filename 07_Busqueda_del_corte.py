def find_augmenting_path(graph, source, sink, path):
    visited = set()
    stack = [source]
    
    while stack:
        current_node = stack.pop()
        visited.add(current_node)
        
        if current_node == sink:
            return path
        
        for neighbor, capacity in graph[current_node].items():
            if neighbor not in visited and capacity > 0:
                path[neighbor] = current_node
                stack.append(neighbor)
    
    return None

def cut_conditioning(graph, source, sink):
    max_flow = 0
    path = find_augmenting_path(graph, source, sink, {})
    
    while path:
        min_capacity = min(graph[path[node]][node] for node in path)
        max_flow += min_capacity
        
        for node, parent in path.items():
            graph[parent][node] -= min_capacity
            if node not in graph:
                graph[node] = {}
            if parent not in graph[node]:
                graph[node][parent] = 0
            graph[node][parent] += min_capacity
        
        path = find_augmenting_path(graph, source, sink, {})

    return max_flow

# Ejemplo de uso:
graph = {
    'A': {'B': 10, 'C': 10},
    'B': {'C': 2, 'D': 4},
    'C': {'D': 8},
    'D': {'E': 10},
    'E': {}
}

source_node = 'A'
sink_node = 'E'
max_flow = cut_conditioning(graph, source_node, sink_node)
print(f"Flujo máximo: {max_flow}")
