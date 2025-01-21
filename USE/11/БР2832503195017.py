import math


total_memory_bits = 71680 * 8  # Память в битах
num_serials = 345

bits_25_digit = math.ceil(math.log2(25))  # 5 бит
bits_487_symbol = math.ceil(math.log2(487))  # 9 бит


def satisfies_condition(n):
    for x in range(n + 1):
        y = n - x
        bits_per_serial = x * bits_25_digit + y * bits_487_symbol
        total_bits = num_serials * bits_per_serial
        if total_bits > total_memory_bits:
            return True
    return False


n = 1
while not satisfies_condition(n):
    n += 1

print(n)
