import sys


class DisjointSetUnion:
    """Класс системы непересекающихся множеств (DSU/Union-Find).

    Позволяет быстро объединять множества и находить представителя множества.
    Используются эвристики: сжатие путей и объединение по размеру.
    """
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        """Возвращает корень множества элемента x с сжатием путей."""
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> None:
        """Объединяет множества, содержащие a и b."""
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]


def main() -> None:
    data = sys.stdin.read().splitlines()
    if not data:
        return

    line_idx = 0
    n = int(data[line_idx].strip())
    line_idx += 1

    dsu = DisjointSetUnion(n)

    # Первая фаза: объединяем запросы, которые делят хотя бы одно слово.
    # Для каждого слова запоминаем индекс первого запроса, где оно встречалось.
    word_owner: dict[str, int] = {}

    for i in range(n):
        # строка с Mi — количеством слов в i-м запросе (можно не использовать напрямую)
        m = int(data[line_idx].strip())
        line_idx += 1
        # строка с самими словами
        words_line = data[line_idx] if line_idx < len(data) else ""
        line_idx += 1
        # Множество игнорирует повторы слов внутри одного запроса.
        words = set(words_line.split()) if m > 0 else set()

        for w in words:
            if w not in word_owner:
                word_owner[w] = i
            else:
                dsu.union(i, word_owner[w])

    # Вторая фаза: считаем число уникальных слов в каждой компоненте.
    comp_word_count: dict[int, int] = {}
    for w, idx in word_owner.items():
        root = dsu.find(idx)
        comp_word_count[root] = comp_word_count.get(root, 0) + 1

    # Считаем количество компонент по корням всех запросов.
    seen_roots = {dsu.find(i) for i in range(n)}
    num_components = len(seen_roots)

    # Размер наибольшего контекста — максимум количества уникальных слов в компоненте.
    max_size = 0
    for root in seen_roots:
        max_size = max(max_size, comp_word_count.get(root, 0))

    print(num_components, max_size)


if __name__ == "__main__":
    main()


