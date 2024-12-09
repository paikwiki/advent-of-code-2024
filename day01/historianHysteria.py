import os


def solve1(lines):
    left_list = []
    right_list = []
    for line in lines.strip().splitlines():
        left, right = line.split("   ")
        left_list.append(int(left))
        right_list.append(int(right))
    left_list.sort()
    right_list.sort()

    diff_list = []
    for left, right in zip(left_list, right_list):
        diff = right - left
        if diff < 0:
            diff *= -1
        diff_list.append(diff)

    return sum(diff_list)


def solve2(lines):
    left_list = []
    right_list = []
    for line in lines.strip().splitlines():
        left, right = line.split("   ")
        left_list.append(int(left))
        right_list.append(int(right))

    right_map = {}
    for right in right_list:
        right_map[right] = right_map.get(right, 0) + 1

    result = 0
    for left in left_list:
        right_value = right_map.get(left, 0)
        result += left * right_value

    return result


def test(lines):
    result = solve1(lines)
    print(f"result: {result}")
    result = solve2(lines)
    print(f"result: {result}")


if __name__ == "__main__":
    current_path = os.path.dirname(os.path.realpath(__file__))
    with open(f"{current_path}/input") as input:
        test(input.read())
