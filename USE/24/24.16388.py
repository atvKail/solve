# def next_word(s):
#     if len(s) > 4:
#         return s[1:]
#     return s


# with open("USE/24/24_16388.txt", "r") as f:
#     s = f.readline()

# pattern = "KLMN"

# answers = []
# words_collector = ["" for _ in range(4)]
# cnts = [0 for _ in range(4)]
# y_word = [False for _ in range(4)]

# c = 0

# for idx, ch in enumerate(s):
#     for j in range(idx % 4 + 1):
#         words_collector[j] = next_word(words_collector[j] + ch)
    
#     if pattern in words_collector:
#         cnts[words_collector.find(pattern)]
#     print(s[:idx])
#     print(words_collector)
#     if c == 5:
#         break
#     c += 1

def next_word(s):
    if len(s) > 4:
        return s[1:]
    return s

with open("USE/24/24_16388.txt", "r") as f:
    s = f.readline().strip()

pattern = "KLMN"

# Переменные для хранения текущей длины и максимальной длины последовательности
current_length = 0
max_length = 0

# Для отслеживания текущей группы символов
current_group = ""

# Флаг наличия хотя бы одной полной группы KLMN
has_full_group = False

for ch in s:
    current_group += ch
    
    # Если текущая группа превышает длину 4, обрезаем начало
    if len(current_group) > 4:
        current_group = current_group[1:]

    # Проверяем, если текущая группа соответствует шаблону
    if current_group == pattern:
        has_full_group = True
        current_length += len(current_group)
        current_group = ""  # Сбрасываем группу для начала новой
    elif ch == pattern[len(current_group) - 1]:
        # Продолжаем накапливать группу
        current_length += 1
    else:
        # Если символ не подходит, сбрасываем текущую длину
        if has_full_group:
            max_length = max(max_length, current_length)
        current_length = len(current_group)
        has_full_group = False

# Проверяем последнюю последовательность
if has_full_group:
    max_length = max(max_length, current_length)

print("Максимальная длина последовательности:", max_length)