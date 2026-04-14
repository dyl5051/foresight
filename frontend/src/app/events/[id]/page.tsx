import { notFound } from "next/navigation";
import Link from "next/link";
import { getEvent } from "@/lib/api";
import CategoryBadge from "@/components/CategoryBadge";
import ScenarioCard from "@/components/ScenarioCard";

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

  return (
    <div>
      <Link
        href="/"
        className="mb-6 inline-block text-sm text-gray-500 hover:text-gray-900 transition-colors"
      >
        &larr; Back to feed
      </Link>

      <div className="mb-2 flex items-center gap-2">
        <CategoryBadge category={event.category} />
        <span className="text-xs text-gray-400">{event.region}</span>
        <span className="ml-auto text-xs text-gray-400">{event.date}</span>
      </div>

      <h1 className="mb-3 text-2xl font-bold">{event.title}</h1>

      <p className="mb-4 text-sm leading-relaxed text-gray-600">
        {event.summary}
      </p>

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

      <h2 className="mb-4 text-lg font-semibold">Possible Scenarios</h2>
      <div className="grid gap-4 sm:grid-cols-2">
        {event.scenarios.map((scenario) => (
          <ScenarioCard key={scenario.title} scenario={scenario} />
        ))}
      </div>
    </div>
  );
}
