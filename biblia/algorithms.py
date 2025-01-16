class mathBib:
    def ceil(n):
        return int(-1 * n // 1 * -1)

    def sqrt(n):
        return pow(n, 0.5)

    def sieveFeratosthenes(n):
        sieve = list(range(n + 1))
        sieve[1] = 0  # без этой строки итоговый список будет содержать единицу
        for i in sieve:
            if i > 1:
                for j in range(2 * i, len(sieve), i):
                    sieve[j] = 0
        return sieve

    def prefixSum(self):
        output = [0]
        for _ in self:
            output.append(output[-1] + _)
        return output


class GcdAndLcm:
    def gcd(a, b):
        return GcdAndLcm.gcd(b, a % b) if b > 0 else a

    def lcm(a, b):
        def gcd(a, b):
            return gcd(b, a % b) if b > 0 else a

        return (a * b) / gcd(a, b)


class search:
    def binary_search_iterative(array, element):  # Бинарный_поиск
        mid = 0
        start = 0
        end = len(array)
        step = 0

        while start <= end:
            print("Subarray in step {}: {}".format(step, str(array[start : end + 1])))
            step = step + 1
            mid = (start + end) // 2

            if element == array[mid]:
                return mid

            if element < array[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1

    def binary_search_recursive(
        array, element, start, end
    ):  # Бинарный_поиск_Рекурсивный
        if start > end:
            return -1

        mid = (start + end) // 2
        if element == array[mid]:
            return mid

        if element < array[mid]:
            return search.binary_search_recursive(array, element, start, mid - 1)
        else:
            return search.binary_search_recursive(array, element, mid + 1, end)


class deleted:
    def deleteDub(
        sp, sp1
    ):  # добавление элементов без дублирования и уничтожения порядка
        [sp1.append(item) for item in sp if item not in sp1]
        return sp1

    def DeleteNotDuble(arr: list):
        vh = []
        for i in range(len(arr) - 1, 0 - 1, -1):
            if arr[i] not in vh:
                vh.append(arr[i])
        return vh[::-1]


class NumberMath:
    def catalan(n):  # Числа_Каталана
        if n < 2:
            return 1
        else:
            ans = ((2 * ((2 * n) - 1)) / (n + 1)) * NumberMath.catalan(n - 1)
            return int(ans)

    def fib(n):  # Числа_Фибоночи_вычисление_n_фибоначи
        dp = [1, 1, 2]
        for i in range(3, n):
            dp.append(dp[i - 1] + dp[i - 2])
        return dp[n - 1]

    def tribonacci(limit):  # Числа_трибоначи_Вычисление_n-ого_трибаночи
        end_tribonacci = [0, 1, 1]
        for _ in range(limit - 1):
            end_tribonacci.append(sum(end_tribonacci[-3:]))
        print(end_tribonacci[-1])


class sorting:  # Сортировки
    def merge_sorting(arr):  # Сортировка_Слиянием
        def merge(a, b):
            res = []
            i = 0
            j = 0
            while i < len(a) and j < len(b):
                if a[i] >= b[j]:
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

    def counting_sort(a):  # Сортировка_подсчётом
        cnt = [0] * 10
        for el in a:
            cnt[el] += 1
        a = []
        for d in range(len(cnt)):
            a += [d] * cnt[d]
        return a

    def bubble_sort(a):  # Сортировка_пузырьком
        unordered = True
        n = len(a)
        z = 0
        while unordered:
            unordered = False
            for j in range(n - 1, z, -1):
                if (
                    a[j] < a[j - 1]
                ):  # Меняя знак, меняется и порядок. т.е. сортировка по убыванию/по возрастанию
                    a[j], a[j - 1] = a[j - 1], a[j]
                    unordered = True
            z += 1

    def selection_sort(a):  # Сортировка_Выбором
        for i in range(len(a) - 1):
            imin = i
            for j in range(i + 1, len(a)):
                if a[j] < a[imin]:
                    imin = j
            a[i], a[imin] = a[imin], a[i]

    def insertion_sort(a):  # Cортировка_вставками
        for i in range(1, len(a)):
            tmp = a[i]
            j = i - 1
            while j >= 0 and a[j] > tmp:
                a[j + 1] = a[j]
                j -= 1
            a[j + 1] = tmp


class graphWork:
    def bfs(graph, node):
        import queue

        visited, q, space = set(), queue.Queue(), [node]
        visited.add(node)
        q.put(node)
        while not q.empty():
            vertex = q.get()
            for neighbour in graph[vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    q.put(neighbour)
                    space.append(neighbour)
        return space
        # graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}

    def dijkstra(graph, start, n):
        import heapq

        distances = {i: float("infinity") for i in range(1, n + 1)}
        distances[start] = 0
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in graph[current_vertex].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances
        # graph = {
        #     'A': {'B': 1, 'C': 4},
        #     'B': {'A': 1, 'C': 2, 'D': 5},
        #     'C': {'A': 4, 'B': 2, 'D': 1},
        #     'D': {'B': 5, 'C': 1}
        # }

    def dfs(visited, graph, node):
        if node not in visited:
            print(node)
            visited.add(node)
            for neighbour in graph[node]:
                graphWork.dfs(visited, graph, neighbour)

    # def graph = {
    # '5' : ['3','7'],
    # '3' : ['2', '4'],
    # '7' : ['8'],
    # '2' : [],
    # '4' : ['8'],
    # '8' : []
    # }
    # visited = set() # Set to keep track of visited nodes of graph.
