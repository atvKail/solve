def modifed_merge_sorting(arr, key=lambda a, b: a >= b):
    def merge(a, b):
        res = []
        i = 0
        j = 0
        while i < len(a) and j < len(b):
            if key(a[i], b[j]):
                res.append(a[i])
                i += 1
            else:
                res.append(b[j])
                j += 1
        res.extend(a[i:])
        res.extend(b[j:])
        return res

    def msort(a):
        if len(a) <= 1:
            return a
        k = len(a) // 2
        return merge(msort(a[:k]), msort(a[k:]))

    return msort(arr)


passed_students = []

with open("USE\\26\\БР2832503195017.txt", "r") as file:
    data = file.readlines()

    n = int(data[0])
    for line in data[1:]:
        id, o1, o2, o3, o4 = map(int, line.split())

        if (o1 != 2) and (o2 != 2) and (o3 != 2) and (o4 != 2):
            passed_students.append([id, o1 + o2 + o3 + o4]) # id, sum

key =lambda a, b: a[1] > b[1] or (a[1] == b[1] and a[0] > b[0])
passed_students = modifed_merge_sorting(passed_students, key)

n_passed_students = len(passed_students)
percentages_10_for_st = int(n_passed_students * 0.1) 
st_students = passed_students[:percentages_10_for_st]

print(st_students[-1][0], n_passed_students - len(st_students))

print(passed_students[:20])
