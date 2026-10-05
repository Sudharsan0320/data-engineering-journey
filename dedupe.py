from safe_reader import SafeReader

reader = SafeReader("messy.txt")
lines = reader.readlines()

unique = set(lines)

with open("unique_messy.txt","w") as file:
    for line in unique:
        file.write(line + "\n")

print(f"{len(lines)} lines in, {len(unique)} unique out")

