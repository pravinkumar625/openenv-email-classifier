import random

EMAILS = [
    ("Win a free iPhone now", "spam"),
    ("Meeting at 10 AM tomorrow", "not_spam"),
    ("Claim your lottery prize", "spam"),
    ("Project deadline extended", "not_spam"),
]

class EmailEnv:
    def __init__(self):
        self.state = None

    def reset(self):
        self.state = random.choice(EMAILS)
        return {"email": self.state[0]}

    def step(self, action):
        correct = self.state[1]
        reward = 1.0 if action == correct else 0.0
        done = True
        return {"reward": reward, "done": done}

    def state(self):
        return {"email": self.state[0]}