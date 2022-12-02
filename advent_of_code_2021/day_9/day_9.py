def get_data():
    floor_map = open("input.txt").read().split("\n")
    floor_map_split = [list(x) for x in floor_map]
    return [[int(x) for x in lst] for lst in floor_map_split]


def is_risk(pt_to_check, nhbr_pts):
    is_risk = True
    for pt in nhbr_pts:
        if pt_to_check > pt:
            is_risk = False
    return is_risk


def get_neighbour_indices(width, height, pt):
    neighbors = lambda x, y: [[x2, y2] for x2 in range(x - 1, x + 2)
                              for y2 in range(y - 1, y + 2)
                              if (-1 < x < width and
                                  -1 < y < height and
                                  (x != x2 or y != y2) and
                                  (0 <= x2 < width) and
                                  (0 <= y2 < height))]
    return neighbors(pt[0], pt[1])


def get_neighbour_values(grid, points):
    nbhr_pts = []
    for point in points:
        nbhr_pts.append(grid[point[0]][point[1]])
    return nbhr_pts


def part_1(floor_map):
    sum_of_risk_points = 0
    row_count = len(floor_map)
    col_count = len(floor_map[0])
    for i in range(row_count):
        for j in range(col_count):
            neighbour_points = get_neighbour_indices(row_count, col_count, (i, j))
            neighbour_values = get_neighbour_values(floor_map, neighbour_points)
            if is_risk(floor_map[i][j], neighbour_values):
                print(floor_map[i][j])
                sum_of_risk_points += (floor_map[i][j] + 1)
    return sum_of_risk_points


def part_2(floor_map):
    basin_1 = 0
    basin_2 = 0
    basin_3 = 0

    return basin_1 * basin_2 * basin_3


points = get_data()
print(part_1(points))
