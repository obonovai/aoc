#!/usr/bin/env python3

# Written by Ivona Obonova
# 4.12.2021


import argparse


parser = argparse.ArgumentParser()
parser.add_argument('fname', type=str, help='File name to data.')


def get_boards(args):
    drawns, boards = [], []
    with open(args.fname) as f:
        line = f.readline()
        drawns = list(map(int, line.strip().split(',')))
        board = []
        for line in f:
            if line == '\n':
                if board:
                    boards += [board]
                    board   = []
            else:
                board += [list(map(int, line.strip().split()))]
        if board:
            boards += [board]
    return drawns, boards


def part_one(drawns, boards) -> int:
    for drawn in drawns:
        for board in boards:
            for row in board:
                for i in range(len(row)):
                    if row[i] == drawn:
                        row[i] = -1
            rows    = [all(column == -1 for column in row) for row in board]
            columns = [all(row[i] == -1 for row in board) for i in range(len(board[0]))]
            if True in rows or True in columns:
                return sum([x for row in board for x in row if x > 0]) * drawn


def part_two(drawns, boards) -> int:
    winners = [False] * len(boards)
    for drawn in drawns:
        for i in range(len(boards)):
            for row in boards[i]:
                for j in range(len(row)):
                    if row[j] == drawn:
                        row[j] = -1
            rows    = [all(column == -1 for column in row) for row in boards[i]]
            columns = [all(row[k] == -1 for row in boards[i]) for k in range(len(boards[i]))]
            if True in rows or True in columns:
                winners[i] = True
                if not False in winners:
                    return sum([x for row in boards[i] for x in row if x > 0]) * drawn


def main(args: argparse.Namespace):
    drawns, boards = get_boards(args)
    print('Part one:', part_one(drawns, boards))
    print('Part two:', part_two(drawns, boards))


if __name__ == '__main__':
    args = parser.parse_args([] if '__file__' not in globals() else None)
    main(args)
