import os

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .data import get_event_by_id, get_events
from .models import Event

app = FastAPI(title="Foresight API", version="0.1.0")

allowed_origins = [
    "http://localhost:3000",
]
if extra := os.environ.get("CORS_ORIGINS"):
    allowed_origins.extend(o.strip() for o in extra.split(",") if o.strip())

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/api/events", response_model=list[Event])
def list_events(category: str | None = None):
    events = get_events()
    if category:
        events = [e for e in events if e.category == category]
    return events


@app.get("/api/events/{event_id}", response_model=Event)
def read_event(event_id: str):
    event = get_event_by_id(event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event


@app.get("/api/health")
def health():
    return {"status": "ok"}
