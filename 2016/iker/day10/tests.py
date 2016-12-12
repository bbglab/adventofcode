import pytest

from balance_bots import BotFactory

def test0():
    instructions = ['value 5 goes to bot 2',
                    'bot 2 gives low to bot 1 and high to bot 0',
                    'value 3 goes to bot 1',
                    'bot 1 gives low to output 1 and high to bot 0',
                    'bot 0 gives low to output 2 and high to output 0',
                    'value 2 goes to bot 2']
    factory = BotFactory()
    for instruction in instructions:
        factory.process_instruction(instruction)

    for chip in factory.outputs[0].chips:
        assert chip in [5]
    for chip in factory.outputs[1].chips:
        assert chip in [2]
    for chip in factory.outputs[2].chips:
        assert chip in [3]
    for id, bot in factory.bots.items():
        if bot.low == 2 and bot.high == 5:
            assert id == 2

if __name__ == "__main__":
    pytest.main(__file__)

