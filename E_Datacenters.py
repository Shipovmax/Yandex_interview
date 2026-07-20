import sys

# Increase recursion depth for deep DFS trees in large networks
sys.setrecursionlimit(200_000)


def find_bridges(
    num_vertices: int, adj: list[list[tuple[int, int]]], num_edges: int
) -> list[bool]:
    """
    Finds all bridges in the graph using Tarjan's bridge-finding algorithm.
    Returns a boolean list where True indicates the edge with that index is a bridge.

    Complexity: O(V + E) time and space — a single DFS visits every vertex
    once and every edge twice (once from each endpoint).
    """
    time_in = [-1] * (num_vertices + 1)
    lowlink = [0] * (num_vertices + 1)
    is_bridge = [False] * num_edges
    timer = 0

    def dfs(u: int, p_edge_id: int = -1) -> None:
        nonlocal timer
        time_in[u] = lowlink[u] = timer
        timer += 1
        for v, edge_id in adj[u]:
            if edge_id == p_edge_id:
                continue
            if time_in[v] != -1:
                # Back-edge found: update lowlink using entry time of ancestor
                lowlink[u] = min(lowlink[u], time_in[v])
            else:
                # Tree-edge: recurse and update lowlink based on child's lowlink
                dfs(v, edge_id)
                lowlink[u] = min(lowlink[u], lowlink[v])
                if lowlink[v] > time_in[u]:
                    is_bridge[edge_id] = True

    for i in range(1, num_vertices + 1):
        if time_in[i] == -1:
            dfs(i)

    return is_bridge


def get_2_edge_connected_components(
    num_vertices: int, adj: list[list[tuple[int, int]]], is_bridge: list[bool]
) -> tuple[int, list[int], dict[int, int]]:
    """
    Partitions the graph into 2-edge-connected components by removing all bridges.

    Complexity: O(V + E) time and space — an iterative DFS/BFS over non-bridge
    edges visits every vertex once and every edge at most twice.

    Returns:
        A tuple of (component_count, component_id, representatives) where
        component_id maps each vertex to its 1-indexed component id, and
        representatives maps each component id to one vertex belonging to it.
    """
    component_id = [0] * (num_vertices + 1)
    comp_count = 0
    representatives = {}

    for i in range(1, num_vertices + 1):
        if component_id[i] == 0:
            comp_count += 1
            component_id[i] = comp_count
            representatives[comp_count] = i

            # BFS/Iterative DFS to avoid recursion depth issues for component assignment
            stack = [i]
            while stack:
                u = stack.pop()
                for v, edge_id in adj[u]:
                    if not is_bridge[edge_id] and component_id[v] == 0:
                        component_id[v] = comp_count
                        stack.append(v)

    return comp_count, component_id, representatives


def solve() -> None:
    """
    Main logic to solve the Datacenters problem.
    Finds leaf components in the 2-edge-connected component tree and pairs them up.

    Complexity: O(V + E) time and space — bridge-finding and component
    compression are each linear, and the leaf-pairing step is linear in the
    number of leaf components (which is at most V).
    """
    input_data = sys.stdin.buffer.read().split()
    if not input_data:
        return

    it = iter(map(int, input_data))
    try:
        n = next(it)
        m = next(it)
    except StopIteration:
        return

    edge_list = []
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        u = next(it)
        v = next(it)
        edge_list.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))

    # 1. Identify all bridges in the original graph
    is_bridge = find_bridges(n, adj, m)

    # 2. Group vertices into 2-edge-connected components
    comp_count, component_id, representatives = get_2_edge_connected_components(
        n, adj, is_bridge
    )

    if comp_count == 1:
        print(0)
        return

    # 3. Calculate degrees of components in the component tree
    comp_degree = [0] * (comp_count + 1)
    for i, (u, v) in enumerate(edge_list):
        if is_bridge[i]:
            cu = component_id[u]
            cv = component_id[v]
            comp_degree[cu] += 1
            comp_degree[cv] += 1

    # 4. Identify leaf components (degree 1)
    leaf_representatives = [
        representatives[i] for i in range(1, comp_count + 1) if comp_degree[i] == 1
    ]

    # 5. Pair up leaves to create a 2-edge-connected graph
    # Total new cables: ceil(number_of_leaves / 2)
    num_leaves = len(leaf_representatives)
    new_connections = []

    # Simple pairing strategy: connect leaf i with leaf i + num_leaves/2
    # This works better than adjacent pairing for ensuring connectivity in some cases
    mid = (num_leaves + 1) // 2
    for i in range(mid):
        u = leaf_representatives[i]
        v = leaf_representatives[(i + num_leaves // 2) % num_leaves]
        if u != v:
            new_connections.append((u, v))

    print(len(new_connections))
    for u, v in new_connections:
        print(f"{u} {v}")


if __name__ == "__main__":
    solve()
