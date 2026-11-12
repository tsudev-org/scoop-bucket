#!/usr/bin/env python3
"""Sinh catalog.json (danh muc may doc, schema 1) tu bucket/*.json - nguon cho website *.tsudev.com va
install.ps1 cua tsudev.com (tsudev-standards PACKAGING.md muc 6, 8), cung dang voi https://pkg.tsudev.com/catalog.json.

Tat dinh (khong dau thoi gian) va chi gom manifest dang co trong bucket - moi manifest tren main da qua CI cai thu
that tren Windows. Goi doi ten (notes chua `scoop install tsudev/<ten moi>`) ghi `replacedBy`.

  python3 tools/catalog.py           # ghi catalog.json
  python3 tools/catalog.py --check   # CI: loi neu catalog.json cu so voi bucket/
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

GOC = Path(__file__).resolve().parent.parent
BUCKET = "https://github.com/tsudev-org/scoop-bucket"
TEN = re.compile(r"[a-z][a-z0-9-]+")


def lenh(b) -> list[str]:
    """Ten lenh Scoop tao shim: `bin` la chuoi, mang chuoi, hoac mang [exe, alias, tham so]."""
    if not b:
        return []
    out = []
    for x in [b] if isinstance(b, str) else b:
        if isinstance(x, str):
            out.append(Path(x.replace("\\", "/")).stem)
        else:
            out.append(x[1] if len(x) > 1 else Path(x[0].replace("\\", "/")).stem)
    return out


def build() -> dict:
    pkgs = []
    for f in sorted((GOC / "bucket").glob("*.json")):
        n = f.stem
        if not TEN.fullmatch(n):
            sys.exit(f"ten manifest sai khuon: {f.name}")
        m = json.loads(f.read_text(encoding="utf-8"))
        notes = m.get("notes", [])
        notes = "\n".join(notes) if isinstance(notes, list) else notes
        moi = re.search(r"scoop install tsudev/([a-z0-9-]+)", notes or "")
        pkgs.append({
            "name": n,
            "version": m["version"],
            "description": m.get("description", ""),
            "homepage": m.get("homepage", ""),
            "license": m["license"] if isinstance(m.get("license"), str) else m.get("license", {}).get("identifier", ""),
            # Khong co `architecture` = mot tep chung (Scoop cai tren moi kien truc Windows).
            "arch": sorted(m.get("architecture", {}).keys()) or ["any"],
            "commands": lenh(m.get("bin")),
            "replacedBy": moi.group(1) if moi and moi.group(1) != n else None,
            "install": f"scoop install tsudev/{n}",
            "installFull": f"scoop bucket add tsudev {BUCKET}; scoop install tsudev/{n}",
        })
    ten = {p["name"] for p in pkgs}
    for p in pkgs:
        if p["replacedBy"] and p["replacedBy"] not in ten:
            sys.exit(f"{p['name']}: replacedBy {p['replacedBy']} khong co trong bucket")
    return {
        "schema": 1,
        "channel": "scoop",
        "bucket": {"name": "tsudev", "url": BUCKET},
        "setup": [f"scoop bucket add tsudev {BUCKET}"],
        "packages": pkgs,
    }


def main() -> None:
    out = GOC / "catalog.json"
    text = json.dumps(build(), ensure_ascii=False, indent=1) + "\n"
    if "--check" in sys.argv:
        if not out.exists() or out.read_text(encoding="utf-8") != text:
            sys.exit("catalog.json cu - chay: python3 tools/catalog.py")
        print("catalog.json khop bucket/")
        return
    with open(out, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print(f"catalog.json: {len(json.loads(text)['packages'])} goi")


if __name__ == "__main__":
    main()
