# Question: https://adventofcode.com/2021/day/1

def part_1(data):
    increase_count = 0
    for i in range(len(data) - 1):
        if data[i + 1] > data[i]:
            increase_count += 1
    return increase_count


def part_2(data):
    sliding_window_list = []
    for i in range(len(data) - 2):
        window_sum = data[i] + data[i + 1] + data[i + 2]
        sliding_window_list.append(window_sum)
    return part_1(sliding_window_list)


# get input and convert to int
input = open('input.txt', 'r').read().split('\n')
int_input = [int(x) for x in input]
print(part_1(int_input))
print(part_2(int_input))

