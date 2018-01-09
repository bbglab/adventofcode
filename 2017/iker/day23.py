"""
--- Day 23: Coprocessor Conflagration ---

You decide to head directly to the CPU and fix the printer from there. As you get close, you find an experimental coprocessor doing so much work that the local programs are afraid it will halt and catch fire. This would cause serious issues for the rest of the computer, so you head in and see what you can do.

The code it's running seems to be a variant of the kind you saw recently on that tablet. The general functionality seems very similar, but some of the instructions are different:

    set X Y sets register X to the value of Y.
    sub X Y decreases register X by the value of Y.
    mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
    jnz X Y jumps with an offset of the value of Y, but only if the value of X is not zero. (An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)

    Only the instructions listed above are used. The eight registers here, named a through h, all start at 0.

The coprocessor is currently set to some kind of debug mode, which allows for testing, but prevents it from doing any meaningful work.

If you run the program (your puzzle input), how many times is the mul instruction invoked?


--- Part Two ---

The Turing machine, and soon the entire computer, springs back to life. A console glows dimly nearby, awaiting your command.

> reboot printer
Error: That command requires priority 50. You currently have priority 0.
You must deposit 50 stars to increase your priority to the required level.

The console flickers for a moment, and then prints another message:

Star accepted.
You must deposit 49 stars to increase your priority to the required level.

The garbage collector winks at you, then continues sweeping.


--- Part Two ---

Now, it's time to fix the problem.

The debug mode switch is wired directly to register a. You flip the switch, which makes register a now start at 1 when the program is executed.

Immediately, the coprocessor begins to overheat. Whoever wrote this program obviously didn't choose a very efficient implementation. You'll need to optimize the program if it has any hope of completing before Santa needs that printer working.

The coprocessor's ultimate goal is to determine the final value left in register h once the program completes. Technically, if it had that... it wouldn't even need to run the program.

After setting register a to 1, if the program were to run to completion, what value would be left in register h?

"""


def read():
    with open('inputs/day23.txt') as fd:
        return fd.readlines()


def parse(lines):
    l = []
    for line in lines:
        inst, *params = line.strip().split()
        l.append((inst, params))
    return l


class Registers(dict):

    def __missing__(self, key):
        try:
            v = int(key)
        except ValueError:
            v = 0
            self[key] = 0
        return v


class Coprocessor:

    def __init__(self):
        self.reg = Registers()
        self.INSTRUCTIONS = {'set': self.set, 'sub': self.sub,
                             'mul': self.mul, 'jnz': self.jump}
        self.last_played = None
        self.mul_counter = 0
        self.instructions = None
        self.pos = 0

    def set(self, reg, val):
        self.reg[reg] = self.reg[val]

    def sub(self, reg, val):
        self.reg[reg] -= self.reg[val]

    def mul(self, reg1, reg2):
        self.mul_counter += 1
        self.reg[reg1] *= self.reg[reg2]

    def jump(self, reg, val):
        if self.reg[reg] != 0:
            self.pos += self.reg[val] -1

    def operate(self, instructions):
        self.instructions = instructions
        self.pos = 0
        while True:
            inst, params = self.instructions[self.pos]
            self.INSTRUCTIONS[inst](*params)
            self.pos += 1
            if self.pos < 0 or self.pos >= len(self.instructions):
                break


def part1():
    p = Coprocessor()
    p.operate(parse(read()))
    print(p.mul_counter)


def part2():
    p = Coprocessor()
    init_instruction = 'set', ('a', 1)
    p.operate([init_instruction])
    p.operate(parse(read()))
    print(p.reg['h'])


if __name__ == '__main__':
    part1()
    # part2()
