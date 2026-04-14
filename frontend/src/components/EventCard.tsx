import Link from "next/link";
import type { Event } from "@/lib/types";
import CategoryBadge from "./CategoryBadge";

export default function EventCard({ event }: { event: Event }) {
  return (
    <Link
      href={`/events/${event.id}`}
      className="group block rounded-xl border border-gray-200 bg-white p-5 shadow-sm transition hover:shadow-md"
    >
      <div className="mb-2 flex items-center gap-2">
        <CategoryBadge category={event.category} />
        <span className="text-xs text-gray-400">{event.region}</span>
        <span className="ml-auto text-xs text-gray-400">{event.date}</span>
      </div>
      <h2 className="mb-1 text-lg font-semibold text-gray-900 group-hover:text-indigo-600 transition-colors">
        {event.title}
      </h2>
      <p className="mb-3 text-sm leading-relaxed text-gray-600 line-clamp-2">
        {event.summary}
      </p>
      <div className="flex flex-wrap gap-1.5">
        {event.actors.map((actor) => (
          <span
            key={actor}
            className="rounded bg-gray-100 px-2 py-0.5 text-xs text-gray-500"
          >
            {actor}
          </span>
        ))}
      </div>
      <p className="mt-3 text-xs text-gray-400">
        {event.scenarios.length} scenarios
      </p>
    </Link>
  );
}
