def solve_water_jug_dfs(capacity1, capacity2, target):
    visited_states = set()
    stack = [ ([(0, 0)], (0, 0)) ]
    visited_states.add((0, 0))

    while stack:
        path, current_state = stack.pop()
        jug1, jug2 = current_state

        if jug1 == target or jug2 == target:
            return path

        possible_states = []
        possible_states.append((capacity1, jug2))
        possible_states.append((jug1, capacity2))
        possible_states.append((0, jug2))
        possible_states.append((jug1, 0))
        
        pour_to_2 = min(jug1, capacity2 - jug2)
        possible_states.append((jug1 - pour_to_2, jug2 + pour_to_2))
        
        pour_to_1 = min(jug2, capacity1 - jug1)
        possible_states.append((jug1 + pour_to_1, jug2 - pour_to_1))

        for next_state in possible_states:
            if next_state not in visited_states:
                visited_states.add(next_state)
                new_path = path + [next_state]
                stack.append((new_path, next_state))
    
    return None

try:
    cap1 = int(input("Enter capacity of Jug 1: "))
    cap2 = int(input("Enter capacity of Jug 2: "))
    target = int(input("Enter target amount: "))
    
    solution_path = solve_water_jug_dfs(cap1, cap2, target)

    if solution_path:
        print("\n--- DFS Solution Found! (Not guaranteed to be shortest) ---")
        for i, state in enumerate(solution_path):
            print(f"Step {i}: Jug1: {state[0]}L, Jug2: {state[1]}L")
    else:
        print("\nNo solution found.")

except ValueError:
    print("Invalid input. Please enter numbers only.")