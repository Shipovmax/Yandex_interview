import sys
from heapq import heappush, heappop


def main() -> None:
    # Быстрый ввод всех чисел одним куском
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)

    grid = [[0] * m for _ in range(n)]
    for i in range(n):
        row = grid[i]
        for j in range(m):
            try:
                row[j] = next(it)
            except StopIteration:
                row[j] = 0

    INF = 10 ** 20
    dist = [[INF] * m for _ in range(n)]
    heap = []

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                dist[i][j] = 0
                heappush(heap, (0, i, j))

    # Если на карте нет воды (нулей), то для устойчивости решению
    # просто выведем высоты как времена затопления.
    # (В рамках оригинальной задачи обычно гарантируется наличие воды.)
    if not heap:
        out_lines = [" ".join(map(str, row)) for row in grid]
        sys.stdout.write("\n".join(out_lines))
        return

    # Мульти-источник Дейкстры.
    # Интерпретация:
    #  для каждой клетки ищем минимально возможный максимум высоты
    #  на пути от воды до неё. Время затопления равно этому максимуму.
    heappush_local = heappush
    heappop_local = heappop
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

    while heap:
        cur_t, x, y = heappop_local(heap)
        # Просроченная запись из кучи — пропускаем
        if cur_t != dist[x][y]:
            continue
        # Локальные ссылки — читаемее и немного быстрее в цикле
        grid_local = grid
        dist_local = dist
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                # Вода приходит тогда, когда уровень достигнет:
                #  max(текущее_время, высота_соседа)
                nt = max(cur_t, grid_local[nx][ny])
                if nt < dist_local[nx][ny]:
                    dist_local[nx][ny] = nt
                    heappush_local(heap, (nt, nx, ny))

    out_lines = [" ".join(map(str, dist[i])) for i in range(n)]
    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    main()
