def simulate_editor(n):
    s = ">" + "0" * 15 + "1" * n + "2" * 21

    while ">1" in s or ">2" in s or ">0" in s:
        if ">1" in s:
            s = s.replace(">1", "23>", 1)
        if ">2" in s:
            s = s.replace(">2", "2>", 1)
        if ">0" in s:
            s = s.replace(">0", "3>", 1)

    result_string = s.replace(">", "")

    digit_sum = sum(int(digit) for digit in result_string)

    return digit_sum


n = 0
while True:
    digit_sum = simulate_editor(n)
    if digit_sum % 26 == 0:
        break
    n += 1

print(n)
