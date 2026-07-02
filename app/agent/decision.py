from app.agent.state import ConversationState

OFF_TOPIC = [
    "salary",
    "politics",
    "weather",
    "restaurant",
    "movie",
    "cricket",
    "football",
    "visa",
    "immigration",
    "legal",
]


class DecisionEngine:

    def decide(self, state: ConversationState):

        role = (state.role or "").lower()

        if any(word in role for word in OFF_TOPIC):
            return "refuse"

        if state.compare_request:
            return "compare"

        if state.role is None:
            return "clarify_role"

        if state.seniority is None:
            return "clarify_seniority"

        return "recommend"