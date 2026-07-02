import re

from app.agent.state import ConversationState


SENIORITY_PATTERNS = {
    "Entry": ["entry", "entry-level", "graduate", "fresher", "junior"],
    "Mid": [
        "mid",
        "mid-level",
        "3 years",
        "4 years",
        "5 years",
        "3+",
        "4+",
        "5+",
    ],
    "Senior": [
        "senior",
        "lead",
        "architect",
        "principal",
        "8 years",
        "10 years",
        "8+",
        "10+",
    ],
}


def clean_role(text: str) -> str:
    text = re.sub(
        r"(?i)i'?m hiring|we are hiring|hiring|looking for|need|want|candidate|role",
        "",
        text,
    )

    return text.strip()


def parse_conversation(messages):

    state = ConversationState()

    for message in messages:

        if message["role"] != "user":
            continue

        text = message["content"]
        lower = text.lower()

        # ---------------- Compare ----------------

        if "compare" in lower or "difference" in lower:

            names = re.split(
                r"compare|difference between|and|vs|,",
                lower,
            )

            state.compare_request = [
                x.strip()
                for x in names
                if len(x.strip()) > 1
            ]

            continue

        # ---------------- Personality ----------------

        if "personality" in lower:

            if "Personality & Behavior" not in state.assessment_types:
                state.assessment_types.append(
                    "Personality & Behavior"
                )

            state.refinement = True

        # ---------------- Ability ----------------

        if "ability" in lower:

            if "Ability & Aptitude" not in state.assessment_types:
                state.assessment_types.append(
                    "Ability & Aptitude"
                )

            state.refinement = True

        # ---------------- Seniority ----------------

        for level, patterns in SENIORITY_PATTERNS.items():

            if any(pattern in lower for pattern in patterns):
                state.seniority = level

        # ---------------- Role ----------------

        if any(
            keyword in lower
            for keyword in [
                "developer",
                "engineer",
                "analyst",
                "scientist",
                "manager",
                "designer",
                "tester",
            ]
        ):

            state.role = clean_role(text)

    state.needs_clarification = (
        state.role is None
        or state.seniority is None
    )

    return state