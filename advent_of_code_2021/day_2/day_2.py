# Question: https://adventofcode.com/2021/day/2
import numpy as np


def part_1(directions):
    horizontal_position = 0
    depth = 0
    for i in range(0, np.size(directions)):
        if directions[i][0] == b'forward':
            horizontal_position += directions[i][1]
        elif directions[i][0] == b'up':
            depth -= directions[i][1]
        elif directions[i][0] == b'down':
            depth += directions[i][1]
    return horizontal_position * depth


def part_2(directions):
    horizontal_position = 0
    depth = 0
    aim = 0
    for i in range(0, np.size(directions)):
        if directions[i][0] == b'forward':
            horizontal_position += directions[i][1]
            depth += aim * directions[i][1]
        elif directions[i][0] == b'up':
            aim -= directions[i][1]
        elif directions[i][0] == b'down':
            aim += directions[i][1]
    return horizontal_position * depth


input = np.loadtxt('input.txt', dtype={'names': ('direction', 'units'),
                                       'formats': ('S10', 'i4')})
print(part_1(input))
print(part_2(input))
