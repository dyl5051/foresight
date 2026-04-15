import Link from "next/link";
import type { Event } from "@/lib/types";
import CategoryBadge from "./CategoryBadge";
import CountdownTimer from "./CountdownTimer";

export default function HeroEvent({ event }: { event: Event }) {
  return (
    <Link
      href={`/events/${event.id}`}
      className="group block rounded-2xl border border-gray-200 bg-white shadow-sm hover:shadow-lg transition-shadow overflow-hidden"
    >
      {/* accent bar */}
      <div className="h-1 bg-gradient-to-r from-red-500 via-amber-500 to-red-500" />

      <div className="p-6">
        {event.deadline && event.deadline_label && (
          <div className="mb-4">
            <CountdownTimer
              deadline={event.deadline}
              label={event.deadline_label}
            />
          </div>
        )}

        <div className="mb-2 flex items-center gap-2">
          <CategoryBadge category={event.category} />
          <span className="text-xs text-gray-400">{event.region}</span>
          <span className="text-xs font-medium text-red-500">LIVE</span>
          <span className="ml-auto text-xs text-gray-400">{event.date}</span>
        </div>

        <h2 className="mb-2 text-xl font-bold text-gray-900 group-hover:text-indigo-600 transition-colors leading-tight">
          {event.title}
        </h2>

        <p className="mb-4 text-sm leading-relaxed text-gray-600 line-clamp-3">
          {event.summary}
        </p>

        <div className="flex flex-wrap gap-1.5 mb-3">
          {event.actors.slice(0, 5).map((actor) => (
            <span
              key={actor}
              className="rounded bg-gray-100 px-2 py-0.5 text-xs text-gray-500"
            >
              {actor}
            </span>
          ))}
          {event.actors.length > 5 && (
            <span className="rounded bg-gray-100 px-2 py-0.5 text-xs text-gray-400">
              +{event.actors.length - 5} more
            </span>
          )}
        </div>

        {/* mini scenario bar */}
        <div className="flex h-2 overflow-hidden rounded-full bg-gray-100">
          {[...event.scenarios]
            .sort((a, b) => b.probability - a.probability)
            .map((s, i) => {
              const colors = [
                "bg-indigo-500",
                "bg-amber-500",
                "bg-emerald-500",
                "bg-rose-500",
                "bg-sky-500",
              ];
              return (
                <div
                  key={s.title}
                  className={colors[i]}
                  style={{ width: `${s.probability * 100}%` }}
                />
              );
            })}
        </div>
        <p className="mt-1.5 text-xs text-gray-400">
          {event.scenarios.length} scenarios analyzed — tap to explore
        </p>
      </div>
    </Link>
  );
}
