import csv


cnt = 0

with open("USE/9/9.csv", "r") as file:
    reader = csv.reader(file, delimiter=";")

    for row in reader:
        nums = list(map(int, row))
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        rep_nums = None
        uniq_num = []

        for num, cnt_num in freq.items():
            if cnt_num == 2:
                if rep_nums is not None:
                    break
                rep_nums = num
            elif cnt_num == 1:
                uniq_num.append(num)

        if rep_nums is not None and len(uniq_num) == 4:
            sum_of_squares = sum(num**2 for num in uniq_num)
            if sum_of_squares >= rep_nums**3:
                cnt += 1

    print(cnt)
