# Justification of the Decision

Below is a brief rationale for the approaches chosen for the .py files in this repository.
Priorities: correctness, linear/quasi-linear complexity, and readability.

## A. Dino the Pirate's Island Treasures
- **Idea:** Dynamic Programming with Bitmasking (Variation of TSP).
- **Why:** Given the constraints (n ≤ 20), an exponential complexity like O(n * 2ⁿ) is acceptable and necessary to find the optimal path in a general graph where each node can be visited only once.
- **Trade-offs:** Uses bitwise operations for efficiency and `array` for memory management.

## B. Dino's Vacation and Island Flooding
- **Idea:** Multi-source Dijkstra-like BFS for flooding time.
- **Why:** BFS/Dijkstra is the natural way to calculate the time it takes for water to reach a cell, especially when the "arrival time" depends on both the cell's height and the neighbor's flood time. Complexity is O(N*M log(N*M)).
- **Trade-offs:** Uses a priority queue to handle varying terrain heights.

## C. Context Enrichment
- **Idea:** Disjoint Set Union (DSU) for grouping prompts by word overlap.
- **Why:** DSU provides near-constant time operations for union and find, making it perfect for grouping connected components based on shared elements (words). Complexity is O(Total Words * α(N)).
- **Trade-offs:** Maps words to prompt indices to efficiently identify overlaps.

## D. Minimum Platform Destruction Time
- **Idea:** Monotonic Stack (separate for even and odd indices).
- **Why:** A monotonic stack is the standard way to find the "nearest larger element" in O(N) time. Since parity is a constraint, splitting the problem into two stacks (even/odd) maintains the O(N) complexity.
- **Trade-offs:** Minimal memory overhead, single-pass processing.

## E. Datacenters
- **Idea:** Tarjan's Bridge-finding algorithm + 2-edge-connected components.
- **Why:** To make a graph 2-edge-connected with minimum edges, we must connect the leaves of the component tree. Tarjan's algorithm finds bridges in O(N+M), and pairing leaves is a proven optimal strategy.
- **Trade-offs:** Uses recursion for DFS (with increased limit) and iterative BFS for component assignment to handle large graphs safely.
