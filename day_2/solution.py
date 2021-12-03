import pandas as pd


def parse_command(command):
    direction = command.split(" ")[0]
    magnitude = int(command.split(" ")[1])
    return direction, magnitude


def apply_command(horizontal, depth, command):
    """
    forward X increases the horizontal position by X units.
    down X increases the depth by X units.
    up X decreases the depth by X units.
    """

    direction, magnitude = parse_command(command)

    if direction == "forward":
        horizontal += magnitude
    elif direction == "up":
        depth -= magnitude
    elif direction == "down":
        depth += magnitude

    return horizontal, depth


def apply_command_part_2(horizontal, depth, aim, command):
    """
    down X increases your aim by X units.
    up X decreases your aim by X units.
    forward X does two things:
        It increases your horizontal position by X units.
        It increases your depth by your aim multiplied by X."""

    direction, magnitude = parse_command(command)

    if direction == "forward":
        horizontal += magnitude
        depth += aim * magnitude
    elif direction == "up":
        aim -= magnitude
    elif direction == "down":
        aim += magnitude

    return horizontal, depth, aim


df = pd.read_csv("data.txt")

horizontal = 0
depth = 0

for command in df['commands'].to_list():
    horizontal, depth = apply_command(horizontal, depth, command)

print(horizontal * depth)


horizontal = 0
depth = 0
aim = 0

for command in df['commands'].to_list():
    horizontal, depth, aim = apply_command_part_2(horizontal, depth, aim, command)

print(horizontal * depth)
