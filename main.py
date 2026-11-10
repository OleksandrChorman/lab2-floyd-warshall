import math

INF = math.inf


# --- 1. Готові тестові матриці ---

TESTS = {
    1: [
        [0, INF, INF, INF, INF, INF, INF],
        [1, 0, -1, 5, INF, INF, INF],
        [2, 4, 0, 3, INF, -2, 6],
        [7, 8, -4, 0, INF, INF, INF],
        [INF, 10, INF, 11, 0, INF, 9],
        [12, INF, 13, INF, 14, 0, INF],
        [-5, 15, INF, -6, INF, 16, 0]
    ],
    2: [
        [0, INF, 1, INF, 3, INF, 4],
        [INF, 0, INF, 5, INF, INF, INF],
        [2, INF, 0, INF, INF, -2, 6],
        [7, 8, INF, 0, INF, INF, INF],
        [INF, 10, INF, 11, 0, INF, 9],
        [12, INF, 13, INF, INF, 0, INF],
        [-3, 14, INF, -1, INF, INF, 0]
    ],
    3: [
        [0, INF, 1, INF, 15, INF, INF],
        [INF, 0, -1, 3, INF, 4, INF],
        [2, INF, 0, -2, INF, INF, 6],
        [7, 8, 5, 0, INF, INF, INF],
        [INF, 10, INF, 11, 0, INF, 9],
        [12, INF, 13, INF, 14, 0, INF],
        [15, INF, INF, -6, INF, -3, 0]
    ],
    4: [
        [0, INF, 1, INF, 3, INF, 4],
        [2, 0, INF, 5, INF, INF, INF],
        [-2, INF, 0, INF, INF, -2, 6],
        [INF, 8, INF, 0, INF, INF, INF],
        [INF, INF, INF, 7, 0, INF, 9],
        [11, INF, 12, INF, INF, 0, INF],
        [INF, -4, INF, -1, INF, 10, 0]
    ],
    5: [
        [0, 1, 2, 7, INF, 12, INF],
        [INF, 0, -1, 5, INF, INF, INF],
        [INF, INF, 0, 3, INF, 4, 6],
        [INF, 8, -4, 0, INF, INF, INF],
        [INF, 10, INF, 11, 0, INF, 9],
        [INF, INF, 13, INF, 14, 0, INF],
        [-5, 15, INF, -6, INF, 16, 0]
    ],
    6: [
        [0, 2, -5, INF, INF, INF, 4],
        [1, 0, INF, 5, INF, INF, INF],
        [3, INF, 0, INF, INF, -2, 6],
        [7, 8, INF, 0, INF, INF, -4],
        [INF, -1, INF, 11, 0, INF, 9],
        [10, INF, 12, INF, INF, 0, INF],
        [-3, INF, INF, INF, INF, INF, 0]
    ],
    7: [
        [0, INF, INF, INF, INF, INF, INF],
        [INF, 0, 5, INF, INF, INF, INF],
        [2, INF, 0, INF, INF, -2, 6],
        [7, 8, INF, 0, INF, INF, INF],
        [INF, 10, INF, INF, 0, INF, 9],
        [12, INF, 13, INF, INF, 0, INF],
        [-5, 15, INF, -6, INF, INF, 0]
    ],
    8: [
        [0, INF, 1, INF, 3, INF, 4],
        [INF, 0, INF, INF, INF, INF, INF],
        [2, INF, 0, INF, INF, -2, 6],
        [7, 8, INF, 0, INF, INF, INF],
        [INF, 10, INF, 11, 0, INF, 9],
        [INF, INF, INF, INF, INF, 0, INF],
        [-3, 14, INF, -1, INF, INF, 0]
    ],
    9: [
        [0, INF, 1, INF, 3, INF, 4],
        [INF, 0, 2, 5, INF, 7, INF],
        [INF, 12, 0, INF, INF, -2, 6],
        [INF, 8, INF, 0, 13, INF, INF],
        [INF, 10, INF, 11, 0, -3, 9],
        [INF, INF, INF, INF, INF, 0, INF],
        [INF, 14, INF, -1, INF, INF, 0]
    ],
    10: [
        [0, INF, INF, INF, 3, INF, 4],
        [INF, 0, -1, INF, INF, INF, INF],
        [2, 5, 0, INF, 8, -2, 6],
        [7, INF, 12, 0, INF, 11, INF],
        [INF, 1, INF, 10, 0, INF, 9],
        [INF, INF, INF, -4, INF, 0, INF],
        [8, INF, -3, 10, INF, INF, 0]
    ]
}


