import re
import os
import numpy as np


give_regex = re.compile(r'value ([0-9]+) goes to bot ([0-9]+)')

instruction_regex = re.compile(r'bot ([0-9]+) gives low to (bot|output) ([0-9]+)'
                               r' and high to (bot|output) ([0-9]+)')

class Bot:
    def __init__(self, id):
        self.id = id
        self.low = None
        self.high = None
        self.low_to = None
        self.high_to = None
        self.triggered = False

    def receive(self, chip):
        if self.low is None and self.high is None:
            self.low = chip
        elif self.low < chip:
            self.high = chip
        else:
            self.high = self.low
            self.low = chip
        self.trigger()

    def add_instruction(self, low_to, high_to):
        self.low_to = low_to
        self.high_to = high_to
        self.trigger()

    def trigger(self):
        if not self.triggered and self.low is not None and self.high is not \
                None and self.low_to is not None and self.high_to is not None:
            self.low_to.receive(self.low)
            self.high_to.receive(self.high)
            self.triggered = True



class Output:

    def __init__(self, id):
        self.id = id
        self.chips = []

    def receive(self, chip):
        self.chips.append(chip)

class BotFactory:

    def __init__(self):
        self.bots = {}
        self.outputs = {}

    def get_bot(self, id):
        if id in self.bots:
            return self.bots[id]
        else:
            bot = Bot(id)
            self.bots[id] = bot
            return bot

    def get_output(self, id):
        if id in self.outputs:
            return self.outputs[id]
        else:
            output_bin = Output(id)
            self.outputs[id] = output_bin
            return output_bin

    def process_instruction(self, instruction):
        m = give_regex.match(instruction)
        if m:
            chip, bot_id = m.groups()
            chip = int(chip)
            bot_id = int(bot_id)
            bot = self.get_bot(bot_id)
            bot.receive(chip)
        else:
            bot_id, low_to, low_to_id, high_to, high_to_id = \
                instruction_regex.match(instruction).groups()
            bot_id = int(bot_id)
            low_to_id = int(low_to_id)
            high_to_id = int(high_to_id)
            bot = self.get_bot(bot_id)
            if low_to == 'output':
                low_to = self.get_output(low_to_id)
            elif low_to == 'bot':
                low_to = self.get_bot(low_to_id)
            if high_to == 'output':
                high_to = self.get_output(high_to_id)
            elif high_to == 'bot':
                high_to = self.get_bot(high_to_id)
            bot.add_instruction(low_to, high_to)


if __name__ == '__main__':
    dir = os.path.dirname(__file__)
    file = os.path.join(dir, 'input.txt')
    factory = BotFactory()
    with open(file) as fd:
        for line in fd:
            factory.process_instruction(line.strip())

    for id, bot in factory.bots.items():
        if bot.high == 61 and bot.low == 17:
            print('Part1: ', id)

    output_bin_0_chip = factory.outputs[0].chips[0]
    output_bin_1_chip = factory.outputs[1].chips[0]
    output_bin_2_chip = factory.outputs[2].chips[0]
    print('Part 2:', output_bin_0_chip*output_bin_1_chip*output_bin_2_chip)
