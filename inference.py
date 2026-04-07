import requests
import os

BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")

print("[START]")

res = requests.get(f"{BASE_URL}/reset").json()
email = res["email"]

print(f"[STEP] Email: {email}")

# Simple rule-based model
if "free" in email.lower() or "win" in email.lower():
    action = "spam"
else:
    action = "not_spam"

step_res = requests.post(f"{BASE_URL}/step", params={"action": action}).json()

print(f"[STEP] Action: {action}, Reward: {step_res['reward']}")

print("[END]")