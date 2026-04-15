import EventCard from "@/components/EventCard";
import HeroEvent from "@/components/HeroEvent";
import { getEvents } from "@/lib/api";

export const dynamic = "force-dynamic";

export default async function HomePage() {
  const events = await getEvents();
  const featured = events.find((e) => e.featured);
  const rest = events.filter((e) => !e.featured);

  return (
    <div>
      <div className="mb-8">
        <h1 className="text-3xl font-extrabold tracking-tight">
          Global Event Feed
        </h1>
        <p className="mt-1 text-sm text-gray-500">
          Forward-looking scenario analysis for events shaping the world.
        </p>
      </div>

      {featured && (
        <div className="mb-8">
          <HeroEvent event={featured} />
        </div>
      )}

      <div className="grid gap-4">
        {rest.map((event) => (
          <EventCard key={event.id} event={event} />
        ))}
      </div>
    </div>
  );
}
