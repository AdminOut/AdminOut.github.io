#!/usr/bin/env bash
# Build both copies of the CV:
#
#   .artifacts/Lance-Moore-CV.pdf   private, gitignored: the copy to attach to
#                                   emails, with a clickable email address
#   public/Lance-Moore-CV.pdf       public, committed: the site's download, with
#                                   the address as an image only, so it cannot
#                                   be scraped
#
#   .claude/cv/build.sh
#
# Images come from assets/img, content from .claude/cv/content.py, fonts
# (Inter, SIL OFL) from .claude/cv/fonts. Rendered with WeasyPrint and gated
# by the pdf-generation skill, both through uv, so nothing is installed.
# A WeasyPrint warning fails the build, as does an address in the public copy.
set -euo pipefail

here=$(cd "$(dirname "$0")" && pwd)
repo=$(cd "$here/../.." && pwd)
work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT

uv run -q --with pillow --with segno python -I "$here/assets.py" "$repo" "$work"
cp -r "$here/fonts" "$work/fonts"

render() {  # render <out.pdf> [--public]
  local out=$1; shift
  python3 -I "$here/content.py" "$work/cv.html" "$@"
  if grep -q '{{' "$work/cv.html"; then
    echo "FAIL  unfilled template token in cv.html" >&2
    exit 1
  fi
  mkdir -p "$(dirname "$out")"
  uvx --from weasyprint weasyprint -u "$work" "$work/cv.html" "$out" 2> "$work/render.log"
  if grep -E 'WARNING|ERROR' "$work/render.log" >&2; then
    echo "FAIL  WeasyPrint reported problems" >&2
    exit 1
  fi
  (cd "$repo" && python3 ~/.claude/skills/pdf-generation/assets/build_doc.py --client default --check-only "$out")
}

private="$repo/.artifacts/Lance-Moore-CV.pdf"
public="$repo/public/Lance-Moore-CV.pdf"
render "$private"
render "$public" --public

uvx --from pymupdf python -I -c '
import sys, pymupdf
d = pymupdf.open(sys.argv[1])
text = "".join(p.get_text() for p in d) + str(d.metadata)
uris = [l.get("uri", "") for p in d for l in p.get_links()]
if "@" in text or any(u.startswith("mailto:") for u in uris):
    sys.exit("FAIL  an email address reached the public copy")
print("PASS  no email address in the public copy")
' "$public"

echo "$private"
echo "$public"
