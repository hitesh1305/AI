def get_user_input(prompt):
    while True:
        print(prompt)
        user_input = input("-> ")
        try:
            numbers = [int(n) for n in user_input.split()]
            if len(numbers) != 9:
                print("\nError: Please enter exactly 9 numbers.\n")
                continue
            if set(numbers) != set(range(9)):
                print("\nError: Please use each number from 0 to 8 exactly once.\n")
                continue
            
            state = tuple(tuple(numbers[i*3 : i*3+3]) for i in range(3))
            return state
        except ValueError:
            print("\nError: Please enter valid numbers separated by spaces.\n")

def find_blank(state):
    for r in range(3):
        for c in range(3):
            if state[r][c] == 0:
                return r, c

def calculate_manhattan_distance(state, goal_state):
    distance = 0
    goal_positions = {goal_state[r][c]: (r, c) for r in range(3) for c in range(3)}

    for r in range(3):
        for c in range(3):
            tile = state[r][c]
            if tile != 0:
                goal_r, goal_c = goal_positions[tile]
                distance += abs(r - goal_r) + abs(c - goal_c)
    return distance

def get_neighbors(state):
    neighbors = []
    r, c = find_blank(state)
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for dr, dc in moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            new_state_list = [list(row) for row in state]
            new_state_list[r][c], new_state_list[nr][nc] = new_state_list[nr][nc], new_state_list[r][c]
            neighbors.append(tuple(tuple(row) for row in new_state_list))
    return neighbors

def reconstruct_path(node):
    path = []
    while node:
        path.append(node['state'])
        node = node['parent']
    return path[::-1]

def solve_puzzle(start_state, goal_state):
    open_list = []
    closed_set = set()

    start_h = calculate_manhattan_distance(start_state, goal_state)
    start_node = {
        'state': start_state,
        'parent': None,
        'g': 0,
        'h': start_h,
        'f': start_h
    }
    open_list.append(start_node)

    while open_list:
        current_node = min(open_list, key=lambda node: node['f'])
        
        open_list.remove(current_node)
        closed_set.add(current_node['state'])

        if current_node['state'] == goal_state:
            return reconstruct_path(current_node)

        for neighbor_state in get_neighbors(current_node['state']):
            if neighbor_state in closed_set:
                continue

            g_cost = current_node['g'] + 1
            h_cost = calculate_manhattan_distance(neighbor_state, goal_state)
            
            existing_node = next((node for node in open_list if node['state'] == neighbor_state), None)

            if existing_node and g_cost >= existing_node['g']:
                continue
            
            neighbor_node = {
                'state': neighbor_state,
                'parent': current_node,
                'g': g_cost,
                'h': h_cost,
                'f': g_cost + h_cost
            }
            
            if existing_node:
                open_list.remove(existing_node)
            open_list.append(neighbor_node)
            
    return None

def print_puzzle(state):
    if not state: return
    for row in state:
        print(" ".join(map(str, row)).replace('0', '_'))
    print("-" * 7)

# --- Main Execution ---
initial_prompt = "Enter the initial state of the 8-puzzle (e.g., 1 8 2 0 4 3 7 6 5):"
start_state = get_user_input(initial_prompt)

goal_prompt = "Enter the goal state of the 8-puzzle (e.g., 1 2 3 4 5 6 7 8 0):"
goal_state = get_user_input(goal_prompt)

print("\nSolving...")
path = solve_puzzle(start_state, goal_state)

if path:
    print("\nSolution found!")
    for i, state in enumerate(path):
        print(f"Step {i}:")
        print_puzzle(state)
else:
    print("\nNo solution found.")