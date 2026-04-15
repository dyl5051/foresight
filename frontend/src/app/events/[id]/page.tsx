import { notFound } from "next/navigation";
import Link from "next/link";
import { getEvent } from "@/lib/api";
import ActorCardCollapsible from "@/components/ActorCardCollapsible";
import CategoryBadge from "@/components/CategoryBadge";
import CountdownTimer from "@/components/CountdownTimer";
import ScenarioBreakdown from "@/components/ScenarioBreakdown";
import Timeline from "@/components/Timeline";

export default async function EventPage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = await params;
  let event;
  try {
    event = await getEvent(id);
  } catch {
    notFound();
  }

  const hasProfiles =
    event.actor_profiles && event.actor_profiles.length > 0;
  const hasTimeline = event.timeline && event.timeline.length > 0;

  return (
    <div>
      <Link
        href="/"
        className="mb-6 inline-block text-sm text-gray-500 hover:text-gray-900 transition-colors"
      >
        &larr; Back to feed
      </Link>

      {/* deadline countdown */}
      {event.deadline && event.deadline_label && (
        <div className="mb-5">
          <CountdownTimer
            deadline={event.deadline}
            label={event.deadline_label}
          />
        </div>
      )}

      <div className="mb-2 flex items-center gap-2">
        <CategoryBadge category={event.category} />
        <span className="text-xs text-gray-400">{event.region}</span>
        {event.featured && (
          <span className="text-xs font-medium text-red-500">LIVE</span>
        )}
        <span className="ml-auto text-xs text-gray-400">{event.date}</span>
      </div>

      <h1 className="mb-3 text-2xl font-extrabold tracking-tight leading-tight">
        {event.title}
      </h1>

      <p className="mb-6 text-sm leading-relaxed text-gray-600">
        {event.summary}
      </p>

      {!hasProfiles && (
        <div className="mb-6 flex flex-wrap gap-1.5">
          {event.actors.map((actor) => (
            <span
              key={actor}
              className="rounded bg-gray-100 px-2 py-0.5 text-xs text-gray-500"
            >
              {actor}
            </span>
          ))}
        </div>
      )}

      {/* timeline */}
      {hasTimeline && (
        <section className="mb-8">
          <h2 className="mb-4 text-lg font-bold tracking-tight">
            Timeline of Events
          </h2>
          <Timeline entries={event.timeline!} />
        </section>
      )}

      {/* scenarios */}
      <section className="mb-8">
        <h2 className="mb-4 text-lg font-bold tracking-tight">
          Possible Scenarios
        </h2>
        <ScenarioBreakdown scenarios={event.scenarios} />
      </section>

      {/* actor profiles */}
      {hasProfiles && (
        <section>
          <h2 className="mb-2 text-lg font-bold tracking-tight">
            Key Actors &amp; Analysis
          </h2>
          <p className="mb-4 text-xs text-gray-400">
            Tap each actor to reveal their public position, what they may
            actually accept, and key incentives.
          </p>
          <div className="grid gap-3 sm:grid-cols-2">
            {event.actor_profiles!.map((actor) => (
              <ActorCardCollapsible key={actor.name} actor={actor} />
            ))}
          </div>
        </section>
      )}
    </div>
  );
}
