import type { Scenario } from "@/lib/types";
import ProbabilityBar from "./ProbabilityBar";

export default function ScenarioCard({ scenario }: { scenario: Scenario }) {
  return (
    <div className="rounded-lg border border-gray-200 bg-white p-5">
      <h3 className="mb-1 text-base font-semibold text-gray-900">
        {scenario.title}
      </h3>
      <div className="mb-3">
        <ProbabilityBar probability={scenario.probability} />
      </div>
      <p className="mb-3 text-sm leading-relaxed text-gray-600">
        {scenario.description}
      </p>
      <div className="rounded-md bg-gray-50 px-3 py-2">
        <p className="text-xs font-medium uppercase tracking-wide text-gray-400 mb-1">
          Implications
        </p>
        <p className="text-sm text-gray-600">{scenario.implications}</p>
      </div>
    </div>
  );
}
