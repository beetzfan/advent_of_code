# Question: https://adventofcode.com/2021/day/5

class ventsGrid:
    def __init__(self, size):
        self.size = size
        self.grid = [[0 for col in range(self.size)] for row in range(self.size)]

    def mark_grid_horizontal(self, x1y1, x2y2):
        row = x1y1[0]
        max_val = max(x1y1[1], x2y2[1])
        min_val = min(x1y1[1], x2y2[1])
        for col_index in range(self.size):
            if min_val <= col_index <= max_val:
                self.grid[row][col_index] += 1

    def mark_grid_vertical(self, x1y1, x2y2):
        col = x1y1[1]
        max_val = max(x1y1[0], x2y2[0])
        min_val = min(x1y1[0], x2y2[0])
        for row_index in range(self.size):
            if min_val <= row_index <= max_val:
                self.grid[row_index][col] += 1

    def mark_grid_diagonal(self, x1y1, x2y2):
        slope = self.get_slope(x1y1, x2y2)
        if slope > 0:
            if x1y1[0] < x2y2[0]:
                start_point = list(x1y1)
                end_point = x2y2
            else:
                start_point = list(x2y2)
                end_point = x1y1
            while tuple(start_point) != end_point:
                self.grid[start_point[0]][start_point[1]] += 1
                start_point[0] += 1
                start_point[1] += 1
            self.grid[start_point[0]][start_point[1]] += 1
        elif slope < 0:
            if x1y1[0] < x2y2[0]:
                start_point = list(x1y1)
                end_point = x2y2
            else:
                start_point = list(x2y2)
                end_point = x1y1
            while (tuple(start_point) != end_point):
                self.grid[start_point[0]][start_point[1]] += 1
                start_point[0] += 1
                start_point[1] -= 1
            self.grid[start_point[0]][start_point[1]] += 1
        else:
            return

    def get_danger_zone_count(self):
        count = 0
        for row in range(self.size):
            for col in range(self.size):
                if self.grid[row][col] >= 2:
                    count += 1
        return count

    def get_slope(self, x1y1, x2y2):
        if x1y1[1] == x2y2[1] or x1y1[0] == x2y2[0]:
            # this shouldn't be called if not diagonal
            return 0
        else:
            return (x1y1[1] - x2y2[1])/(x1y1[0] - x2y2[0])


def get_data():
    data = open("input.txt").read().strip().split("\n")
    pts1 = []
    pts2 = []
    for line in data:
        pts1.append(tuple(int(x) for x in line.split(" -> ")[0].split(",")))
        pts2.append(tuple(int(x) for x in line.split(" -> ")[1].split(",")))
    return pts1, pts2


def part_1():
    pts1, pts2 = get_data()
    num_of_pts = len(pts1)
    size_of_grid = 1000
    hydrovent_grid = ventsGrid(size_of_grid)
    for i in range(num_of_pts):
        if pts1[i][0] == pts2[i][0]:
            hydrovent_grid.mark_grid_horizontal(pts1[i], pts2[i])
        elif pts1[i][1] == pts2[i][1]:
            hydrovent_grid.mark_grid_vertical(pts1[i], pts2[i])
        else:
            # is diagonal, ignore
            continue
    return hydrovent_grid.get_danger_zone_count()


def part_2():
    pts1, pts2 = get_data()
    num_of_pts = len(pts1)
    size_of_grid = 1000
    hydrovent_grid = ventsGrid(size_of_grid)
    for i in range(num_of_pts):
        if pts1[i][0] == pts2[i][0]:
            hydrovent_grid.mark_grid_horizontal(pts1[i], pts2[i])
        elif pts1[i][1] == pts2[i][1]:
            hydrovent_grid.mark_grid_vertical(pts1[i], pts2[i])
        else:
            hydrovent_grid.mark_grid_diagonal(pts1[i], pts2[i])
    return hydrovent_grid.get_danger_zone_count()
