/**
 * Month-precision periods for the resume. A month is written "YYYY-MM";
 * an open-ended period (end undefined) runs to the current month.
 */

const MONTHS = [
  "Jan",
  "Feb",
  "Mar",
  "Apr",
  "May",
  "Jun",
  "Jul",
  "Aug",
  "Sep",
  "Oct",
  "Nov",
  "Dec",
];

function parseMonth(month: string): { year: number; index: number } {
  const [year, m] = month.split("-").map(Number);
  return { year, index: m - 1 };
}

export function currentMonth(now: Date): string {
  const m = String(now.getUTCMonth() + 1).padStart(2, "0");
  return `${now.getUTCFullYear()}-${m}`;
}

/** Whole months covered, counting both the first and last month. */
export function monthsBetween(start: string, end: string): number {
  const a = parseMonth(start);
  const b = parseMonth(end);
  return (b.year - a.year) * 12 + (b.index - a.index) + 1;
}

export function formatMonth(month: string): string {
  const { year, index } = parseMonth(month);
  return `${MONTHS[index]} ${year}`;
}

export function formatDuration(months: number): string {
  const years = Math.floor(months / 12);
  const rest = months % 12;
  const parts: string[] = [];
  if (years) parts.push(`${years} ${years === 1 ? "yr" : "yrs"}`);
  if (rest) parts.push(`${rest} ${rest === 1 ? "mo" : "mos"}`);
  return parts.join(" ") || "1 mo";
}

/** e.g. "Sep 2023 to Present · 3 yrs 3 mos" */
export function formatPeriod(
  start: string,
  end: string | undefined,
  now: Date
) {
  const last = end ?? currentMonth(now);
  const range = `${formatMonth(start)} to ${
    end ? formatMonth(end) : "Present"
  }`;
  return `${range} · ${formatDuration(monthsBetween(start, last))}`;
}

/** Completed years from a start month to now, e.g. for "11+ years". */
export function yearsSince(start: string, now: Date): number {
  return Math.floor(monthsBetween(start, currentMonth(now)) / 12);
}
