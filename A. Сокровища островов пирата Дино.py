import sys
from array import array


def solve() -> None:
    it = iter(map(int, sys.stdin.read().split()))
    try:
        n, m = next(it), next(it)
    except StopIteration:
        print(0)
        return

    val = [next(it) for _ in range(n)]

    # Смежность как битмаски: adj[v] имеет единицы на позициях соседей v
    adj = [0] * n
    for _ in range(m):
        a, b = next(it) - 1, next(it) - 1
        if a != b:
            adj[a] |= 1 << b
            adj[b] |= 1 << a

    # ДП по подмножествам: стартуем с вершины 0, она всегда в маске.
    # Компактизируем маску сдвигом вправо на 1 (бит 0 гарантированно = 1).
    if n == 0:
        print(0)
        return

    NEG = -1
    num = 1 << (n - 1)
    dp = array('i', [NEG]) * (num * n)

    def comp(mask: int) -> int:
        return mask >> 1  # убрать гарантированный младший бит

    start = 1  # посещён только остров 1 (индекс 0)
    dp[comp(start) * n + 0] = val[0]
    best = val[0]

    # dp[c * n + v] — лучшая сумма для компактной маски c и последней вершины v
    for c in range(num):
        mask = (c << 1) | 1
        base = c * n
        for v in range(n):
            cur = dp[base + v]
            if cur == NEG:
                continue
            if cur > best:
                best = cur
            free = adj[v] & ~mask  # соседи v, которых ещё нет в маске
            while free:
                bit = free & -free
                u = bit.bit_length() - 1
                nm = mask | bit
                pos = comp(nm) * n + u
                nv = cur + val[u]
                if nv > dp[pos]:
                    dp[pos] = nv
                free ^= bit

    print(best)


if __name__ == "__main__":
    solve()

# Подсказка для запуска из терминала VS Code/PowerShell вручную:
# после ввода всех строк нажмите Enter, затем Ctrl+Z и снова Enter — это завершит ввод (EOF).


