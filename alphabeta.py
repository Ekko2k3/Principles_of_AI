# Define MAX and MIN values for alpha-beta pruning
MAX, MIN = 1000, -1000

# Minimax function with alpha-beta pruning
def minmax(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    # Base case: if depth is 3, return the value of the node
    if depth == 3:
        return values[nodeIndex]
    
    # If maximizing player
    if maximizingPlayer:
        best = MIN  # Initialize best value for maximizing player
        # Explore all possible moves for maximizing player
        for i in range(0, 2):
            val = minmax(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)  # Recur for child nodes
            best = max(best, val)  # Update best value
            alpha = max(alpha, best)  # Update alpha value
            if beta <= alpha:
                break  # Beta cut-off
        return best
    
    # If minimizing player
    else:
        best = MAX  # Initialize best value for minimizing player
        # Explore all possible moves for minimizing player
        for i in range(0, 2):
            val = minmax(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)  # Recur for child nodes
            best = min(best, val)  # Update best value
            beta = min(beta, best)  # Update beta value
            if beta <= alpha:
                break  # Alpha cut-off
        return best

if __name__ == "__main__":
    # Input values for the nodes
    values = [10, 9, 14, 4, 5, 18, 50, 22, 13, 14]
    # Print the output of the minimax function with alpha-beta pruning
    print(f"Output:", minmax(0, 0, True, values, MIN, MAX))
