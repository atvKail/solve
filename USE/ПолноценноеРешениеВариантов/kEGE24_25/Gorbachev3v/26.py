def read_data(filename="26.txt"):
    with open(filename, "r", encoding="utf-8") as f:
        data = f.read().split()
    return data


def solve(data):
    if not data:
        return

    N = int(data[0])
    S = int(data[1])
    candidates = []
    pos = 2
    for _ in range(N):
        cid = int(data[pos])
        pos += 1
        score1 = int(data[pos])
        pos += 1
        score2 = int(data[pos])
        pos += 1
        score3 = int(data[pos])
        pos += 1
        interview = int(data[pos])
        pos += 1
        exam_sum = score1 + score2 + score3
        candidates.append((cid, exam_sum, interview))

    groups = {}
    for cand in candidates:
        cid, exam_sum, interview = cand
        groups.setdefault(exam_sum, []).append(cand)

    exam_sums_sorted = sorted(groups.keys(), reverse=True)

    admitted = []
    current_count = 0
    semi_pass_not_admitted = 0

    for es in exam_sums_sorted:
        group = groups[es]
        group_size = len(group)
        if current_count + group_size < S:
            admitted.extend(group)
            current_count += group_size
        elif current_count + group_size == S:
            admitted.extend(group)
            current_count += group_size
            break
        else:
            remaining = S - current_count
            group_sorted = sorted(group, key=lambda x: (x[2], x[0]), reverse=True)
            admitted_from_group = group_sorted[:remaining]
            admitted.extend(admitted_from_group)
            semi_pass_not_admitted = group_size - remaining
            current_count += remaining
            break

    admitted_sorted = sorted(admitted, key=lambda x: (x[1], x[2], x[0]), reverse=True)
    last_candidate_id = admitted_sorted[-1][0]

    return last_candidate_id, semi_pass_not_admitted


def main():
    data = read_data("USE\\ПолноценноеРешениеВариантов\\kEGE24_25\\Gorbachev3v\\26.txt")
    result = solve(data)
    if result is not None:
        print(result[0], result[1])


if __name__ == "__main__":
    main()
# Намного легче при помощи excel или libre calc
