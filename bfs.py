def bfs(graph, start_node):
    # Keep track of visited nodes to avoid processing twice
    visited = []
    
    # Use a standard list as a queue
    queue = []
    
    # Mark the start node as visited and add it to the queue
    visited.append(start_node)
    queue.append(start_node)
    
    # Loop until there are nodes left to check
    while queue:
        # Remove the first node from the queue (FIFO)
        current_node = queue.pop(0)
        print(current_node, end=" ")
        
        # Get all neighboring nodes
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

# Example graph represented as an adjacency list (dictionary)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("Following is the Breadth-First Traversal:")
bfs(graph, 'A')
