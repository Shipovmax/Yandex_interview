import sys


class DisjointSetUnion:
    
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> None:
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

    word_owner: dict[str, int] = {}

    for i in range(n):
        m = int(data[line_idx].strip())
        line_idx += 1
        words_line = data[line_idx] if line_idx < len(data) else ""
        line_idx += 1
        words = set(words_line.split()) if m > 0 else set()

        for w in words:
            if w not in word_owner:
                word_owner[w] = i
            else:
                dsu.union(i, word_owner[w])

    comp_word_count: dict[int, int] = {}
    for w, idx in word_owner.items():
        root = dsu.find(idx)
        comp_word_count[root] = comp_word_count.get(root, 0) + 1

    seen_roots = set()
    for i in range(n):
        seen_roots.add(dsu.find(i))
    num_components = len(seen_roots)

    max_size = 0
    for root in seen_roots:
        max_size = max(max_size, comp_word_count.get(root, 0))

    print(num_components, max_size)


if __name__ == "__main__":
    main()


