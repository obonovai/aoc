#!/usr/bin/env python3

# Written by Ivona Obonova
# 1.12.2021


import argparse
import numpy as np


parser = argparse.ArgumentParser()
parser.add_argument('fname', type=str, help='File name to data.')


def part_one(data) -> int:
    return sum(map(lambda x, y: x > y, data[1:], data[:-1]))


def part_two(data) -> int:
    return sum(map(lambda x, y: x > y, (data[1:-2] + data[2:-1] + data[3:]), (data[:-3] + data[1:-2] + data[2:-1])))


def main(args: argparse.Namespace):
    data = np.loadtxt(fname=args.fname, dtype=int)
    print('Part one:', part_one(data))
    print('Part two:', part_two(data))


if __name__ == '__main__':
    args = parser.parse_args([] if '__file__' not in globals() else None)
    main(args)
