class Octopus:
    def __init__(self, value):
        self.value = value
        self.flashed = 0

    def __repr__(self):
        return f'''{self.value}'''

    def __str__(self):
        return self.value

    def increase(self):
        self.value += 1
        if self.value > 9 and not self.flashed:
            self.to_flash()

    def to_flash(self):
        if not self.flashed:
            self.flashed = 1

    def flash(self):
        if self.flashed == 1:
            self.flashed = 2
            return True
        else:
            return False

    def reset(self):
        if self.flashed == 2:
            self.value = 0
            self.flashed = 0
            return True
        else:
            return False

def get_data():
    grid = open("sample_input.txt").read().split("\n")
    grid_split = [list(x) for x in grid]
    return [[int(x) for x in lst] for lst in grid_split]


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


def part_1(octopus_grid, num_days):
    num_flashes = 0
    row_count = len(octopus_grid)
    col_count = len(octopus_grid[0])
    for day in range(num_days):
        for x in range(10):
            print(octopus_grid[x])
            # print(num_flashes)
        print("***********************")
        for i in range(row_count):
            for j in range(col_count):
                octopus_grid[i][j] += 1
                neighbour_points = get_neighbour_indices(row_count, col_count, (i, j))
                if octopus_grid[i][j] > 9:
                    for point in neighbour_points:
                        octopus_grid[point[0]][point[1]] += 1

    return num_flashes


octo_grid = get_data()
print(part_1(octo_grid, 10))