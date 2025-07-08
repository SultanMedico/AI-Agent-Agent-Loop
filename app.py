class Agent:
    def __init__(self):
        self.state = "start"
        self.goal = "goal"
    
    def perceive(self):
        print(f"[Perceiving] Current State: {self.state}")
        return self.state

    def decide(self, state):
        print(f"[Deciding] Based on state: {state}")
        if state == "start":
            return "move_forward"
        elif state == "near_goal":
            return "move_to_goal"
        else:
            return "idle"

    def act(self, action):
        print(f"[Acting] Performing action: {action}")
        if action == "move_forward":
            self.state = "near_goal"
        elif action == "move_to_goal":
            self.state = "goal"
        elif action == "idle":
            pass

    def has_reached_goal(self):
        return self.state == self.goal

    def run(self):
        while not self.has_reached_goal():
            state = self.perceive()
            action = self.decide(state)
            self.act(action)
        print("[Success] Goal reached!")


if __name__ == "__main__":
    agent = Agent()
    agent.run()
