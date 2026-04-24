# Yandex Interview

Real algorithmic problems from Yandex technical interviews — Python solutions with complexity analysis and approach justifications.

---

## Problems

### A — Dino the Pirate's Island Treasures
Find the maximum treasure value collectible by traversing a graph of n islands (n ≤ 20) starting from island 1, visiting each island at most once.

**Approach:** DP with bitmask (TSP variant) — `O(n · 2ⁿ)`  
**Why:** n ≤ 20 makes exponential complexity viable; bitmasking encodes visited state compactly.

---

### B — Dino's Vacation and Island Flooding
Given an n×m topographic grid, determine how many minutes until each land cell is flooded as water rises 1 m/min from all water cells simultaneously.

**Approach:** Multi-source Dijkstra (priority queue BFS) — `O(N·M · log(N·M))`  
**Why:** Flood time depends on both cell height and distance from water; Dijkstra handles variable-cost propagation correctly.

---

### C — Context Enrichment
Group N prompts such that prompts sharing at least one word merge into the same context (transitive). Output the number of contexts and the size of the largest one.

**Approach:** Disjoint Set Union (DSU) on word → prompt mapping — `O(total_words · α(N))`  
**Why:** DSU gives near-O(1) union/find; maps each word to the first prompt containing it for efficient overlap detection.

---

### D — Minimum Platform Destruction Time
For each platform i, find the minimum j−i where j > i, j has the same parity as i, and h[j] > h[i]. Output −1 if no such j exists.

**Approach:** Monotonic stack — two separate stacks for even/odd indices — `O(N)`  
**Why:** Standard "nearest greater element" pattern; splitting by parity maintains O(N) with no overhead.

---

### E — Datacenters
Given a connected graph, find the minimum number of edges to add so the graph becomes 2-edge-connected (survives any single cable failure). Output the pairs to connect.

**Approach:** Tarjan's bridge-finding + 2-edge-connected component compression → leaf pairing — `O(N + M)`  
**Why:** Compressing SCCs into a tree of components reduces the problem to counting and pairing leaves; `ceil(L/2)` new edges always suffice.

---

## Structure

```
Yandex_interview/
├── A_Dino_Pirate_Island_Treasures.py
├── B_Dino_Vacation_and_Island_Flooding.py
├── C_Context_Enrichment.py
├── D_Minimum_Platform_Destruction_Time.py
├── E_Datacenters.py
├── Task_A.md  ..  Task_E.md   # Full problem statements
├── Justification.md            # Approach rationale for all tasks
└── Interview_Prep.md           # Python internals Q&A (GIL, GC, async, MRO...)
```

---

## Author

- GitHub: [Shipovmax](https://github.com/Shipovmax)
- Email: shipov.max@icloud.com