# --- 2. Форматування значень ---

def format_value(value):
    if value == INF:
        return "∞"

    if value == -INF:
        return "-∞"

    if value == int(value):
        return str(int(value))

    return f"{value:.2f}"


# --- 3. Виведення матриці мінімальних відстаней ---

def print_matrix(matrix, title, affected=None):
    print(f"\n--- {title} ---")

    n = len(matrix)

    print("    " + "".join(f"{j + 1:>6}" for j in range(n)))

    for i in range(n):
        row_str = f"{i + 1:>2} |"

        for j in range(n):
            if affected is not None and affected[i][j]:
                val = f"{'-∞':>6}"
            else:
                val = f"{format_value(matrix[i][j]):>6}"

            row_str += val

        print(row_str)


# --- 4. Виведення матриці NEXT ---

def print_next_matrix(nxt, title, affected, dist):
    print(f"\n--- {title} ---")

    n = len(nxt)

    print("    " + "".join(f"{j + 1:>6}" for j in range(n)))

    for i in range(n):
        row_str = f"{i + 1:>2} |"

        for j in range(n):

            if affected[i][j]:
                value = "-∞"

            elif dist[i][j] == INF or nxt[i][j] is None:
                value = "—"

            else:
                # Перетворення індексу Python на номер вершини
                value = str(nxt[i][j] + 1)

            row_str += f"{value:>6}"

        print(row_str)


# --- 5. Алгоритм Флойда-Уоршелла ---

def floyd_warshall(matrix):

    n = len(matrix)

    # Копія початкової матриці відстаней
    dist = [row[:] for row in matrix]

    # Матриця наступних вершин NEXT
    nxt = [[None] * n for _ in range(n)]

    # Початкова ініціалізація NEXT
    for i in range(n):
        for j in range(n):

            if i == j:
                nxt[i][j] = i

            elif dist[i][j] != INF:
                nxt[i][j] = j

    # Три вкладені цикли алгоритму
    for k in range(n):

        for i in range(n):

            if dist[i][k] == INF:
                continue

            for j in range(n):

                if dist[k][j] == INF:
                    continue

                candidate = dist[i][k] + dist[k][j]

                if candidate < dist[i][j]:

                    dist[i][j] = candidate

                    # Записуємо наступну вершину маршруту
                    nxt[i][j] = nxt[i][k]

    # Перевірка негативних циклів
    negative_vertices = [
        k for k in range(n) if dist[k][k] < 0
    ]

    affected = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):

            for k in negative_vertices:

                if dist[i][k] != INF and dist[k][j] != INF:

                    affected[i][j] = True
                    break

    return dist, nxt, affected, negative_vertices


# --- 6. Відновлення маршруту ---

def restore_path(i, j, nxt, dist, affected):

    if affected[i][j]:
        return "-∞"

    if dist[i][j] == INF or nxt[i][j] is None:
        return "Маршруту немає"

    if i == j:
        return str(i + 1)

    path = [i + 1]
    current = i

    # Послідовне відновлення маршруту
    for _ in range(len(nxt) + 1):

        current = nxt[current][j]

        if current is None:
            return "Помилка"

        path.append(current + 1)

        if current == j:
            return " -> ".join(str(v) for v in path)

    return "Помилка"


# --- 7. Головне меню ---

