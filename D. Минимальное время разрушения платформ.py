import sys


def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    heights = [int(next(it)) for _ in range(n)]

    answers = [-1] * n

    even_stack: list[int] = []
    odd_stack: list[int] = []
    stacks = (even_stack, odd_stack)

    for idx, h in enumerate(heights):
        stack = stacks[idx & 1]

        while stack and heights[stack[-1]] < h:
            i = stack.pop()
            answers[i] = idx - i

        stack.append(idx)

    sys.stdout.write(" ".join(map(str, answers)))


if __name__ == "__main__":
    solve()
