def perform_action(current_state, action):
    print(f"[Acting] Performing action: {action}")
    if action == "move_forward":
        return "near_goal"
    elif action == "move_to_goal":
        return "goal"
    elif action == "idle":
        return current_state
    return current_state
