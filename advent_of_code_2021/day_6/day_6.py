# Question: https://adventofcode.com/2021/day/6
from collections import Counter

def get_data():
    data = open("input.txt").read().strip().split(",")
    return [int(x) for x in data]


def part_1(fish_timer, num_days):
    for i in range(num_days):
        fish_to_add_count = 0
        for index, timer in enumerate(fish_timer):
            if timer > 0:
                fish_timer[index] -= 1
            else:
                fish_timer[index] = 6
                fish_to_add_count += 1
        fish_timer += fish_to_add_count * [8]
        print("day: " + str(i))
    return len(fish_timer)


# def part_2(fish_timer, num_days):
#     count_of_fish_per_day = 7 * [0] # for fish with with 0-6 days remaining to reproduce
#     special_case = 2 * [0]
#     for fish in fish_timer:
#         if fish < 7:
#             count_of_fish_per_day[fish] += 1
#         elif fish == 7:
#             special_case[0] += 1
#         elif fish == 8:
#             special_case[1] += 1
#     print(count_of_fish_per_day)
#     for i in range(num_days):
#         print("day: " + str(i))
#         # get all fish with 0 days left and add to special case list
#         new_fish = count_of_fish_per_day.pop(0)
#         special_case.append(new_fish)
#         print("new_fish", new_fish)
#         print("special_case", special_case)
#
#         # take out fish at index 0 and move to end of normal fish list
#         value_to_move = special_case.pop(0)
#         count_of_fish_per_day.append(value_to_move)
#         print("value to move", value_to_move)
#         print("count of fish per day", count_of_fish_per_day)
#         print("***********************")
#     return sum(count_of_fish_per_day) + sum(special_case)

def part_2(fish_timer, days):
    timers = Counter({timer: 0 for timer in range(10)})
    fish_timer = Counter(fish_timer)
    fish_timer.update(timers)

    for day in range(days):
        fish_timer[7] += fish_timer.get(0,0)
        fish_timer[9] += fish_timer.get(0,0)
        fish_timer = {fish: fish_timer.get(fish + 1, 0) for fish in fish_timer}
    return sum(fish_timer.values())

input = get_data()
print(part_2(input, 256))