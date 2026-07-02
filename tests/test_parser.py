from app.agent.parser import parse_conversation

messages = [
    {
        "role": "user",
        "content": "Hiring a Java developer"
    },
    {
        "role": "assistant",
        "content": "What seniority?"
    },
    {
        "role": "user",
        "content": "Around 4 years experience"
    },
    {
        "role": "user",
        "content": "Also include personality assessments"
    }
]

state = parse_conversation(messages)

print(state)