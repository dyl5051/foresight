from pydantic import BaseModel


class Scenario(BaseModel):
    title: str
    description: str
    probability: float  # 0.0 – 1.0
    implications: str


class ActorProfile(BaseModel):
    name: str
    role: str
    public_position: str
    likely_accepts: str
    incentives: list[str]


class Event(BaseModel):
    id: str
    title: str
    category: str  # "politics" | "tech" | "economy"
    summary: str
    actors: list[str]
    actor_profiles: list[ActorProfile] | None = None
    scenarios: list[Scenario]
    date: str  # ISO date
    region: str
