import type { Event } from "./types";

const API_BASE = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";

export async function getEvents(category?: string): Promise<Event[]> {
  const url = new URL(`${API_BASE}/api/events`);
  if (category) url.searchParams.set("category", category);
  const res = await fetch(url.toString(), { next: { revalidate: 60 } });
  if (!res.ok) throw new Error("Failed to fetch events");
  return res.json();
}

export async function getEvent(id: string): Promise<Event> {
  const res = await fetch(`${API_BASE}/api/events/${id}`, {
    next: { revalidate: 60 },
  });
  if (!res.ok) throw new Error("Event not found");
  return res.json();
}
