# Task A: Dino the Pirate's Island Treasures

Legendary adventurer Dino discovered an ancient treasure map marking an archipelago of **n** islands. Each island hides a treasure of a certain value, but the islands are connected by dangerous underwater tunnels teeming with sea monsters.

Dino begins his journey on island **1** and wants to collect as many treasures as possible. However, due to an ancient pirate curse, each island can be visited **only once**. After visiting an island, the tunnel leading to it is magically sealed forever.

Dino can end his journey on any island — he doesn't necessarily have to return to the starting island.

Help Dino find the maximum total value of treasures he can collect!

## Input Format
The first line contains two integers **n** and **m** (1 ≤ n ≤ 20, 0 ≤ m ≤ n(n-1)/2) — the number of islands and the number of tunnels, respectively.

The second line contains **n** integers v₁, v₂, ..., vₙ (1 ≤ vᵢ ≤ 10⁶) — the treasure value on each island.

The following **m** lines each contain two integers **a** and **b** (1 ≤ a, b ≤ n, a ≠ b), indicating that a bidirectional tunnel exists between islands **a** and **b**.

## Output Format
Print a single integer — the maximum total treasure value Dino can collect.

## Notes
- **Example 1:** The islands form a cycle: 1-2-3-4-1. Dino can take the route 1 → 2 → 3 → 4, collecting treasures 10 + 30 + 20 + 5 = 65. This is the maximum possible sum as he visits all islands.
- **Example 2:** The graph consists of two separate components: islands {1, 2, 3} and islands {4, 5}. Dino starts at island 1 and can only reach islands 2 and 3. The optimal path is 1 → 2 → 3, collecting 100 + 50 + 75 = 225. Islands 4 and 5 are unreachable.
- **Example 3:** There are no tunnels, so Dino can only visit island 1, collecting 40 gold coins.
- **Example 4:** Dino can visit all islands in various ways. One optimal route: 1 → 6 → 5 → 2 → 3 → 4, collecting 15 + 65 + 55 + 25 + 35 + 45 = 240.
