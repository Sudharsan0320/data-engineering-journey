import csv
with open("data.csv") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

print(f"Rows:{len(rows)}")
print(f"Columns:{reader.fieldnames}")
for row in rows:
    print(row)