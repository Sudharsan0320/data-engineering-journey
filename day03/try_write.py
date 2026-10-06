import csv

rows = [["Name", "Age"], ["Ana", "30"], ["Bob", "25"]]

with open("day03/out.csv", "w", newline = "") as f:
    writer = csv.writer(f)
    writer.writerows(rows)