#!/usr/bin/env python3

# Written by Ivona Obonova
# 2.12.2021


import argparse
import numpy as np


parser = argparse.ArgumentParser()
parser.add_argument("fname", type=str, help="File name to input data")


def part_one(args):
    # U15 as string
    data = np.genfromtxt(fname=args.fname, dtype=['U15', 'int'], delimiter=" ")

    horizont, depth = 0, 0

    for i in range(0, len(data)):
        direction, number = data[i][0], data[i][1]

        if (direction == "forward"):
            horizont += number
        elif (direction == "down"):
            depth += number
        elif (direction == "up"):
            depth -= number

    print(horizont * depth)


def part_two(args):
    # U15 as string
    data = np.genfromtxt(fname=args.fname, dtype=['U15', 'int'], delimiter=" ")

    horizont, depth, aim = 0, 0, 0

    for i in range(0, len(data)):
        direction, number = data[i][0], data[i][1]

        if (direction == "forward"):
            horizont += number
            if (aim != 0):
                depth += aim * number
        elif (direction == "down"):
            aim += number
        elif (direction == "up"):
            aim -= number

    print(horizont * depth)


def main(args: argparse.Namespace):
    part_one(args) # 2120749
    part_two(args) # 2138382217


if __name__ == "__main__":
    args = parser.parse_args([] if "__file__" not in globals() else None)
    main(args)
