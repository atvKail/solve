def readData(path: str) -> list:
    with open(path, "r") as f:
        data = [tuple(line.strip().split()) for line in f.readlines()]
    return data

