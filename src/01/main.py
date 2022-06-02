#!/usr/bin/env python3

# Written by Ivona Obonova
# 1.12.2021

import argparse
import numpy as np


parser = argparse.ArgumentParser()
parser.add_argument("fname", type=str, help="File name to input data")


def is_greater(a, b):
    if (a > b): return 1
    else: return 0


def part_one(args):
    data = np.loadtxt(fname=args.fname, dtype=int)
    print(sum(map(is_greater, data[1:], data[:-1])))


def part_two(args):
    data = np.loadtxt(fname=args.fname, dtype=int)
    print(sum(map(is_greater, (data[1:-2] + data[2:-1] + data[3:]), (data[:-3] + data[1:-2] + data[2:-1]))))


def main(args: argparse.Namespace):
    part_one(args) # 1624
    part_two(args) # 1653


if __name__ == "__main__":
    args = parser.parse_args([] if "__file__" not in globals() else None)
    main(args)
