#!/usr/bin/env python3
"""Regenerate the progress tables in README.md and in every section README.

Lesson notes are the single source of truth. The front matter of each note in
a section folder provides `title`, `type` (lesson | quiz | certificate),
`duration` (m:ss) and `status` (todo | draft | done). This script rewrites the
content between `<!-- BEGIN generated: NAME -->` and `<!-- END generated: NAME -->`
markers; everything outside the markers is left untouched.

Usage:
    python scripts/update_progress.py          # rewrite the generated blocks
    python scripts/update_progress.py --check  # exit 1 if any block is stale
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SECTION_DIR = re.compile(r"^\d{2}-[a-z0-9-]+$")
NOTE_FILE = re.compile(r"^(\d{2})-[a-z0-9-]+\.md$")
STATUS_LABELS = {"todo": "Not started", "draft": "Draft", "done": "Done"}
TYPE_LABELS = {"lesson": "Video", "quiz": "Quiz", "certificate": "Certificate"}


@dataclass
class Note:
    path: Path
    number: int
    title: str
    kind: str
    seconds: int
    status: str


@dataclass
class Section:
    path: Path
    number: int
    title: str
    short_title: str
    notes: list[Note] = field(default_factory=list)

    @property
    def videos(self) -> int:
        return sum(note.kind == "lesson" for note in self.notes)

    @property
    def done(self) -> int:
        return sum(note.status == "done" for note in self.notes)

    @property
    def seconds(self) -> int:
        return sum(note.seconds for note in self.notes)


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def read_front_matter(path: Path) -> dict[str, str]:
    """Read top-level `key: value` pairs; list values (tags, aliases) are skipped."""
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    data: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        match = re.match(r"^([A-Za-z_][\w-]*):\s*(.*?)\s*$", line)
        if match:
            key, value = match.groups()
            if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
                value = value[1:-1]
            data[key] = value
    return data


def parse_duration(value: str, path: Path) -> int:
    if not value:
        return 0
    try:
        seconds = 0
        for part in value.split(":"):
            seconds = seconds * 60 + int(part)
        return seconds
    except ValueError:
        sys.exit(f"{rel(path)}: invalid duration {value!r} (expected m:ss or h:mm:ss)")


def format_duration(seconds: int) -> str:
    if not seconds:
        return "—"
    hours, rest = divmod(seconds, 3600)
    minutes, secs = divmod(rest, 60)
    return f"{hours}:{minutes:02d}:{secs:02d}" if hours else f"{minutes}:{secs:02d}"


def load_sections() -> list[Section]:
    sections = []
    for directory in sorted(p for p in ROOT.iterdir() if p.is_dir() and SECTION_DIR.match(p.name)):
        readme = directory / "README.md"
        meta = read_front_matter(readme) if readme.exists() else {}
        if meta.get("type") != "section":
            continue
        section = Section(
            path=directory,
            number=int(meta["section"]),
            title=meta["title"],
            short_title=meta.get("short_title", meta["title"]),
        )
        for file in sorted(directory.glob("*.md")):
            match = NOTE_FILE.match(file.name)
            if not match:
                continue
            fm = read_front_matter(file)
            status = fm.get("status", "todo")
            if status not in STATUS_LABELS:
                sys.exit(f"{rel(file)}: unknown status {status!r} (use one of: {', '.join(STATUS_LABELS)})")
            section.notes.append(
                Note(
                    path=file,
                    number=int(match.group(1)),
                    title=fm.get("title", file.stem),
                    kind=fm.get("type", "lesson"),
                    seconds=parse_duration(fm.get("duration", ""), file),
                    status=status,
                )
            )
        sections.append(section)
    return sections


def percent(done: int, total: int) -> int:
    return round(100 * done / total) if total else 0


def render_section_table(section: Section) -> str:
    rows = [
        "| # | Lesson | Type | Duration | Notes |",
        "|---:|---|---|---:|---|",
    ]
    for note in section.notes:
        rows.append(
            f"| {note.number} | [{note.title}]({note.path.name}) "
            f"| {TYPE_LABELS.get(note.kind, note.kind.title())} "
            f"| {format_duration(note.seconds)} | {STATUS_LABELS[note.status]} |"
        )
    rows.append("")
    rows.append(
        f"**Video time:** {format_duration(section.seconds)} · "
        f"**Notes completed:** {section.done} / {len(section.notes)}"
    )
    return "\n".join(rows)


def render_overview(sections: list[Section]) -> str:
    rows = [
        "| # | Section | Videos | Video time | Notes completed |",
        "|---:|---|---:|---:|---:|",
    ]
    for s in sections:
        rows.append(
            f"| {s.number} | [{s.short_title}]({s.path.name}/README.md) | {s.videos} "
            f"| {format_duration(s.seconds)} | {s.done} / {len(s.notes)} |"
        )
    done = sum(s.done for s in sections)
    total = sum(len(s.notes) for s in sections)
    rows.append(
        f"| | **Total** | **{sum(s.videos for s in sections)}** "
        f"| **{format_duration(sum(s.seconds for s in sections))}** "
        f"| **{done} / {total} ({percent(done, total)}%)** |"
    )
    return "\n".join(rows)


def render_course_map(sections: list[Section]) -> str:
    lines = []
    for s in sections:
        lines.append(f"### [Section {s.number} — {s.title}]({s.path.name}/README.md)")
        lines.append("")
        for note in s.notes:
            box = "x" if note.status == "done" else " "
            detail = format_duration(note.seconds) if note.seconds else TYPE_LABELS.get(note.kind, note.kind)
            draft = " · draft" if note.status == "draft" else ""
            lines.append(f"- [{box}] [{note.title}]({rel(note.path)}) · {detail}{draft}")
        lines.append("")
    return "\n".join(lines).rstrip()


def replace_block(text: str, name: str, content: str, path: Path) -> str:
    pattern = re.compile(
        rf"(<!-- BEGIN generated: {re.escape(name)} -->).*?(<!-- END generated: {re.escape(name)} -->)",
        re.S,
    )
    if not pattern.search(text):
        sys.exit(f"{rel(path)}: missing '<!-- BEGIN generated: {name} -->' / '<!-- END generated: {name} -->' markers")
    return pattern.sub(lambda m: f"{m.group(1)}\n\n{content}\n\n{m.group(2)}", text, count=1)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true", help="only report stale files, do not write")
    args = parser.parse_args()

    sections = load_sections()
    if not sections:
        sys.exit("No section folders found.")

    targets: dict[Path, dict[str, str]] = {
        ROOT / "README.md": {
            "overview": render_overview(sections),
            "course-map": render_course_map(sections),
        }
    }
    for s in sections:
        targets[s.path / "README.md"] = {"lessons": render_section_table(s)}

    stale = []
    for path, blocks in targets.items():
        original = path.read_text(encoding="utf-8")
        text = original
        for name, content in blocks.items():
            text = replace_block(text, name, content, path)
        if text != original:
            stale.append(path)
            if not args.check:
                with open(path, "w", encoding="utf-8", newline="\n") as handle:
                    handle.write(text)

    done = sum(s.done for s in sections)
    drafts = sum(n.status == "draft" for s in sections for n in s.notes)
    total = sum(len(s.notes) for s in sections)
    print(f"Notes completed: {done}/{total} ({percent(done, total)}%), drafts: {drafts}")

    if args.check:
        for path in stale:
            print(f"stale: {rel(path)}")
        return 1 if stale else 0
    for path in stale:
        print(f"updated: {rel(path)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
