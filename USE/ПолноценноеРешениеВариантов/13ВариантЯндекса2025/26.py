import heapq


def max_tasks_with_workers(n, times):
    heap = [(0, i) for i in range(n)]
    heapq.heapify(heap)
    total = 0
    for t in times:
        next_free, wid = heap[0]
        if next_free <= t:
            heapq.heappop(heap)
            total += 1
            heapq.heappush(heap, (t + 60, wid))
    return total


def main():
    with open("USE\\ПолноценноеРешениеВариантов\\13ВариантЯндекса2025\\26.txt") as f:
        data = f.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    k = int(next(it))
    times = [int(next(it)) for _ in range(k)]
    times.sort()

    total = max_tasks_with_workers(n, times)
    if n > 1:
        total_wo_one = max_tasks_with_workers(n - 1, times)
        min_count = total - total_wo_one
    else:
        min_count = total

    print(f"{total} {min_count}\n")


if __name__ == "__main__":
    main()
