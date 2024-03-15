def astaralgo(start_node, stop_node):
    # Initialize the open set with the start node
    open_set = {start_node}
    closed_set = set()  # Initialize the closed set
    g = {start_node: 0}  # Initialize the cost from start to each node
    parents = {start_node: start_node}  # Initialize the parent nodes
    
    def heuristic(n):
        # Heuristic function to estimate the cost from node n to the goal node
        H_dist = {
            'A': 11,
            'B': 12,
            'C': 20,
            'D': 77,
            'E': 3,
            'G': 0
        }
        return H_dist[n]
    
    while open_set:
        # Choose the node in the open set with the lowest f value
        n = min(open_set, key=lambda x: g[x] + heuristic(x))
        
        # Check if the goal node is reached or if the node is not present in the graph
        if n == stop_node or Graph_nodes.get(n) is None:
            pass
        else:
            # Expand the current node and update its neighbors
            for m, weight in Graph_nodes.get(n, []):
                # If m is not in the open set or closed set, add it to the open set
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    # If a shorter path to m is found, update its cost and parent
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n
                        # If m was previously in the closed set, move it back to the open set
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)
        
        # If the goal node is not reachable, print a message and return None
        if not n:
            print("Path does not exist")
            return None
        
        # If the goal node is reached, reconstruct and return the optimal path
        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()  # Reverse the path to get it from start to stop node
            return g[stop_node], path
        
        # Remove the current node from the open set and add it to the closed set
        open_set.remove(n)
        closed_set.add(n)
    
    # If the open set becomes empty without reaching the goal node, print a message and return None
    print("Path does not exist")
    return None

# Define the graph nodes and their connections
Graph_nodes = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'C': None,
    'D': [('D', 6)],
    'E': [('G', 1)]
}

# Run A* algorithm to find the optimal path from start to stop node
optimal_value_path = astaralgo('A', 'G')

# If an optimal path is found, print the optimal value and the path
if optimal_value_path is not None:
    optimal_value, path = optimal_value_path
    print('Optimal value:', optimal_value)
    print('Path:', path)
