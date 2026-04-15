"use client";

import { useState } from "react";
import type { ActorProfile } from "@/lib/types";

export default function ActorCardCollapsible({
  actor,
}: {
  actor: ActorProfile;
}) {
  const [open, setOpen] = useState(false);

  return (
    <div className="rounded-lg border border-gray-200 bg-white overflow-hidden">
      <button
        onClick={() => setOpen(!open)}
        className="w-full text-left px-5 py-4 flex items-center gap-3 hover:bg-gray-50 transition-colors"
      >
        <div className="flex-1 min-w-0">
          <h3 className="text-sm font-semibold text-gray-900">{actor.name}</h3>
          <p className="text-xs text-gray-400 truncate">{actor.role}</p>
        </div>
        <span className="text-xs text-amber-600 font-medium hidden sm:block">
          Tap to reveal analysis
        </span>
        <svg
          className={`h-4 w-4 shrink-0 text-gray-400 transition-transform ${open ? "rotate-180" : ""}`}
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
          strokeWidth={2}
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            d="M19 9l-7 7-7-7"
          />
        </svg>
      </button>

      {open && (
        <div className="border-t border-gray-100 px-5 py-4 space-y-3">
          <Section
            label="Public Position"
            color="text-gray-500"
            bg="bg-gray-50"
          >
            {actor.public_position}
          </Section>

          <Section
            label="What They May Actually Accept"
            color="text-amber-700"
            bg="bg-amber-50"
          >
            {actor.likely_accepts}
          </Section>

          <div>
            <p className="mb-1.5 text-xs font-semibold uppercase tracking-wide text-gray-400">
              Key Incentives
            </p>
            <ul className="space-y-1">
              {actor.incentives.map((incentive, i) => (
                <li key={i} className="flex gap-2 text-sm text-gray-600">
                  <span className="mt-1.5 h-1.5 w-1.5 shrink-0 rounded-full bg-gray-300" />
                  {incentive}
                </li>
              ))}
            </ul>
          </div>
        </div>
      )}
    </div>
  );
}

function Section({
  label,
  color,
  bg,
  children,
}: {
  label: string;
  color: string;
  bg: string;
  children: React.ReactNode;
}) {
  return (
    <div className={`rounded-md px-3 py-2.5 ${bg}`}>
      <p className={`mb-1 text-xs font-semibold uppercase tracking-wide ${color}`}>
        {label}
      </p>
      <p className="text-sm leading-relaxed text-gray-700">{children}</p>
    </div>
  );
}
