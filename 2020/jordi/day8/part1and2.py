#!/bin/env python3

from collections import namedtuple
from typing import List

Instruction = namedtuple('Instruction', ['label', 'arg'])
ExecResult = namedtuple('ExecResult', ['pos', 'acc', 'loop'])

INSTRUCTION_SET = {
    "nop": lambda x: (+1, x[0]),
    "acc": lambda x: (+1, x[0] + x[1]),
    "jmp": lambda x: (x[1], x[0])
}


def execute_instruction(ins: Instruction, pos: int, acc: int) -> (int, int):
    inc, acc = INSTRUCTION_SET[ins.label]((acc, ins.arg))
    return pos + inc, acc


def execute_program(instructions: List[Instruction]) -> ExecResult:
    visited = set()
    acc, pos = 0, 0
    while 0 <= pos < len(instructions):
        visited.add(pos)
        pos, acc = execute_instruction(instructions[pos], pos, acc)
        if pos in visited:
            # Stop execution if a loop is detected
            return ExecResult(pos, acc, True)
    return ExecResult(pos, acc, False)


def instructions_mutator(instructions: List[Instruction]):
    # First yield without any mutation
    yield [ins for ins in instructions]

    # Mutate one instruction at each iteration
    for mutation in [('jmp', 'nop'), ('nop', 'jmp')]:
        for p, ins in filter(lambda x: x[1][0] == mutation[0], enumerate(instructions)):
            mutated_instructions = [ins for ins in instructions]
            mutated_instructions[p] = Instruction(mutation[1], ins.arg)
            yield mutated_instructions


def main():
    with open("input.txt") as fd:
        instructions = [Instruction(asm[0], int(asm[1])) for asm in [line.strip().split(" ") for line in fd.readlines()]]

    result = execute_program(instructions)
    print("Part One", result.acc)

    result = next(filter(lambda r: not r.loop, map(execute_program, instructions_mutator(instructions))))
    print("Part Two", result.acc)


if __name__ == "__main__":
    main()
