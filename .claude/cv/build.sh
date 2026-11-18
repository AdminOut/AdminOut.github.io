#!/usr/bin/env bash
# Build the emailable CV into .artifacts/Lance-Moore-CV.pdf.
#
#   .claude/cv/build.sh
#
# Images come from assets/img, content from .claude/cv/content.py, fonts
# (Inter, SIL OFL) from .claude/cv/fonts. Rendered with WeasyPrint and gated
# by the pdf-generation skill, both through uv, so nothing is installed.
# A WeasyPrint warning fails the build.
set -euo pipefail

here=$(cd "$(dirname "$0")" && pwd)
repo=$(cd "$here/../.." && pwd)
out="$repo/.artifacts/Lance-Moore-CV.pdf"
work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT

uv run -q --with pillow --with segno python -I "$here/assets.py" "$repo" "$work"
cp -r "$here/fonts" "$work/fonts"
python3 -I "$here/content.py" "$work/cv.html"
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

cd "$repo"
python3 ~/.claude/skills/pdf-generation/assets/build_doc.py --client default --check-only "$out"
echo "$out"
