class Exercise24:
    def __init__(self, filename, target_A_count, forbidden_symbol):
        self.filename = filename
        self.target_A_count = target_A_count
        self.forbidden_symbol = forbidden_symbol

    def sol(self):
        with open(self.filename, "r", encoding="utf-8") as f:
            data = f.read().strip()

        max_length = 0
        segments = data.split(self.forbidden_symbol)
        for seg in segments:
            if seg.count("A") < self.target_A_count:
                continue
            positions = [i for i, ch in enumerate(seg) if ch == "A"]
            for i in range(len(positions) - self.target_A_count + 1):
                left_bound = 0 if i == 0 else positions[i - 1] + 1
                right_bound = (
                    len(seg) - 1
                    if (i + self.target_A_count == len(positions))
                    else positions[i + self.target_A_count] - 1
                )
                current_length = right_bound - left_bound + 1
                if current_length > max_length:
                    max_length = current_length

        return max_length


ex24 = Exercise24(filename="USE\\kEGE24_25\\Gorbachev3v\\24.txt", target_A_count=22, forbidden_symbol="F")
print("Задание 24:")
print(ex24.sol())
