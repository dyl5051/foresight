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


class TimelineEntry(BaseModel):
    date: str  # ISO date
    label: str
    description: str


class Event(BaseModel):
    id: str
    title: str
    category: str  # "politics" | "tech" | "economy"
    summary: str
    actors: list[str]
    actor_profiles: list[ActorProfile] | None = None
    timeline: list[TimelineEntry] | None = None
    deadline: str | None = None  # ISO date — countdown target
    deadline_label: str | None = None
    featured: bool = False
    scenarios: list[Scenario]
    date: str  # ISO date
    region: str
