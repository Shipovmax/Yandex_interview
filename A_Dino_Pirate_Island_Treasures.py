import sys
from array import array


def solve() -> None:
    """
    Solves the 'Dino the Pirate's Island Treasures' problem using Dynamic Programming with Bitmasking.
    The goal is to find the maximum total value collected starting from island 1,
    visiting each island at most once.

    Complexity: O(n^2 * 2^n) time (2^(n-1) masks, each expanding into up to n
    states, each state scanning up to n neighbor bits) and O(n * 2^n) space
    (the DP table has one entry per (mask, last_island) pair).
    """
    it = iter(map(int, sys.stdin.read().split()))
    try:
        n, m = next(it), next(it)
    except StopIteration:
        return

    # Island treasure values
    values = [next(it) for _ in range(n)]

    # Adjacency matrix represented by bitmasks for efficiency
    adj = [0] * n
    for _ in range(m):
        u, v = next(it) - 1, next(it) - 1
        if u != v:
            adj[u] |= 1 << v
            adj[v] |= 1 << u

    if n == 0:
        print(0)
        return

    # Constant to represent unvisited state
    UNVISITED = -1
    # We only care about masks that include the starting island (island 0)
    # Mask format: bit 0 is always 1. Total states: (2^(n-1)) * n
    num_masks = 1 << (n - 1)
    dp = array("i", [UNVISITED]) * (num_masks * n)

    def get_dp_index(mask: int, last_island: int) -> int:
        # Since bit 0 is always 1, we can right shift to save space
        return (mask >> 1) * n + last_island

    # Initial state: starting at island 0
    start_mask = 1
    dp[get_dp_index(start_mask, 0)] = values[0]
    max_treasure = values[0]

    # Iterate through all possible masks (combinations of visited islands)
    for c in range(num_masks):
        mask = (c << 1) | 1
        base_idx = c * n
        for v in range(n):
            current_total = dp[base_idx + v]
            if current_total == UNVISITED:
                continue

            # Update overall maximum
            if current_total > max_treasure:
                max_treasure = current_total

            # Try moving to an unvisited adjacent island
            neighbors_to_visit = adj[v] & ~mask
            while neighbors_to_visit:
                # Get the lowest set bit
                bit = neighbors_to_visit & -neighbors_to_visit
                u = bit.bit_length() - 1

                new_mask = mask | bit
                new_pos = get_dp_index(new_mask, u)
                new_value = current_total + values[u]

                if new_value > dp[new_pos]:
                    dp[new_pos] = new_value

                # Remove the bit we just processed
                neighbors_to_visit ^= bit

    print(max_treasure)


if __name__ == "__main__":
    solve()
