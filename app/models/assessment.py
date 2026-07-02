from pydantic import BaseModel

class Assessment(BaseModel):
    id: str
    name: str
    url: str
    description: str

    job_levels: list[str]
    languages: list[str]

    duration: str

    remote: bool
    adaptive: bool

    categories: list[str]

    searchable_text: str