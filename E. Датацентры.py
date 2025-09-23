import sys


def find_bridges(num_vertices, edges_by_vertex, edges_count):
    sys.setrecursionlimit(1_000_000)

    time_in = [-1] * (num_vertices + 1)
    lowlink = [0] * (num_vertices + 1)
    visited = [False] * (num_vertices + 1)
    # Массив отметок «мост/не мост» по id ребра
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


def build_components(num_vertices, edges_by_vertex, is_bridge, is_bridge_endpoint):
    component_of = [0] * (num_vertices + 1)

    sys.setrecursionlimit(1_000_000)

    def dfs_assign(start: int, comp_id: int) -> tuple[int, int]:
        # Возвращает (любой представитель, представитель не-«мостовой» если есть)
        stack = [start]
        component_of[start] = comp_id
        any_rep = start
        non_bridge_rep = 0
        if not is_bridge_endpoint[start]:
            non_bridge_rep = start
        while stack:
            v = stack.pop()
            for to, eid in edges_by_vertex[v]:
                if is_bridge[eid]:
                    continue
                if component_of[to] == 0:
                    component_of[to] = comp_id
                    if non_bridge_rep == 0 and not is_bridge_endpoint[to]:
                        non_bridge_rep = to
                    stack.append(to)
        return any_rep, non_bridge_rep

    comp_count = 0
    rep_any = {}
    rep_safe = {}
    for v in range(1, num_vertices + 1):
        if component_of[v] == 0:
            comp_count += 1
            a, b = dfs_assign(v, comp_count)
            rep_any[comp_count] = a
            rep_safe[comp_count] = b if b != 0 else a

    return comp_count, component_of, rep_safe


def pair_leaves(leaf_representatives):
    pairs = []
    leaf_count = len(leaf_representatives)
    if leaf_count == 0:
        return pairs
    # Более устойчивое парное соединение: разбиваем список на две половины
    # и соединяем попарно элементы из 1-й и 2-й половин.
    # Это снижает шанс напечатать конец одного и того же мостового ребра.
    half = (leaf_count + 1) // 2
    for i in range(leaf_count // 2):
        pairs.append((leaf_representatives[i], leaf_representatives[i + half]))
    if leaf_count % 2 == 1:
        # Остался один лист — замыкаем его с первым из второй половины
        pairs.append((leaf_representatives[-1], leaf_representatives[half - 1]))
    return pairs


data = sys.stdin.buffer.read().split()
if not data:
    # No input provided
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

# 1) Найти мосты
bridges = find_bridges(n, adj, m)

# Пометим вершины, являющиеся концами мостов — их по возможности лучше не
# использовать в качестве представителей компонент, чтобы не напечатать
# существующее ребро.
is_bridge_endpoint = [False] * (n + 1)
for eid in range(m):
    if bridges[eid]:
        is_bridge_endpoint[edge_u[eid]] = True
        is_bridge_endpoint[edge_v[eid]] = True

# 2) Сжать граф по немостовым рёбрам в 2‑рёберно‑связные компоненты
comp_count, comp_of, representative = build_components(n, adj, bridges, is_bridge_endpoint)

# 3) Построить дерево компонент по мостам и посчитать листья
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


