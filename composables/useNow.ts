/**
 * The render time, fixed on the server and reused on the client so that
 * computed durations match during hydration.
 */
export function useNow(): Date {
  const iso = useState("resume-now", () => new Date().toISOString());
  return new Date(iso.value);
}
