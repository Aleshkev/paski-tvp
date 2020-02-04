from pathlib import Path
import string

p = Path("paski.txt")
s = p.read_text("utf-8").upper()

for k, v in {'„': '"', '”': '"', "…": "...", "–": "-", "—": "-", "  ": " "}.items():
    s = s.replace(k, v)

t = set(x for x in set(x.strip() for x in s.splitlines()) if x)

met = {}
for i in t:
    j = "".join(c for c in i if c not in string.punctuation + string.whitespace)
    if j in met.keys():
        print(f"Kolizja interpunkcyjna: {met[j]}, {i}")
    if "  " in i:
        print(f"Podwójna spacja: {i}")
    met[j] = i

s = "\n".join(sorted(t))

print(f"Paski: {len(s.splitlines())}")

p.write_text(s, "utf-8")
