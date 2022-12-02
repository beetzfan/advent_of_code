def get_data():
    data = open("input.txt").read().strip().split("\n")
    data_split = [x.split("|") for x in data]
    for i in range(len(data_split)):
        for j in range(2):
            data_split[i][j] = data_split[i][j].split(" ")
    return data_split


def part_1(digit_data):
    count_of_1478 = 0
    num_of_segments_in_1478 = [2, 3, 4, 7]
    for row in digit_data:
        for value in row[1]:
            if len(value) in num_of_segments_in_1478:
                count_of_1478 += 1
    return count_of_1478


def parse_line(line):
    digit_str, readout_str = line.strip().split(' | ')

    digits = [tuple(sorted(digit)) for digit in digit_str.split(' ')]
    readout = [tuple(sorted(digit)) for digit in readout_str.split(' ')]

    return digits, readout


def filter_by_segment_count(digits, segment_count):
    return list(filter(lambda digit: len(digit) == segment_count, digits))


def digit_has_segments(digit, segment_list):
    return all(item in digit for item in segment_list)


def int_from_readout(readout, translations):
    out = ''
    for digit in readout:
        out += translations[digit]

    return int(out)


def find_one(digits):
    return filter_by_segment_count(digits, 2)[0]


def find_four(digits):
    return filter_by_segment_count(digits, 4)[0]


def find_seven(digits):
    return filter_by_segment_count(digits, 3)[0]


def find_eight(digits):
    return filter_by_segment_count(digits, 7)[0]


def find_three(digits, one):
    for digit in filter_by_segment_count(digits, 5):
        if digit_has_segments(digit, one):
            return digit


def find_nine(digits, four):
    for digit in filter_by_segment_count(digits, 6):
        if digit_has_segments(digit, four):
            return digit


def find_zero_and_six(digits, one, nine):
    for digit in filter_by_segment_count(digits, 6):
        if digit == nine:
            continue

        if digit_has_segments(digit, one):
            zero = digit
        else:
            six = digit

    return zero, six

def find_two_and_five(digits, three, six):
    for digit in filter_by_segment_count(digits, 5):
        if digit == three:
            continue

        if digit_has_segments(six, digit):
            five = digit
        else:
            two = digit

    return two, five


with open('input.txt') as f:
    output_sum = 0
    for line in f:
        digits, readout = parse_line(line)

        one = find_one(digits)
        four = find_four(digits)
        seven = find_seven(digits)
        eight = find_eight(digits)
        three = find_three(digits, one)
        nine = find_nine(digits, four)
        zero, six = find_zero_and_six(digits, one, nine)
        two, five = find_two_and_five(digits, three, six)

        translations = {
            zero: '0',
            one: '1',
            two: '2',
            three: '3',
            four: '4',
            five: '5',
            six: '6',
            seven: '7',
            eight: '8',
            nine: '9'
        }

        output_sum += int_from_readout(readout, translations)

print(output_sum)


inputs = get_data()
print(part_1(inputs))
