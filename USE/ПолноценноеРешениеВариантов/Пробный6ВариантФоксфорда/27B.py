file_B = "USE\\ПолноценноеРешениеВариантов\\Пробный6ВариантФоксфорда\\387705_B.txt"

with open(file_B, "r") as f:
    line = f.readline().strip()
    data_B = []
    while line != "":
        data_B.append(list(map(float, line.replace(',', '.').split())))
        line = f.readline()
