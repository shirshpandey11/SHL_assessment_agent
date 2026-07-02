from app.agent.parser import parse_conversation
from app.agent.decision import DecisionEngine

messages = [
    {
        "role": "user",
        "content": "Hiring a Java developer"
    }
]

state = parse_conversation(messages)

decision = DecisionEngine().decide(state)

print(state)
print()
print("Decision:", decision)