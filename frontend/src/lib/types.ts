export interface Scenario {
  title: string;
  description: string;
  probability: number;
  implications: string;
}

export interface Event {
  id: string;
  title: string;
  category: "politics" | "tech" | "economy";
  summary: string;
  actors: string[];
  scenarios: Scenario[];
  date: string;
  region: string;
}
