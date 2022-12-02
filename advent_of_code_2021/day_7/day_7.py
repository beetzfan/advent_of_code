# Question: https://adventofcode.com/2021/day/7

def get_data():
    data = open("input.txt").read().strip().split(",")
    return [int(x) for x in data]


def get_sum(horizontal_positions, comparing_position):
    return sum([abs(position - comparing_position) for position in horizontal_positions])


def get_increasing_fuel_sum(horizontal_positions, comparing_position):
    return int(sum([((abs(position - comparing_position) * (abs(position - comparing_position) + 1)) / 2) for position in
                horizontal_positions]))


def part_1(horizontal_positions):
    current_position = 0
    min_sum = get_sum(horizontal_positions, current_position)
    for i in range(1, max(horizontal_positions)):
        current_position = i
        tracking_sum = get_sum(horizontal_positions, current_position)
        if tracking_sum < min_sum:
            min_sum = tracking_sum
    return min_sum


def part_2(horizontal_positions):
    current_position = 0
    min_sum = get_increasing_fuel_sum(horizontal_positions, current_position)
    for i in range(1, max(horizontal_positions)):
        current_position = i
        tracking_sum = get_increasing_fuel_sum(horizontal_positions, current_position)
        if tracking_sum < min_sum:
            min_sum = tracking_sum
    return min_sum


list_of_horizontal_inputs = get_data()
print(part_1(list_of_horizontal_inputs))
print(part_2(list_of_horizontal_inputs))
