import type { ActorProfile } from "@/lib/types";

export default function ActorCard({ actor }: { actor: ActorProfile }) {
  return (
    <div className="rounded-lg border border-gray-200 bg-white p-5">
      <div className="mb-3">
        <h3 className="text-base font-semibold text-gray-900">{actor.name}</h3>
        <p className="text-xs text-gray-400">{actor.role}</p>
      </div>

      <div className="mb-3">
        <p className="mb-1 text-xs font-medium uppercase tracking-wide text-emerald-600">
          Public Position
        </p>
        <p className="text-sm leading-relaxed text-gray-600">
          {actor.public_position}
        </p>
      </div>

      <div className="mb-3 rounded-md bg-amber-50 px-3 py-2">
        <p className="mb-1 text-xs font-medium uppercase tracking-wide text-amber-700">
          What They May Actually Accept
        </p>
        <p className="text-sm leading-relaxed text-gray-700">
          {actor.likely_accepts}
        </p>
      </div>

      <div>
        <p className="mb-1.5 text-xs font-medium uppercase tracking-wide text-gray-400">
          Key Incentives
        </p>
        <ul className="space-y-1">
          {actor.incentives.map((incentive, i) => (
            <li key={i} className="flex gap-2 text-sm text-gray-600">
              <span className="mt-1.5 h-1 w-1 flex-shrink-0 rounded-full bg-gray-300" />
              {incentive}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}
