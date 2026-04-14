export default function ProbabilityBar({
  probability,
}: {
  probability: number;
}) {
  const pct = Math.round(probability * 100);
  return (
    <div className="flex items-center gap-2">
      <div className="h-2 flex-1 overflow-hidden rounded-full bg-gray-200">
        <div
          className="h-full rounded-full bg-indigo-500 transition-all"
          style={{ width: `${pct}%` }}
        />
      </div>
      <span className="text-xs font-semibold tabular-nums text-gray-600">
        {pct}%
      </span>
    </div>
  );
}
