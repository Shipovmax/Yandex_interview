# Task B: Dino's Vacation and Island Flooding

Dino decided to spend his vacation on a tropical archipelago and rented a small helicopter to view the islands from above. Unfortunately, heavy rains have caused a severe flood in the region.

Dino has a topographic map of the archipelago of size **n × m**, where each cell contains the terrain height in meters above the current sea level. Cells with height 0 represent water, and cells with positive height represent land.

Due to the flood, the water level rises at a rate of 1 meter per minute. As soon as the water level equals the land height, that area is flooded and becomes water. Water spreads only to adjacent cells (up, down, left, right); water does not move diagonally.

Dino wants to know after how many minutes each piece of land will be flooded, so he can take beautiful photos of the islands before they disappear underwater.

## Input Format
The first line contains two integers **n** and **m** (1 ≤ n, m ≤ 1000) — the dimensions of the map.
The following **n** lines each contain **m** integers — the cell heights **h[i][j]** (0 ≤ h[i][j] ≤ 10⁹).
A value of 0 means water; positive values represent land height in meters.

## Output Format
Print **n** lines, each containing **m** integers — for each cell, output the time in minutes after which it will be flooded. For cells that are initially water, output 0.

## Notes
- **Example 1:** A cell with height 0 is already flooded (time = 0), a cell with height 1 will flood in 1 minute, height 2 in 2 minutes, and so on.
- **Example 2:** Similar situation — each cell floods exactly after a number of minutes equal to its height.
- **Example 3:** An island with height 5 is adjacent to water, so it floods in 5 minutes. Islands with heights 10, 8, 6 are further from water, but in this case, it doesn't affect the flood time (water level is the primary factor).
