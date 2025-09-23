import sys


def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    heights = [int(next(it)) for _ in range(n)]

    # Ответы по умолчанию — −1 (если подходящей платформы справа нет)
    answers = [-1] * n

    # Две монотонные убывающие по высоте стека для каждой чётности индекса:
    # even_stack — для чётных i, odd_stack — для нечётных i.
    even_stack: list[int] = []
    odd_stack: list[int] = []
    stacks = (even_stack, odd_stack)

    for idx, h in enumerate(heights):
        # Выбираем стек по чётности индекса (0 — чётный, 1 — нечётный)
        stack = stacks[idx & 1]

        # Текущая платформа j «разрушает» все предыдущие меньшие по высоте
        # платформы той же чётности. Для них j — ближайший справа больший.
        while stack and heights[stack[-1]] < h:
            i = stack.pop()
            answers[i] = idx - i

        # Текущая платформа становится кандидатом для следующих слева
        stack.append(idx)

    sys.stdout.write(" ".join(map(str, answers)))


if __name__ == "__main__":
    solve()
