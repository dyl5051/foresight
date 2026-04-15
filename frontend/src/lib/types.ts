export interface Scenario {
  title: string;
  description: string;
  probability: number;
  implications: string;
}

export interface ActorProfile {
  name: string;
  role: string;
  public_position: string;
  likely_accepts: string;
  incentives: string[];
}

export interface TimelineEntry {
  date: string;
  label: string;
  description: string;
}

export interface Event {
  id: string;
  title: string;
  category: "politics" | "tech" | "economy";
  summary: string;
  actors: string[];
  actor_profiles: ActorProfile[] | null;
  timeline: TimelineEntry[] | null;
  deadline: string | null;
  deadline_label: string | null;
  featured: boolean;
  scenarios: Scenario[];
  date: string;
  region: string;
}
