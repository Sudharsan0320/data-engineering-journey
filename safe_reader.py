class SafeReader:
    def __init__(self, path):
        self.path = path

    def readlines(self):
        try:
            with open(self.path, 'r') as file:
                return [line.strip() for line in file]
        except FileNotFoundError:
            print(f"Error: The file at {self.path} was not found.")
            return []

    def line_count(self):
        return len(self.readlines())


if __name__ == "__main__":
    r = SafeReader("data.csv")
    print(r.readlines())
    print(r.line_count())
    r2 = SafeReader("nope.txt")
    print(r2.readlines())
    print(r2.line_count())
    