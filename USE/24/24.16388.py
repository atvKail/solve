"""
Задание 24 (№16388).
Текстовый файл состоит из символов К, L, Ми N.
В прилагаемом файле определите максимальное количество символов в непрерывной подпоследовательности,
состоящей из идущих подряд групп символов KLMN в указанном порядке,
при этом в начале и в конце искомой последовательности группа символов KLMN может быть неполной.
Искомая последовательность должна содержать не менее одной полной группы символов KLMN. Например,
условию задачи удовлетворяют: MNKLMNKLMNK, или
NKLMNKLMNKL, или KLMNKLMNKLMи т.п.
Для выполнения этого задания следует написать программу.

Ответ на КЕГЭ 182, хотя 182 / 4 = 45.5, что странно, т.к. у нас последовательности идут друг за другом
образуя: len(klmn klmn klmn) = 3 => всего символов 4 * 3 = 12
"""


def next_word(s):
    if len(s) > 4:
        return s[1:]
    return s


def finger(k_word):
    for i in range(4):
        if k_word[i] == 0:
            return i
    return -1


with open("USE/24/24_16388.txt", "r") as f:
    s = f.readline()

pattern, pid = "KLMN", [0, 1, 2, 3]

answers = []
words_collector = ["" for _ in range(4)]
cnts = [0 for _ in range(4)]
k_word = [0 for _ in range(4)]

# c = 0

# print(s[:100])

for idx in range(len(s) - 3):
    for j in range(4):
        words_collector[j] = next_word(words_collector[j] + s[idx + pid[j]])
        if k_word[j] != 0:
            k_word[j] -= 1

    for id in range(4):
        if k_word[id] == 0 and words_collector[id] == pattern:
            k_word[id] = 4
            cnts[id] += 1
        else:
            if k_word[id] == 0 and cnts[id] != 0:
                answers.append(cnts[id])
                cnts[id] = 0

    # print(words_collector, k_word, cnts)

    # if c == 100:
    #     break
    # c += 1

print(max(answers) * 4)  # answer: 180
