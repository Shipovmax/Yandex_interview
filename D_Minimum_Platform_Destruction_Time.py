import sys


def solve() -> None:
    """
    Solves Task D: Minimum Platform Destruction Time.
    Finds the nearest platform 'j' to the right of 'i' such that h[j] > h[i] and j has the same parity as i.
    Uses a monotonic stack approach for both even and odd indices to achieve O(N) time complexity.
    """
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        n = int(next(it))
        heights = [int(next(it)) for _ in range(n)]
    except (StopIteration, ValueError):
        return

    # Initialize results with -1 (not destroyed)
    destruction_times = [-1] * n

    # Separate stacks for even and odd index platforms
    even_stack: list[int] = []
    odd_stack: list[int] = []
    stacks = (even_stack, odd_stack)

    for current_idx, current_height in enumerate(heights):
        # Select the stack based on index parity
        stack = stacks[current_idx % 2]

        # While the current platform is higher than the platforms on the stack,
        # the current platform is the 'destroyer' for those on the stack.
        while stack and heights[stack[-1]] < current_height:
            previous_idx = stack.pop()
            destruction_times[previous_idx] = current_idx - previous_idx

        # Add the current platform to the stack to find its destroyer later
        stack.append(current_idx)

    # Print results as a single space-separated string
    sys.stdout.write(" ".join(map(str, destruction_times)) + "\n")


if __name__ == "__main__":
    solve()
