import sys
from heapq import heappush, heappop


def main() -> None:
    """
    Calculates the flooding time for each cell in an n x m grid.
    Water level rises by 1 meter per minute. 
    A cell floods if the water level reaches its height AND water can flow to it from a flooded neighbor.
    Initially, all cells with height 0 are flooded.
    
    This is solved using a variation of Dijkstra's algorithm.

    Complexity: O(N*M * log(N*M)) time — each of the N*M cells is pushed onto
    the heap at most once per relaxation from its up to 4 neighbors, and each
    heap operation costs O(log(N*M)). Space: O(N*M) for the grid, flood_time
    table, and heap.
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

    grid = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            try:
                grid[i][j] = next(it)
            except StopIteration:
                break

    # Flood time for each cell. Initialize with a large value.
    INF = 10**18
    flood_time = [[INF] * m for _ in range(n)]
    heap = []

    # All initial water cells (height 0) are the starting points for the flood.
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                flood_time[i][j] = 0
                heappush(heap, (0, i, j))

    # If there is no water initially, the flood cannot start according to the rules (water spreads from 0 cells).
    # However, the problem description implies water rises everywhere. 
    # Let's check the logic: "Water spreads only to adjacent cells".
    # This means if an island is completely surrounded by land, it only floods when the water reaches it from the edge or a 0-cell.
    if not heap:
        # If no water is present, the problem might be interpreted differently.
        # But based on the 'water spreads' rule, we assume the perimeter or initial 0 cells.
        # Let's output original heights if no water is found, or assume the flood starts from outside?
        # Re-reading: "Cells with height 0 represent water".
        out_lines = [" ".join(map(str, row)) for row in grid]
        sys.stdout.write("\n".join(out_lines))
        return

    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

    while heap:
        cur_t, x, y = heappop(heap)
        
        if cur_t > flood_time[x][y]:
            continue
            
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                # The time a neighbor floods is the maximum of the current water time
                # and the neighbor's own elevation.
                arrival_time = max(cur_t, grid[nx][ny])
                if arrival_time < flood_time[nx][ny]:
                    flood_time[nx][ny] = arrival_time
                    heappush(heap, (arrival_time, nx, ny))

    # Prepare and write output
    output = []
    for i in range(n):
        output.append(" ".join(map(str, flood_time[i])))
    
    sys.stdout.write("\n".join(output) + "\n")


if __name__ == "__main__":
    main()
