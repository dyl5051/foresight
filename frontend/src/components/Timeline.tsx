import type { TimelineEntry } from "@/lib/types";

export default function Timeline({ entries }: { entries: TimelineEntry[] }) {
  return (
    <div className="relative pl-4 border-l-2 border-gray-200 space-y-6">
      {entries.map((entry, i) => {
        const isToday = entry.label.includes("Today");
        const isFuture = new Date(entry.date) > new Date();
        return (
          <div key={i} className="relative">
            {/* dot */}
            <div
              className={`absolute -left-[calc(1rem+5px)] top-1 h-2.5 w-2.5 rounded-full border-2 ${
                isToday
                  ? "border-red-500 bg-red-500"
                  : isFuture
                    ? "border-amber-400 bg-amber-400"
                    : "border-gray-400 bg-white"
              }`}
            />
            <div className="flex items-baseline gap-2 mb-0.5">
              <span className="text-xs font-mono text-gray-400 tabular-nums">
                {entry.date.slice(5)}
              </span>
              <span
                className={`text-sm font-semibold ${
                  isToday
                    ? "text-red-600"
                    : isFuture
                      ? "text-amber-600"
                      : "text-gray-800"
                }`}
              >
                {entry.label}
              </span>
            </div>
            <p className="text-sm text-gray-500 leading-relaxed">
              {entry.description}
            </p>
          </div>
        );
      })}
    </div>
  );
}
