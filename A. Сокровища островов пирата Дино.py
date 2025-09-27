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

    adj = [0] * n
    for _ in range(m):
        a, b = next(it) - 1, next(it) - 1
        if a != b:
            adj[a] |= 1 << b
            adj[b] |= 1 << a

    if n == 0:
        print(0)
        return

    NEG = -1
    num = 1 << (n - 1)
    dp = array('i', [NEG]) * (num * n)

    def comp(mask: int) -> int:
        return mask >> 1  

    start = 1  
    dp[comp(start) * n + 0] = val[0]
    best = val[0]

    for c in range(num):
        mask = (c << 1) | 1
        base = c * n
        for v in range(n):
            cur = dp[base + v]
            if cur == NEG:
                continue
            if cur > best:
                best = cur
            free = adj[v] & ~mask  
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

# Enter after Ctrl+Z after Enter — completing the input


