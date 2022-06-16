#!/usr/bin/env python3

# Written by Ivona Obonova
# 2.12.2021


import argparse
import numpy as np


parser = argparse.ArgumentParser()
parser.add_argument('fname', type=str, help='File name to data.')


def part_one(data) -> int:
    horizont, depth = 0, 0

    for i in range(len(data)):
        direction, number = data[i][0], data[i][1]

        if direction == 'forward':
            horizont += number
        elif direction == 'down':
            depth += number
        elif direction == 'up':
            depth -= number
        else:
            raise ValueError

    return horizont * depth


def part_two(data) -> int:
    horizont, depth, aim = 0, 0, 0

    for i in range(len(data)):
        direction, number = data[i][0], data[i][1]

        if direction == 'forward':
            horizont += number
            if aim != 0:
                depth += aim * number
        elif direction == 'down':
            aim += number
        elif direction == 'up':
            aim -= number
        else:
            raise ValueError

    return horizont * depth


def main(args: argparse.Namespace):
    data = np.genfromtxt(fname=args.fname, dtype=['U15', 'int'], delimiter=' ')
    print('Part one:', part_one(data))
    print('Part two:', part_two(data))


if __name__ == '__main__':
    args = parser.parse_args([] if '__file__' not in globals() else None)
    main(args)
