from csv import DictReader


locations_file = ".\\USE\\3\\Tables\\ЯндексВариант5КЕГЭ\\3Локации.csv"
sales_file = ".\\USE\\3\\Tables\\ЯндексВариант5КЕГЭ\\3Продажи.csv"

rows_name_locations = ["ID локации", "Локация", "Тип площадки", "Время работы"]
rows_name_sales = ["ID продажи", "Дата", "ID локации", "Код товара", "Количество", "Тип операции"]

timeWork = {}
with open(locations_file, newline='', encoding="utf-8") as csvfile:
    dlocations = DictReader(csvfile)
    for row in dlocations:
        id_location = row[rows_name_locations[0]]
        time_range = row[rows_name_locations[3]].replace(' ', '').split('-')
        if len(time_range) == 2:
            start_time = time_range[0].split(':')
            end_time = time_range[1].split(':')
            timeWork[id_location] = {
                'start_hour': int(start_time[0]),
                'start_minute': int(start_time[1]),
                'end_hour': int(end_time[0]),
                'end_minute': int(end_time[1])
            }

maxSales = {}
with open(sales_file, newline='', encoding="utf-8") as csvfile:
    dsales = DictReader(csvfile)
    for row in dsales:
        id_location = row[rows_name_sales[2]]
        operation_type = row[rows_name_sales[-1]]

        if operation_type == "Возврат":
            date, time_str = row[rows_name_sales[1]].split()
            _, month, day = date.split('-')
            hour, minute = map(int, time_str.split(':'))

            if month == '12' and '02' <= day <= '15':
                if id_location in timeWork:
                    work_start_hour = timeWork[id_location]['start_hour']
                    work_start_minute = timeWork[id_location]['start_minute']
                    work_end_hour = timeWork[id_location]['end_hour']
                    work_end_minute = timeWork[id_location]['end_minute']

                    current_minutes = hour * 60 + minute
                    work_start_minutes = work_start_hour * 60 + work_start_minute
                    work_end_minutes = work_end_hour * 60 + work_end_minute

                    if work_start_minutes <= work_end_minutes:
                        is_non_working = not (work_start_minutes <= current_minutes < work_end_minutes)
                    else:
                        is_non_working = not ((current_minutes >= work_start_minutes) or (current_minutes < work_end_minutes))

                    if is_non_working:
                        if id_location in maxSales:
                            maxSales[id_location] += 1
                        else:
                            maxSales[id_location] = 1

if maxSales:
    result_id = max(maxSales, key=maxSales.get)
    print(f"ID локации с наибольшим количеством возвратов в нерабочее время: {result_id}")
else:
    print("Нет возвратов в нерабочее время.")