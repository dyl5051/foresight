"use client";

import { useEffect, useState } from "react";

function compute(target: string) {
  const diff = new Date(target + "T23:59:59Z").getTime() - Date.now();
  if (diff <= 0) return { days: 0, hours: 0, minutes: 0, expired: true };
  return {
    days: Math.floor(diff / 86_400_000),
    hours: Math.floor((diff % 86_400_000) / 3_600_000),
    minutes: Math.floor((diff % 3_600_000) / 60_000),
    expired: false,
  };
}

export default function CountdownTimer({
  deadline,
  label,
}: {
  deadline: string;
  label: string;
}) {
  const [time, setTime] = useState(compute(deadline));

  useEffect(() => {
    const id = setInterval(() => setTime(compute(deadline)), 60_000);
    return () => clearInterval(id);
  }, [deadline]);

  if (time.expired) {
    return (
      <div className="flex items-center gap-2 rounded-lg bg-red-600 px-4 py-2.5 text-white">
        <span className="relative flex h-2.5 w-2.5">
          <span className="absolute inline-flex h-full w-full animate-ping rounded-full bg-white opacity-75" />
          <span className="relative inline-flex h-2.5 w-2.5 rounded-full bg-white" />
        </span>
        <span className="text-sm font-semibold uppercase tracking-wide">
          {label} — Deadline passed
        </span>
      </div>
    );
  }

  return (
    <div className="flex items-center gap-3 rounded-lg bg-red-600 px-4 py-2.5 text-white">
      <span className="relative flex h-2.5 w-2.5">
        <span className="absolute inline-flex h-full w-full animate-ping rounded-full bg-white opacity-75" />
        <span className="relative inline-flex h-2.5 w-2.5 rounded-full bg-white" />
      </span>
      <span className="text-sm font-semibold uppercase tracking-wide">
        {label}
      </span>
      <div className="ml-auto flex gap-3 text-center">
        <Unit value={time.days} label="days" />
        <Unit value={time.hours} label="hrs" />
        <Unit value={time.minutes} label="min" />
      </div>
    </div>
  );
}

function Unit({ value, label }: { value: number; label: string }) {
  return (
    <div className="flex flex-col items-center leading-none">
      <span className="text-xl font-bold tabular-nums">{value}</span>
      <span className="text-[10px] uppercase tracking-wider opacity-70">
        {label}
      </span>
    </div>
  );
}
