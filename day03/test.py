import csv
with open("data/train.csv", newline="", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))
print("empty Age:", sum(1 for r in rows if r["Age"].strip() == ""))
print("empty Cabin:", sum(1 for r in rows if r["Cabin"].strip() == ""))
