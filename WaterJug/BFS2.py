from collections import deque        
  # Import deque (double-ended queue) from Python's collections library.
  # Deque is useful for BFS because we can pop elements from the left side efficiently.

def bfs_jugs(capA, capB, target):      # Define a function to solve the water jug problem using BFS.
    start = (0, 0)                     # Initial state: both jugs are empty (Jug A = 0, Jug B = 0).
    visited = {start}                  # A set that keeps track of all visited states to avoid repetition.
    parent = {start: (None, None)}     # Dictionary to remember how we reached each state:
                                       # Key = state, Value = (previous_state, action_taken)
    q = deque([start])                 # BFS queue initialized with the start state.

    while q:                           # While there are still states to explore in the queue...
        s = q.popleft()                # Take the first state from the queue (FIFO → BFS order).
        x, y = s                       # Unpack: x = amount in Jug A, y = amount in Jug B.

        if x == target or y == target: # Check if we’ve reached the goal condition (one jug has target water).
            path = []                  # List to reconstruct the sequence of steps.
            cur = s                    # Start backtracking from the goal state.

            while parent[cur][0] is not None:  # While current state is not the initial state...
                prev, action = parent[cur]     # Look up how we reached `cur`: (previous state, action taken).
                path.append((action, cur))     # Add this step (action + resulting state) into the path.
                cur = prev                     # Move backwards to the previous state.

            path.reverse()              # Reverse the list since we built it backwards.
            path.append(("Goal", s))    # Mark the last state as the "Goal".
            return path                 # Return the complete path of solution.

        # Generate all possible next moves from the current state `s`:
        moves = []                       # This will store the new states and actions.

        moves.append(((capA, y), "Fill A"))   # Action: Fill Jug A to its full capacity.
        moves.append(((x, capB), "Fill B"))   # Action: Fill Jug B to its full capacity.
        moves.append(((0, y), "Empty A"))     # Action: Empty Jug A completely.
        moves.append(((x, 0), "Empty B"))     # Action: Empty Jug B completely.

        pour = min(x, capB - y)               # Calculate how much water can be poured from A to B.
        if pour > 0:                          # Only valid if there is water in A and space in B.
            moves.append(((x - pour, y + pour), "Pour A→B"))

        pour = min(y, capA - x)               # Calculate how much water can be poured from B to A.
        if pour > 0:                          # Only valid if there is water in B and space in A.
            moves.append(((x + pour, y - pour), "Pour B→A"))

        # For every possible next state, check if it's already visited.
        for ns, action in moves:
            if ns not in visited:             # If state hasn't been seen before...
                visited.add(ns)               # Mark it as visited.
                parent[ns] = (s, action)      # Store how we reached this new state.
                q.append(ns)                  # Add new state to the BFS queue.

    return None   # If BFS finishes without finding the target, return None (no solution exists).


# Example run for the classic case:
if __name__ == "__main__":                     # Standard Python main entry point.
    solution = bfs_jugs(5, 3, 4)               # Call BFS function with Jug A = 5L, Jug B = 3L, target = 4L.
    if solution:                               # If a solution is found...
        print("Start -> (0, 0)")               # Print the starting state.
        for i, (act, state) in enumerate(solution, 1):  # Loop through the solution steps.
            if act == "Goal":                  # If this is the goal step...
                print(f"{i}. Reached {state}") # Print as "Reached (x, y)".
            else:
                print(f"{i}. {act} -> {state}")# Print the action and resulting state.
    else:
        print("No solution found")             # If BFS failed, print no solution.
