from app.agent.parser import parse_conversation
from app.agent.decision import DecisionEngine
from app.agent.query_builder import build_query
from app.agent.comparison import compare_assessments

from app.models.schemas import ChatResponse, Recommendation

from app.retrieval.hybrid import HybridRetriever

from app.services.llm import generate_reply


class SHLAgent:

    def __init__(self):
        self.decision_engine = DecisionEngine()
        self.retriever = HybridRetriever()

    def chat(self, messages):

        history = [
            message.model_dump()
            for message in messages
        ]

        state = parse_conversation(history)

        decision = self.decision_engine.decide(state)

        # ---------------- Clarify Role ----------------

        if decision == "clarify_role":

            return ChatResponse(
                reply="What role are you hiring for?",
                recommendations=[],
                end_of_conversation=False,
            )

        # ---------------- Clarify Seniority ----------------

        if decision == "clarify_seniority":

            return ChatResponse(
                reply="What seniority level or years of experience are you looking for?",
                recommendations=[],
                end_of_conversation=False,
            )

        # ---------------- Refuse ----------------

        if decision == "refuse":

            return ChatResponse(
                reply=(
                    "I can only recommend and compare SHL assessments. "
                    "Please ask about assessment selection or comparison."
                ),
                recommendations=[],
                end_of_conversation=False,
            )

        # ---------------- Compare ----------------

        if decision == "compare":

            return ChatResponse(
                reply=compare_assessments(
                    state.compare_request
                ),
                recommendations=[],
                end_of_conversation=False,
            )

        # ---------------- Recommendation ----------------

        query = build_query(state)

        print("=" * 70)
        print("SEARCH QUERY")
        print(query)
        print("=" * 70)

        results = self.retriever.search(
            query,
            top_k=7,
        )

        recommendations = []

        for item in results:

            recommendations.append(

                Recommendation(
                    name=item.name,
                    url=item.url,
                    test_type=", ".join(item.categories),
                )

            )

        reply = generate_reply(
            query,
            [item.name for item in recommendations]
        )

        return ChatResponse(
            reply=reply,
            recommendations=recommendations,
            end_of_conversation=True,
        )