import math

syntax_error_scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

completion_scores = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}

bracket_pairs = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}


def get_data():
    return [list(x) for x in open("input.txt").read().split("\n")]


def part_1(brackets_list):
    stack = []
    illegal_character_pts = 0
    for bracket_line in brackets_list:
        for bracket in bracket_line:
            if bracket in bracket_pairs.keys():
                stack.append(bracket)
            else:
                if bracket_pairs.get(stack[-1]) == bracket:
                    stack.pop()
                else:
                    illegal_character_pts += syntax_error_scores.get(bracket)
                    break
    return illegal_character_pts


def part_2(brackets_list):
    completion_pts_list = []
    for bracket_line in brackets_list:
        completion_pts = 0
        stack = []
        corrupt = False
        for bracket in bracket_line:
            if bracket in bracket_pairs.keys():
                stack.append(bracket)
            else:
                if bracket_pairs.get(stack[-1]) == bracket:
                    stack.pop()
                else:
                    corrupt = True
                    break
        if len(stack) > 0 and corrupt == False:
            for bracket in reversed(stack):
                completion_pts *= 5
                completion_pts += completion_scores.get(bracket)
            completion_pts_list.append(completion_pts)
    completion_pts_list.sort()
    middleIndex = math.floor((len(completion_pts_list) - 1)/2)
    return completion_pts_list[middleIndex]


data = get_data()
print(part_2(data))

