from pathlib import Path

p = Path("paski.txt")
s = p.read_text("utf-8").upper()

for k, v in {'„': '"', '”': '"', "…": "...", "–": "-", "—": "-"}.items():
    s = s.replace(k, v)

s = "\n".join(sorted(x for x in set(x.strip() for x in s.splitlines()) if x))

print(f"Paski: {len(s.splitlines())}")

p.write_text(s, "utf-8")
