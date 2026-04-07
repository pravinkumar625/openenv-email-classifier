from fastapi import FastAPI
from environment import EmailEnv

app = FastAPI()
env = EmailEnv()

@app.get("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(action: str):
    return env.step(action)

@app.get("/state")
def state():
    return env.state()