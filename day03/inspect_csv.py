from pathlib import Path

p = Path("data.csv")
p.exists()

folder = Path("day03")
f = folder / "out.csv"

list(Path(".").glob("*.csv"))
list(Path(".").rglob("*.csv"))

print(p.exists())
print(f)
print(list(Path(".").glob("*.csv")))


p.name
p.suffix
p.stem