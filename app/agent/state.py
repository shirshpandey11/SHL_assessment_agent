from dataclasses import dataclass, field


@dataclass
class ConversationState:

    role: str | None = None

    seniority: str | None = None

    industry: str | None = None

    assessment_types: list[str] = field(default_factory=list)

    needs_clarification: bool = True

    compare_request: list[str] = field(default_factory=list)

    refinement: bool = False

    finished: bool = False