from app.agent.state import ConversationState


def build_query(state):

    query = []

    if state.role:
        query.append(state.role)

    if state.seniority:
        query.append(state.seniority)

    for assessment in state.assessment_types:
        query.append(assessment)

    return "\n".join(query)