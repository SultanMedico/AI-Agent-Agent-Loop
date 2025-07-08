def decide_action(state):
    print(f"[Deciding] Based on state: {state}")
    if state == "start":
        return "move_forward"
    elif state == "near_goal":
        return "move_to_goal"
    else:
        return "idle"
