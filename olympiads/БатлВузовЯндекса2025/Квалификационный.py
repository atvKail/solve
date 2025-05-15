# from typing import List, Dict, Set
# import re


# def solution(tasks: List[str]) -> List[List[str]]:
#   ws = [set(re.findall(r"\b\w+\b", t.lower())) for t in tasks]
#   n = len(tasks)
#   adj = {i: {j for j in range(n) if i != j and ws[i] & ws[j]} for i in range(n)}
#   cliques = []

#   def bronk(R: Set[int], P: Set[int], X: Set[int]):
#     if not P and not X and len(R) >= 2:
#       cliques.append(R)
#     for v in list(P):
#       bronk(R|{v}, P&adj[v], X&adj[v])
#       P.remove(v)
#       X.add(v)
#   bronk(set(), set(range(n)), set())

#   unique = []
#   seen = set()
#   for c in cliques:
#     key = tuple(sorted(c))
#     if key not in seen:
#       seen.add(key)
#       unique.append(c)
    
#   unique.sort(key=lambda c: [min(c)] + sorted(c))
#   return [[tasks[i] for i in sorted(c)] for c in unique] 


from typing import List, Dict, Set


def extract_words(s: str) -> Set[str]:
    s = s.lower()
    buf = []
    words = set()
    for ch in s:
        if ch.isalnum():
            buf.append(ch)
        else:
            if buf:
                words.add(''.join(buf))
                buf.clear()
    if buf:
        words.add(''.join(buf))
    return words


def solution(tasks: List[str]) -> List[List[str]]:
    ws = [extract_words(t) for t in tasks]
    n = len(tasks)

    inv: Dict[str, Set[int]] = {}
    for i, words in enumerate(ws):
        for w in words:
            inv.setdefault(w, set()).add(i)

    groups = [idxs for idxs in inv.values() if len(idxs) >= 2]

    uniq = []
    seen = set()
    for g in groups:
        key = tuple(sorted(g))
        if key not in seen:
            seen.add(key)
            uniq.append(g)
    uniq.sort(key=lambda g: (min(g), sorted(g)))

    return [[tasks[i] for i in sorted(g)] for g in uniq]


if __name__ == "__main__":
    tasks = [
        "Почистить дом от пыли",
        "Сделать уборку в доме",
        "Поиграть в футбол",
        "Купить новый мяч",
        "Прочитать книгу по Python"
    ]
    for grp in solution(tasks):
        print(grp)