def main():

    print("=" * 55)
    print("АЛГОРИТМ ФЛОЙДА-УОРШЕЛЛА (Лабораторна робота №2)")
    print("=" * 55)

    while True:

        print("\nОберіть дію:")
        print("1. Використати готовий тест з Додатку 2 (Тести 1-10)")
        print("2. Ввести матрицю вручну")
        print("3. Вийти")

        choice = input("Ваш вибір (1-3): ").strip()

        if choice == "3":
            print("До побачення!")
            break

        matrix = None

        # Вибір готового тесту
        if choice == "1":

            while True:
                try:

                    test_num = int(input("Введіть номер тесту (1-10): "))

                    if test_num in TESTS:

                        matrix = [row[:] for row in TESTS[test_num]]

                        print(
                            f"\nЗавантажено Тест {test_num} (7 вершин)."
                        )

                        break

                    else:
                        print("Помилка: тест має бути від 1 до 10.")

                except ValueError:
                    print("Помилка: введіть ціле число.")

        # Ручне введення матриці
        elif choice == "2":

            while True:
                try:

                    n = int(input("Введіть кількість вершин (1-20): "))

                    if 1 <= n <= 20:
                        break

                    print("Розмір має бути від 1 до 20.")

                except ValueError:
                    print("Введіть ціле число.")

            print(
                "Введіть матрицю по рядках (використовуйте INF для ∞):"
            )

            matrix = []

            for i in range(n):

                while True:
                    try:

                        row_input = input(
                            f"Рядок {i + 1}: "
                        ).split()

                        if len(row_input) != n:
                            raise ValueError(
                                f"Потрібно {n} значень."
                            )

                        row = []

                        for x in row_input:

                            if x.lower() in ("inf", "∞", "x"):
                                row.append(INF)

                            else:
                                row.append(float(x))

                        if row[i] != 0:
                            raise ValueError(
                                "На діагоналі мають бути нулі!"
                            )

                        matrix.append(row)
                        break

                    except ValueError as e:
                        print(
                            f"Помилка: {e}. Спробуйте ще раз."
                        )

        else:
            print("Невірний вибір.")
            continue

        # --- Обчислення ---

        print("\nОбчислення...")

        # Зберігаємо початкову матрицю
        original_matrix = [row[:] for row in matrix]

        # Запуск алгоритму
        dist, nxt, affected, neg_vertices = floyd_warshall(matrix)

        if neg_vertices:

            print(
                "\nУВАГА: Виявлено негативний цикл "
                f"у вершинах: {[v + 1 for v in neg_vertices]}"
            )

        # Перша матриця: початкові ваги ребер
        print_matrix(
            original_matrix,
            "Початкова матриця"
        )

        # Друга матриця: мінімальні відстані
        print_matrix(
            dist,
            "Матриця мінімальних відстаней",
            affected
        )

        # Третя матриця за змістом результатів:
        # NEXT — наступна вершина для переходу
        print_next_matrix(
            nxt,
            "Матриця найкоротших шляхів (NEXT)",
            affected,
            dist
        )

        n = len(matrix)

        # --- Пошук маршруту для окремої пари ---

        print(
            "\nБажаєте знайти шлях для конкретної пари вершин?"
        )

        ans = input("(так/ні): ").strip().lower()

        if ans in ("так", "т", "yes", "y"):

            while True:
                try:

                    start = int(
                        input(f"Початкова вершина (1-{n}): ")
                    )

                    end = int(
                        input(f"Кінцева вершина (1-{n}): ")
                    )

                    if 1 <= start <= n and 1 <= end <= n:
                        break

                    print("Номери мають бути в межах.")

                except ValueError:
                    print("Введіть цілі числа.")

            i, j = start - 1, end - 1

            print(
                f"\nНайкоротший шлях з {start} до {end}:"
            )

            print(
                f"Маршрут: {restore_path(i, j, nxt, dist, affected)}"
            )

            if affected[i][j]:

                print("Відстань: -∞")

            else:

                print(
                    f"Відстань: {format_value(dist[i][j])}"
                )

        print("\n" + "=" * 55)


if __name__ == "__main__":
    main()