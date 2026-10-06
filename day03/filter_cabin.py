import csv

with open("data/train.csv", newline="", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

cabin_rows = [r for r in rows if r["Cabin"].strip() != ""]
print(f"Rows with Cabin: {len(cabin_rows)}")
print(f"Rows without Cabin: {len(rows) - len(cabin_rows)}")

with open("day03/with_cabin.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["Name", "Age", "Cabin", "Survived"])
    writer.writeheader()
    for r in cabin_rows:
        writer.writerow({"Name": r["Name"], "Age": r["Age"],
                         "Cabin": r["Cabin"], "Survived": r["Survived"]})
