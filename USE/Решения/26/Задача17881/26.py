students = []
with open("USE\\Решения\\26\\Задача17881\\26_17881.txt", "r") as f:
    n = int(f.readline().strip())
    while (x := f.readline()) != "":
        stud_id, x1, x2, x3, x4 = map(int, x.strip().split())
        grades = [x1, x2, x3, x4]
        count_twos = grades.count(2)
        avg = sum(grades) / 4.0
        students.append(
            {"id": stud_id, "grades": grades, "count_twos": count_twos, "avg": avg}
        )

passed = [s for s in students if s["count_twos"] == 0]
failed = [s for s in students if s["count_twos"] >= 1]

passed_sorted = sorted(passed, key=lambda s: (-s["avg"], s["id"]))

failed_sorted = sorted(failed, key=lambda s: (s["count_twos"], s["id"]))

rating = [s["id"] for s in passed_sorted] + [s["id"] for s in failed_sorted]

idx_scholarship = n // 4 - 1
id_last_scholar = rating[idx_scholarship]

twos_by_id = {s["id"]: s["count_twos"] for s in students}
id_more_than_two = None
for stud_id in rating:
    if twos_by_id[stud_id] > 2:
        id_more_than_two = stud_id
        break

print(id_last_scholar, id_more_than_two)
