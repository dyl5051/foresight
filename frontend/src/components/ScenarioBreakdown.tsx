import type { Scenario } from "@/lib/types";

const COLORS = [
  "bg-indigo-500",
  "bg-amber-500",
  "bg-emerald-500",
  "bg-rose-500",
  "bg-sky-500",
];

const COLORS_LIGHT = [
  "bg-indigo-100 text-indigo-700",
  "bg-amber-100 text-amber-700",
  "bg-emerald-100 text-emerald-700",
  "bg-rose-100 text-rose-700",
  "bg-sky-100 text-sky-700",
];

export default function ScenarioBreakdown({
  scenarios,
}: {
  scenarios: Scenario[];
}) {
  const sorted = [...scenarios].sort((a, b) => b.probability - a.probability);

  return (
    <div>
      {/* stacked bar */}
      <div className="mb-6 flex h-10 overflow-hidden rounded-lg">
        {sorted.map((s, i) => (
          <div
            key={s.title}
            className={`${COLORS[i]} flex items-center justify-center transition-all`}
            style={{ width: `${s.probability * 100}%` }}
            title={`${s.title}: ${Math.round(s.probability * 100)}%`}
          >
            {s.probability >= 0.15 && (
              <span className="text-xs font-bold text-white">
                {Math.round(s.probability * 100)}%
              </span>
            )}
          </div>
        ))}
      </div>

      {/* legend + details */}
      <div className="space-y-4">
        {sorted.map((s, i) => (
          <div key={s.title} className="rounded-lg border border-gray-200 bg-white p-4">
            <div className="flex items-start gap-3 mb-2">
              <span
                className={`mt-0.5 inline-flex shrink-0 items-center rounded-full px-2.5 py-0.5 text-xs font-bold ${COLORS_LIGHT[i]}`}
              >
                {Math.round(s.probability * 100)}%
              </span>
              <h3 className="text-sm font-semibold text-gray-900">
                {s.title}
              </h3>
            </div>
            <p className="text-sm leading-relaxed text-gray-600 mb-2">
              {s.description}
            </p>
            <div className="rounded bg-gray-50 px-3 py-2">
              <p className="text-xs font-semibold uppercase tracking-wide text-gray-400 mb-0.5">
                Implications
              </p>
              <p className="text-sm text-gray-600">{s.implications}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
