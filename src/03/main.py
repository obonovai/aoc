#!/usr/bin/env python3

# Written by Ivona Obonova
# 3.12.2021


import argparse

from math import ceil


parser = argparse.ArgumentParser()
parser.add_argument('fname', type=str, help='File name to data.')


def part_one(data):
    ones    = [sum(column) for column in zip(*data)]
    gamma   = ['0' if s < ceil(len(data) / 2) else '1' for s in ones]
    epsilon = ['0' if s > ceil(len(data) / 2) else '1' for s in ones]
    return int(''.join(gamma), 2) * int(''.join(epsilon), 2)


def part_two(data) -> int:
    def determine_oxygen(numbers, index = 0):
        ones    = sum([number[index] for number in numbers])
        msb     = 0 if ones < ceil(len(numbers) / 2) else 1
        numbers = [number for number in numbers if number[index] == msb]
        if len(numbers) == 1:
            return numbers[0]
        else:
            return determine_oxygen(numbers, index + 1)


    def determine_co2(numbers, index = 0):
        ones    = sum([number[index] for number in numbers])
        lsb     = 0 if ones >= ceil(len(numbers) / 2) else 1
        numbers = [number for number in numbers if number[index] == lsb]
        if len(numbers) == 1:
            return numbers[0]
        else:
            return determine_co2(numbers, index + 1)

    oxygen = determine_oxygen(data)
    co2    = determine_co2(data)
    return int(''.join(map(str, oxygen)), 2) * int(''.join(map(str, co2)), 2)


def main(args: argparse.Namespace):
    data = []
    with open(args.fname) as f:
        for line in f:
            line = line.strip()
            data += [[int(c) for c in line]]

    print('Part one:', part_one(data))
    print('Part two:', part_two(data))


if __name__ == '__main__':
    args = parser.parse_args([] if '__file__' not in globals() else None)
    main(args)
