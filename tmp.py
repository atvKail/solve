# import sys
# import bisect


# input = sys.stdin.readline

# t = int(input())
# horizontals = []
# verticals = []
# for i in range(1, t + 1):
#     x1, y1, x2, y2 = map(int, input().split())
#     if y1 == y2:
#         xmin, xmax = min(x1, x2), max(x1, x2)
#         horizontals.append((xmin, xmax, y1, i))
#     else:
#         ymin, ymax = min(y1, y2), max(y1, y2)
#         verticals.append((x1, ymin, ymax, i))

# events = []
# for xmin, xmax, y, idH in horizontals:
#     events.append((xmin, 0, y, idH))
#     events.append((xmax, 2, y, idH))
# for x, ymin, ymax, idV in verticals:
#     events.append((x, 1, ymin, ymax, idV))

# events.sort(key=lambda x: (x[0], x[1]))

# active = []
# id_to_y = {}
# flagH = [False] * (t + 1)
# flagV = [False] * (t + 1)

# for ev in events:
#     if ev[1] == 0:
#         _, _, y, idH = ev
#         bisect.insort(active, (y, idH))
#         id_to_y[idH] = y
#     elif ev[1] == 2:
#         _, _, y, idH = ev
#         pos = bisect.bisect_left(active, (y, idH))
#         if pos < len(active) and active[pos] == (y, idH):
#             active.pop(pos)
#     else:
#         _, _, ymin, ymax, idV = ev
#         l = bisect.bisect_right(active, (ymin, 10**18))
#         r = bisect.bisect_left(active, (ymax, -(10**18)))
#         if l < r:
#             flagV[idV] = True
#             for y, idH in active[l:r]:
#                 flagH[idH] = True

# ans = 0
# for i in range(1, t + 1):
#     if flagH[i] or flagV[i]:
#         ans += 1
# print(ans)


# def ntod(x: str, n: int) -> int:
#     import string

#     alph = "0123456789" + string.ascii_uppercase
#     num = list(x)
#     dnum = sum(alph.index(num[i]) * n ** (len(num) - i - 1) for i in range(len(num)))
#     return dnum


# print(ntod("2N04", 36))

# print(2 & 1 == 0)


# def dbscan(points, eps, min_pts):
#     labels = [None] * len(points)
#     cluster_id = 0
#     for i in range(len(points)):
#         if labels[i] is not None:
#             continue

#         neighbors = []
#         for j in range(len(points)):
#             dx = points[i][0] - points[j][0]
#             dy = points[i][1] - points[j][1]
#             if dx * dx + dy * dy <= eps * eps:
#                 neighbors.append(j)

#         if len(neighbors) < min_pts:
#             labels[i] = -1
#         else:
#             cluster_id += 1
#             labels[i] = cluster_id
#             k = 0

#             while k < len(neighbors):
#                 j = neighbors[k]
#                 if labels[j] == -1:
#                     labels[j] = cluster_id
#                 if labels[j] is None:
#                     labels[j] = cluster_id

#                     new_neighbors = []
#                     for m in range(len(points)):
#                         dx = points[j][0] - points[m][0]
#                         dy = points[j][1] - points[m][1]
#                         if dx * dx + dy * dy <= eps * eps:
#                             new_neighbors.append(m)

#                     if len(new_neighbors) >= min_pts:
#                         neighbors += new_neighbors
#                 k += 1
#     return labels


# import os


# source_root = "/путь/к/родительской/папке"
# destination_folder = "/путь/к/папке/назначения"

# video_extensions = {'.mp4', '.avi', '.mkv', '.mov', '.webm', '.flv'}

# if not os.path.exists(destination_folder):
#     os.makedirs(destination_folder)

# for current_dir, dirs, files in os.walk(source_root):
#     for file in files:
#         _, ext = os.path.splitext(file)
#         if ext.lower() in video_extensions:
#             source_path = os.path.join(current_dir, file)
#             dest_path = os.path.join(destination_folder, file)

#             base_name, ext = os.path.splitext(file)
#             counter = 1
#             while os.path.exists(dest_path):
#                 new_name = f"{base_name}_{counter}{ext}"
#                 dest_path = os.path.join(destination_folder, new_name)
#                 counter += 1

#             with open(source_path, 'rb') as fsrc:
#                 with open(dest_path, 'wb') as fdst:
#                     while True:
#                         buf = fsrc.read(1024 * 1024) # Корочь по 1 меби байту
#                         if not buf:
#                             break
#                         fdst.write(buf)

#             print(f"Скопировано: {source_path} -> {dest_path}")

# print("Завершено.")


# import requests


# req = requests.get("http://kslweb1.spb.ctf.su/second/level23/")
# s = req.text.split()
# for i in range(1337):
#     req = requests.get("http://kslweb1.spb.ctf.su/second/level23/", headers={"Cookie":s[16]})
#     s = req.text.split()
#     if i % 10 == 0:
#         print(i)
# print(s)


# import hashlib
# import itertools
# import string
# from datetime import datetime


# def brute_force_sha256(target_hash, max_length=5, chars=string.printable.strip()):
#     start_time = datetime.now()
#     print(f"Начало брутфорса SHA-256 в {start_time}")
#     print(f"Перебираем строки длиной до {max_length} символов")
#     print(f"Используемый набор символов: {chars}\n")

#     for length in range(1, max_length + 1):
#         print(f"Проверяем строки длиной {length}...")
#         for candidate in itertools.product(chars, repeat=length):
#             candidate = "".join(candidate)
#             candidate_hash = hashlib.sha256(candidate.encode("utf-8")).hexdigest()

#             if candidate_hash == target_hash:
#                 end_time = datetime.now()
#                 duration = end_time - start_time
#                 print(f"\nНайдено совпадение!")
#                 print(f"Исходная строка: {candidate}")
#                 print(f"Хэш SHA-256: {candidate_hash}")
#                 print(f"Время поиска: {duration}")
#                 return candidate

#         print(f"Перебор строк длиной {length} завершен. Совпадений не найдено.")

#     end_time = datetime.now()
#     duration = end_time - start_time
#     print(f"Общее время поиска: {duration}")
#     return None


# target_hash = "a21855da08cb102d1d217c53dc5824a3a795c1c1a44e971bf01ab9da3a2acbbf"
# brute_force_sha256(target_hash, max_length=25)
