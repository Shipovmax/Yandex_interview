# Task E: Datacenters

**Time Limit:** 2 seconds
**Memory Limit:** 256 MB

## Description
A company has a network of datacenters. Some pairs of datacenters are connected by cables, allowing them to exchange messages. If datacenters are not connected directly, they communicate through a chain of intermediate datacenters.

The goal is to increase fault tolerance: after any **SINGLE** cable failure, the network must remain connected (any two datacenters must still be reachable). You are allowed to lay new cables between any two datacenters that do not already have a direct connection. You must do this using the minimum number of new cables. It is guaranteed that the initial network is connected and contains no multiple edges.

## Input Format
1. The first line contains two integers **n** and **k** (3 ≤ n ≤ 10⁵, n−1 ≤ k ≤ 10⁵) — the number of datacenters and the number of existing connections.
2. The following **k** lines each contain two integers **i** and **j**, indicating a cable exists between datacenter **i** and **j**.

## Output Format
1. Print an integer **t** — the minimum number of new connections required.
2. In the following **t** lines, print the pairs of datacenter IDs to be connected by additional cables.

## Hint
If you "compress" all non-bridge edges, you will get a tree of 2-edge-connected components. Let **L** be the number of leaf components in this tree. The minimum number of new cables required is **ceil(L / 2)**. It is sufficient to pair up representatives of these leaf components.

## Example
**Input:**
```
3 2
1 2
2 3
```
**Output:**
```
1
1 3
```
*Explanation:* The original network is a chain 1-2-3. Connecting 1 and 3 creates a cycle, making the network 2-edge-connected.
