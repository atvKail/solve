from itertools import product
import re

alphabet = "ЯНВАРЬ"

n = 5
pattern = r"^([^Я].*|$)"
valid_ya = r"^[^Я]*Я?[^Я]*$"
no_consecutive_ya = r"^(?!.*ЯЯ).*"

idx = 0
lstValididx = 0

for word in product(alphabet, repeat=n):
    idx += 1
    word = "".join(word)

    if (
        re.match(pattern, word)
        and re.match(valid_ya, word)
        and re.match(no_consecutive_ya, word)
    ):
        lstValididx = idx

print(lstValididx)
