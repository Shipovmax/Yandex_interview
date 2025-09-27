import sys


def find_bridges(num_vertices, edges_by_vertex, edges_count):
    sys.setrecursionlimit(1_000_000)

    time_in = [-1] * (num_vertices + 1)
    lowlink = [0] * (num_vertices + 1)
    visited = [False] * (num_vertices + 1)
    is_bridge = [False] * edges_count

    time_counter = 0

    def dfs(vertex: int, parent_edge_id: int) -> None:
        nonlocal time_counter
        visited[vertex] = True
        time_in[vertex] = lowlink[vertex] = time_counter
        time_counter += 1
        for neighbour, eid in edges_by_vertex[vertex]:
            if eid == parent_edge_id:
                continue
            if visited[neighbour]:
                # Обратное ребро (вверх по дереву) — обновляем lowlink
                lowlink[vertex] = min(lowlink[vertex], time_in[neighbour])
            else:
                dfs(neighbour, eid)
                lowlink[vertex] = min(lowlink[vertex], lowlink[neighbour])
                if lowlink[neighbour] > time_in[vertex]:
                    is_bridge[eid] = True

    for v in range(1, num_vertices + 1):
        if not visited[v]:
            dfs(v, -1)

    return is_bridge


def build_components(num_vertices, edges_by_vertex, is_bridge):
    component_of = [0] * (num_vertices + 1)

    sys.setrecursionlimit(1_000_000)

    def dfs_assign(start: int, comp_id: int) -> None:
        stack = [start]
        component_of[start] = comp_id
        while stack:
            v = stack.pop()
            for to, eid in edges_by_vertex[v]:
                if is_bridge[eid]:
                    continue
                if component_of[to] == 0:
                    component_of[to] = comp_id
                    stack.append(to)

    comp_count = 0
    reps = {}
    for v in range(1, num_vertices + 1):
        if component_of[v] == 0:
            comp_count += 1
            reps[comp_count] = v
            dfs_assign(v, comp_count)

    return comp_count, component_of, reps


def pair_leaves(leaf_representatives):
    pairs = []
    leaf_count = len(leaf_representatives)
    if leaf_count == 0:
        return pairs
    for i in range(0, leaf_count // 2):
        a = leaf_representatives[2 * i]
        b = leaf_representatives[2 * i + 1]
        pairs.append((a, b))
    if leaf_count % 2 == 1:
        pairs.append((leaf_representatives[-1], leaf_representatives[0]))
    return pairs


data = sys.stdin.buffer.read().split()
if not data:
    print(0)
    sys.exit(0)

it = iter(map(int, data))
n = next(it)
m = next(it)

edge_u = [0] * m
edge_v = [0] * m

adj = [[] for _ in range(n + 1)]
for idx in range(m):
    u = next(it)
    v = next(it)
    edge_u[idx] = u
    edge_v[idx] = v
    adj[u].append((v, idx))
    adj[v].append((u, idx))

bridges = find_bridges(n, adj, m)

comp_count, comp_of, representative = build_components(n, adj, bridges)

if comp_count == 1:
    print(0)
    sys.exit(0)

degree = [0] * (comp_count + 1)
for eid in range(m):
    if not bridges[eid]:
        continue
    cu = comp_of[edge_u[eid]]
    cv = comp_of[edge_v[eid]]
    if cu == cv:
        continue
    degree[cu] += 1
    degree[cv] += 1

leaf_reps = [representative[i] for i in range(1, comp_count + 1) if degree[i] == 1]

pairs = pair_leaves(leaf_reps)

print(len(pairs))
for a, b in pairs:
    print(a, b)


