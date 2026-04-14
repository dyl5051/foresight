from pydantic import BaseModel


class Scenario(BaseModel):
    title: str
    description: str
    probability: float  # 0.0 – 1.0
    implications: str


class Event(BaseModel):
    id: str
    title: str
    category: str  # "politics" | "tech" | "economy"
    summary: str
    actors: list[str]
    scenarios: list[Scenario]
    date: str  # ISO date
    region: str
