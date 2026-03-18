# Task D: Minimum Platform Destruction Time

**Time Limit:** 1 second
**Memory Limit:** 64 MB

Dino is running across a chain of **N** platforms numbered from 0 to **N−1**. Each platform **i** has a height **h[i]**. A platform **i** is destroyed if there exists a platform **j** (where **j > i**) that simultaneously satisfies two conditions:
1. **i** and **j** have the same parity (i % 2 == j % 2).
2. **h[j] > h[i]**.

The **destruction time** for platform **i** is the minimum value of (**j − i**) among all such suitable **j**. If no such platforms exist, the destruction time is considered **-1**.

Your task is to determine the destruction time for each platform.

## Input Format
- The first line contains an integer **N** (1 ≤ N ≤ 10⁵) — the number of platforms.
- The second line contains **N** integers h₀, h₁, ..., hₙ₋₁ (1 ≤ h[i] ≤ 10⁹) — the heights of the platforms.

## Output Format
Print **N** integers. The i-th number is the minimum destruction time for platform **i**, or **-1** if destruction is impossible.

## Example
**Input:**
```
6
5 3 8 1 7 9
```
**Output:**
```
2 4 -1 2 -1 -1
```
*Explanation:*
- Platform 0 (h=5, i=0): Nearest platform j > 0 with j%2 == 0 and h[j] > 5 is platform 2 (h=8, i=2). Time: 2-0 = 2.
- Platform 1 (h=3, i=1): Nearest platform j > 1 with j%2 == 1 and h[j] > 3 is platform 5 (h=9, i=5). Time: 5-1 = 4.
- Platform 2 (h=8, i=2): No platform j > 2 with j%2 == 0 and h[j] > 8 exists. Time: -1.
- Platform 3 (h=1, i=3): Nearest platform j > 3 with j%2 == 1 and h[j] > 1 is platform 5 (h=9, i=5). Time: 5-3 = 2.
- Platform 4 (h=7, i=4): No platform j > 4 with j%2 == 0 and h[j] > 7 exists. Time: -1.
- Platform 5 (h=9, i=5): No platform j > 5 exists. Time: -1.
