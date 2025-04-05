import time
from collections import Counter

import requests
from RatingSystem import CodeforcesRatingCalculator


def timer(func):
    def wrapper(*args, **kwargs):
        beg = time.time()
        res = func(*args, **kwargs)
        print("Elapsed:", time.time() - beg)
        return res

    return wrapper


@timer
def predict(rows, prev_ratings):
    calc = CodeforcesRatingCalculator(rows, prev_ratings)
    return calc.calculate_rating_changes()


ROUND1013DIV3 = 2091
EDUROUND177 = 2086

contest = EDUROUND177
url = f"https://codeforces.com/api/contest.standings?contestId={contest}"
resp = requests.get(url)
data = resp.json()
url2 = f"https://codeforces.com/api/contest.ratingChanges?contestId={contest}"
resp2 = requests.get(url2)
data2 = resp2.json()
resp.status_code, resp2.status_code

rows = data["result"]["rows"]
rows = [
    (row["party"]["members"][0]["handle"], row["rank"], row["points"], row["penalty"])
    for row in rows
]

prev_ratings, new_ratings = {}, {}
changes = data2["result"]

rated_for = set()
for change in changes:
    rated_for.add(change["handle"])
    prev_ratings[change["handle"]] = change["oldRating"]
    new_ratings[change["handle"]] = change["newRating"]
rows = [row for row in rows if row[0] in rated_for]
prev_ratings[rows[0][0]], new_ratings[rows[0][0]]

predicted = predict(rows, prev_ratings)

difs = Counter()
difdif = []
for handle, _, _, _ in rows:
    old = prev_ratings[handle]
    change = predicted[handle]
    new = new_ratings[handle]
    dif = new - (old + change)
    if abs(dif) > 2:
        print(handle, f"truedelta={new - old}", f"predict={change}", f"dif={dif}")
    difs[dif] += 1
    if round(dif):
        difdif.append(round(dif))

print(len(predicted), sorted(difs.items()))
