import EventCard from "@/components/EventCard";
import { getEvents } from "@/lib/api";

export const dynamic = "force-dynamic";

export default async function HomePage() {
  const events = await getEvents();

  return (
    <div>
      <div className="mb-8">
        <h1 className="text-2xl font-bold">Global Event Feed</h1>
        <p className="mt-1 text-sm text-gray-500">
          Forward-looking scenario analysis for events shaping the world.
        </p>
      </div>
      <div className="grid gap-4">
        {events.map((event) => (
          <EventCard key={event.id} event={event} />
        ))}
      </div>
    </div>
  );
}
