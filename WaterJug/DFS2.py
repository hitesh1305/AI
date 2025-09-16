def dfs_jugs(capA, capB, target):       # Define a function that solves the water jug problem using DFS.
                                                                  # This function takes three inputs:
                                                                       # capA → capacity of Jug A
                                                                                   # capB → capacity of Jug B
                                             # target → the desired amount of water we want in either Jug A or Jug B.

    start = (0, 0)                      # Initial state: both jugs are empty → Jug A = 0, Jug B = 0.
    # We represent states as tuples (x, y), where x = amount in Jug A, y = amount in Jug B.
    # Initially, both are empty: (0,0).

    visited = set()                     # A set to remember which states have been visited (to avoid loops).
    # Example: If we already reached (2,3), we don’t want to repeat it again
    # otherwise DFS could loop infinitely between states.

    def dfs(state, path):               # Define an inner recursive function for DFS exploration.
        # state = current jug amounts (x, y)
        # path = list of actions taken so far to reach this state.

        x, y = state                    # Unpack the current state into x = Jug A, y = Jug B.
        # Example: if state = (2,3), then x=2 liters in Jug A, y=3 liters in Jug B.

        if state in visited:            # If this state was already visited earlier...
            return None                 # ...stop exploring this branch (avoids infinite recursion).
        # This prevents revisiting the same configuration and wasting time.

        visited.add(state)              # Mark the current state as visited.
        # Example: once we enter (2,3), it’s added to visited = {(2,3)}.

        if x == target or y == target:                       # Goal test: If either jug contains the target amount...
            return path + [("Goal", state)]  
        # If goal found → return the path of actions plus a final "Goal" marker.

        # All possible next moves from the current state:
        moves = [
            ((capA, y), "Fill A"),             # Fill Jug A completely → new state: (capA, y).
            ((x, capB), "Fill B"),                       # Fill Jug B completely → new state: (x, capB).
            ((0, y), "Empty A"),                            # Empty Jug A → new state: (0, y).
            ((x, 0), "Empty B"),                         # Empty Jug B → new state: (x, 0).
            ((x - min(x, capB - y), y + min(x, capB - y)), "Pour A->B"), 
                                                                 # Pour from A into B until either A is empty or B is full.
                                                                      # min(x, capB - y) ensures we don’t pour more than possible.
            
            ((x + min(y, capA - x), y - min(y, capA - x)), "Pour B->A"),
                                                                                  # Pour from B into A until either B is empty or A is full.
                                                                             # min(y, capA - x) ensures the right amount is transferred.
        ]

        for ns, act in moves:            # For every possible next state (ns) with its action name (act)...
            res = dfs(ns, path + [(act, ns)])  
            # Recursive DFS call on next state, adding this action into the path.
            if res:                      # If recursion found a solution...
                return res               # ...return that solution upwards (end recursion).
        # DFS explores deeply until it finds a solution or exhausts moves.

        return None                      # If no move leads to a solution, return None for this branch.

    return dfs(start, [])                # Start DFS search from the initial state with an empty path.
    # Start from (0,0) and an empty path → dfs((0,0), [])
