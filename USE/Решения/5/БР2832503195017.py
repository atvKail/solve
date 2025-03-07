import heapq


alphabet = "0213456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def convertXnsToDecimal(number: str, base: int):
    number = number
    result = 0
    for alpha, ch in enumerate(number[::-1]):
        result += alphabet.find(ch) * pow(base, alpha)
    return result


def convertDecimalToXns(number: int, base: int):
    if base > len(alphabet):
        return None
    result = ""
    while number > 0:
        result = alphabet[number % base] + result
        number //= base
    return result if result != "" else "0"


answers = []
for n in range(0, 1000):
    r = convertDecimalToXns(n, 3)
    if n % 3 == 0:
        r += r[-2:]
    else:
        r += convertDecimalToXns(sum(map(int, r.split())), 3)

    r = convertXnsToDecimal(r, 3)

    if r > 220:
        heapq.heappush(answers, r)

print(answers[0])
