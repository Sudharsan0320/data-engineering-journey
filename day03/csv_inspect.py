import csv
from os import path

def inspect_csv(path):
    with open(path, newline="", encoding = "utf-8-sig") as f:
        reader = csv.DictReader(f)

        cols = reader.fieldnames
        row_count = 0
        counts = {col:0 for col in cols}

        for row in reader:
            row_count += 1
            for col in cols:
                        if row[col].strip() != "":
                            counts[col] += 1   
     

        print(f"File: {path}")
        print(f"Rows: {row_count}")

        print(f"Columns: {', '.join(cols)}")
        for col in cols:
            print(f"  {col}: {counts[col]}")


if __name__ == "__main__":
    inspect_csv("data/train.csv")
