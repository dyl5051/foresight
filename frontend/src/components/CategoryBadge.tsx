const colors: Record<string, string> = {
  politics: "bg-violet-100 text-violet-700",
  tech: "bg-sky-100 text-sky-700",
  economy: "bg-amber-100 text-amber-700",
};

export default function CategoryBadge({ category }: { category: string }) {
  return (
    <span
      className={`inline-block rounded-full px-2.5 py-0.5 text-xs font-medium uppercase tracking-wide ${colors[category] ?? "bg-gray-100 text-gray-600"}`}
    >
      {category}
    </span>
  );
}
