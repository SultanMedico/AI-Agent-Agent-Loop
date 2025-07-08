from agent.decisions import decide_action
from agent.actions import perform_action

class Agent:
    def __init__(self):
        self.state = "start"
        self.goal = "goal"
    
    def perceive(self):
        print(f"[Perceiving] Current State: {self.state}")
        return self.state

    def decide(self, state):
        return decide_action(state)

    def act(self, action):
        self.state = perform_action(self.state, action)

    def has_reached_goal(self):
        return self.state == self.goal

    def run(self):
        while not self.has_reached_goal():
            state = self.perceive()
            action = self.decide(state)
            self.act(action)
        print("[Success] Goal reached!")
