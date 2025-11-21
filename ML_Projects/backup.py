import json
import os
import shutil
from datetime import datetime

MANIFEST = "backup_manifest.json"

def load_manifest(d):
    p = os.path.join(d, MANIFEST)
    if not os.path.exists(p):
        return {}
    try:
        with open(p, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}

def save_manifest(d, m):
    p = os.path.join(d, MANIFEST)
    with open(p, "w", encoding="utf-8") as f:
        json.dump(m, f, indent=2, ensure_ascii=False)

def rel(root, p):
    return os.path.relpath(p, root)

def changed(p, manifest, root):
    try:
        m = os.path.getmtime(p)
    except Exception:
        return False
    key = rel(root, p)
    entry = manifest.get(key)
    if not entry:
        return True
    return entry.get("mtime") != m

def do_backup(src, dest):
    if not os.path.exists(src):
        print("source not found:", src)
        return
    os.makedirs(dest, exist_ok=True)
    manifest = load_manifest(dest)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    snap = os.path.join(dest, ts)
    copied = 0
    for root, dirs, files in os.walk(src):
        for name in files:
            sp = os.path.join(root, name)
            try:
                if changed(sp, manifest, src):
                    rp = rel(src, sp)
                    dp = os.path.join(snap, rp)
                    os.makedirs(os.path.dirname(dp), exist_ok=True)
                    shutil.copy2(sp, dp)
                    manifest[rp] = {"mtime": os.path.getmtime(sp)}
                    copied += 1
            except Exception as e:
                print("failed:", sp, e)
    if copied:
        save_manifest(dest, manifest)
        print(f"backed up {copied} files to {snap}")
    else:
        if os.path.exists(snap) and not os.listdir(snap):
            try:
                os.rmdir(snap)
            except Exception:
                pass
        print("no changes")

def main():
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--source", "-s", required=True)
    p.add_argument("--dest", "-d", required=True)
    a = p.parse_args()
    s = os.path.abspath(a.source)
    d = os.path.abspath(a.dest)
    do_backup(s, d)

if __name__ == "__main__":
    main()
