# def modifed_merge_sorting(arr, key=lambda a, b: a >= b):
#     def merge(a, b):
#         res = []
#         i = 0
#         j = 0
#         while i < len(a) and j < len(b):
#             if key(a[i], b[j]):
#                 res.append(a[i])
#                 i += 1
#             else:
#                 res.append(b[j])
#                 j += 1
#         res.extend(a[i:])
#         res.extend(b[j:])
#         return res

#     def msort(a):
#         if len(a) <= 1:
#             return a
#         k = len(a) // 2
#         return merge(msort(a[:k]), msort(a[k:]))

#     return msort(arr)


# passed_students = []

# with open("USE\\26\\БР2832503195017.txt", "r") as file:
#     data = file.readlines()

#     n = int(data[0])
#     for line in data[1:]:
#         id, o1, o2, o3, o4 = map(int, line.split())

#         if (o1 != 2) and (o2 != 2) and (o3 != 2) and (o4 != 2):
#             passed_students.append([id, o1 + o2 + o3 + o4]) # id, sum

# key =lambda a, b: a[1] > b[1] or (a[1] == b[1] and a[0] > b[0])
# passed_students = modifed_merge_sorting(passed_students, key)

# n_passed_students = len(passed_students)
# percentages_10_for_st = int(n_passed_students * 0.1)
# st_students = passed_students[:percentages_10_for_st]

# print(st_students[-1][0], n_passed_students - len(st_students))

# print(passed_students[:20])


def merge_sort(arr, key=lambda x: x):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], key)
    right = merge_sort(arr[mid:], key)
    return merge(left, right, key)


def merge(left, right, key):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if key(left[i]) <= key(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def process_students_data():
    with open("USE\\26\\БР2832503195017.txt", "r") as file:
        data = file.readlines()

    N = int(data[0])
    students = []

    for line in data[1:]:
        parts = list(map(int, line.split()))
        student_id = parts[0]
        grades = parts[1:]
        total_score = sum(grades)
        twos_count = grades.count(2)
        threes_count = grades.count(3)

        passed = twos_count == 0

        students.append(
            {
                "id": student_id,
                "grades": grades,
                "total_score": total_score,
                "twos_count": twos_count,
                "threes_count": threes_count,
                "passed": passed,
            }
        )

    passed_students = [s for s in students if s["passed"]]
    failed_students = [s for s in students if not s["passed"]]

    passed_students = merge_sort(
        passed_students, key=lambda x: (-x["total_score"], -x["id"])
    )

    failed_students = merge_sort(
        failed_students, key=lambda x: (x["twos_count"], -x["id"])
    )

    scholarship_limit = N // 10
    scholarship_students = [
        s for s in passed_students if s["threes_count"] == 0 and s["twos_count"] == 0
    ]

    scholarship_students = scholarship_students[:scholarship_limit]

    if scholarship_students:
        last_scholarship_student = scholarship_students[-1]["id"]
    else:
        last_scholarship_student = None

    non_scholarship_students = [
        s for s in passed_students if s not in scholarship_students
    ]
    non_scholarship_count = len(non_scholarship_students)

    print(last_scholarship_student, non_scholarship_count)


if __name__ == "__main__":
    process_students_data()
