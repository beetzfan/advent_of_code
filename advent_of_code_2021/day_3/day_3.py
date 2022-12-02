# Question: https://adventofcode.com/2021/day/3
import pandas as pd


def part_1(gamma, epsilon):
    gamma_rate = int("".join(gamma), 2)  # most common
    epsilon_rate = int("".join(epsilon), 2)  # least common
    return epsilon_rate * gamma_rate


def get_gamma_and_epsilon_values(bin_nums, value_to_get):
    bin_nums_df = pd.DataFrame.from_records([list(x) for x in bin_nums])
    mode = bin_nums_df.mode().to_numpy()
    gamma_value = []
    if len(mode) == 2:
        for index,bit in enumerate(mode[0]):
            if bit == '0' and mode[1][index] == '1':
                gamma_value.append('1')
            else:
                gamma_value.append(bit)
    else:
        gamma_value = mode[0]
    epsilon_value = ['1' if x == '0' else '0' for x in gamma_value]
    if value_to_get == 'both':
        return gamma_value, epsilon_value
    elif value_to_get == 'gamma':
        return gamma_value
    else:
        return epsilon_value


def part_2(bin_nums, gamma, epsilon):
    oxygen_gen_rating = get_rating(bin_nums, gamma, len(gamma), 'gamma')
    co2_scrub_rating = get_rating(bin_nums, epsilon, len(epsilon), 'epsilon')
    oxygen_in_dec = int("".join(oxygen_gen_rating), 2)
    co2_in_dec = int("".join(co2_scrub_rating), 2)
    return oxygen_in_dec * co2_in_dec


def get_rating(bin_nums, value, len_of_bit, gamma_or_epsilon):
    temp_list = bin_nums
    for i in range(len_of_bit):
        outcome_of_filter = filter_by_bit(value[i], i, temp_list)
        if not outcome_of_filter:
            return temp_list[-1]
        else:
            temp_list = outcome_of_filter
            value = get_gamma_and_epsilon_values(temp_list, gamma_or_epsilon)
    return temp_list[0]


def filter_by_bit(bit, index_of_bit, list_of_bits):
    final_list = []
    for num in list_of_bits:
        if num[index_of_bit] == bit:
            final_list.append(num)
    return final_list


input = open('sample_input.txt', 'r').read().split('\n')
split_bins = pd.DataFrame.from_records([list(x) for x in input])
split_bins_list = [list(x) for x in input]

gamma_values, epsilon_values = get_gamma_and_epsilon_values(input, 'both')

print(part_1(gamma_values, epsilon_values))
print(part_2(split_bins_list, gamma_values, epsilon_values))
