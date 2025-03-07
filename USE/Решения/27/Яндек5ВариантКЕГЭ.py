import csv
from datetime import datetime

# Пути к файлам
data_A_path = "./USE/27/data/Яндекс5ВариантКЕГЭ/27_A.csv".replace("/", "\\")
data_B_path = "./USE/27/data/Яндекс5ВариантКЕГЭ/27_B.csv".replace("/", "\\")

# Названия столбцов
row_data_names = [
    "id записи",
    "id пользователя",
    "Тема",
    "Переход по баннеру",
    "Дата просмотра",
    "Проведённое время, сек",
    "Возраст",
]


# Функция для получения номера недели
def get_week_number(date_str):
    date = datetime.strptime(date_str.split()[0], "%d.%m.%Y")
    return date.isocalendar()[1]


# Функция для анализа данных
def analyze_data(file_path):
    data = {}
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=",")
        for row in reader:
            theme = row[row_data_names[2]]
            transition = int(1 if row[row_data_names[3]] == "Да" else 0)
            time_spent = int(row[row_data_names[5]])
            date = row[row_data_names[4]]
            age_group = row[row_data_names[-1]]
            user_id = row[row_data_names[1]]

            # Учитываем только переходы с временем >= 5 секунд
            if transition == 1 and time_spent >= 5:
                week = get_week_number(date)
                if week not in data:
                    data[week] = {
                        "Образование": 0,
                        "Подарки на Новый год": 0,
                        "Путешествия": 0,
                        "Электроника": 0,
                        "user_education": {},
                        "age_13_17_education": 0,
                    }

                # Увеличиваем счетчик для соответствующей темы
                if theme in data[week]:
                    data[week][theme] += 1

                # Обработка данных для темы "Образование"
                if theme == "Образование":
                    if user_id not in data[week]["user_education"]:
                        data[week]["user_education"][user_id] = 0
                    data[week]["user_education"][user_id] += 1
                    if age_group == "13-17":
                        data[week]["age_13_17_education"] += 1
    return data


# Функция для поиска максимального временного участка (файл A)
def find_max_segment_A(data):
    weeks = sorted(data.keys())
    max_length = 0
    best_segment = []

    # Отладочная информация
    print("Weeks:", weeks)

    for i in range(len(weeks)):
        current_segment = []
        for j in range(i, len(weeks)):
            week = weeks[j]
            # Условие: переходов по теме "Подарки на Новый год" больше или равно переходам по теме "Образование"
            gifts = data[week].get("Подарки на Новый год", 0)
            education = data[week].get("Образование", 0)
            if gifts >= education:
                current_segment.append(week)
            else:
                break

        # Отладочная информация
        print(f"Current segment starting at week {weeks[i]}: {current_segment}")

        if len(current_segment) > max_length:
            max_length = len(current_segment)
            best_segment = current_segment

    # Если временной участок пустой, выводим сообщение
    if not best_segment:
        print("No valid segment found for file A.")
        return 0, 0

    # Вычисляем метрики для найденного участка
    user_transitions = {}
    total_age_13_17_transitions = 0
    for week in best_segment:
        for user_id, count in data[week]["user_education"].items():
            if user_id not in user_transitions:
                user_transitions[user_id] = 0
            user_transitions[user_id] += count
        total_age_13_17_transitions += data[week]["age_13_17_education"]

    max_user_transitions = max(user_transitions.values(), default=0)

    # Отладочная информация
    print("Best segment:", best_segment)
    print("User transitions:", user_transitions)
    print("Max user transitions:", max_user_transitions)
    print("Total age 13-17 transitions:", total_age_13_17_transitions)

    return max_user_transitions, total_age_13_17_transitions


# Функция для поиска максимального временного участка (файл B)
def find_max_segment_B(data):
    weeks = sorted(data.keys())
    max_length = 0
    best_segment = []

    for i in range(len(weeks)):
        current_segment = []
        for j in range(i, len(weeks)):
            week = weeks[j]
            # Условие: переходов по теме "Образование" больше, чем суммарных переходов по темам "Путешествия" и "Электроника"
            education = data[week].get("Образование", 0)
            travel_electronics = data[week].get("Путешествия", 0) + data[week].get(
                "Электроника", 0
            )
            if education > travel_electronics:
                current_segment.append(week)
            else:
                break
        if len(current_segment) > max_length:
            max_length = len(current_segment)
            best_segment = current_segment

    # Вычисляем метрики для найденного участка
    user_transitions = {}
    total_age_13_17_transitions = 0
    for week in best_segment:
        for user_id, count in data[week]["user_education"].items():
            if user_id not in user_transitions:
                user_transitions[user_id] = 0
            user_transitions[user_id] += count
        total_age_13_17_transitions += data[week]["age_13_17_education"]

    max_user_transitions = max(user_transitions.values(), default=0)
    return max_user_transitions, total_age_13_17_transitions


# Анализ данных для файлов A и B
data_A = analyze_data(data_A_path)
data_B = analyze_data(data_B_path)

# Поиск результатов для файла A
result_A = find_max_segment_A(data_A)

# Поиск результатов для файла B
result_B = find_max_segment_B(data_B)

# Вывод результатов
print(f"{result_A[0]} {result_A[1]}")
print(f"{result_B[0]} {result_B[1]}")



# Неверно сделан