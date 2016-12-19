import re
import hashlib
from functools import partial

regex = re.compile(r'([a-z0-9])(?=\1\1)')


def md5_hash(string):
    m = hashlib.md5()
    m.update(string.encode('ascii'))
    return m.hexdigest()


def generate_keys(salt_string):
    salt = salt_string
    index = 0
    while True:
        yield index, md5_hash(salt + str(index))
        index += 1

class PadKey:

    def __init__(self, char, index):
        self.char = char
        self.index = index
        self.counts = 0


def index_of_key(key_generator, number_of_keys):
    keys_found = []
    index_of_keys_found = []
    potential_keys = []

    for index, generated_hash in key_generator():
        keys_to_remove = []
        for key in potential_keys:
            if index > key.index + 1001:
                keys_to_remove.append(key)
                if key.counts >= 1:
                    keys_found.append(key.char)
                    index_of_keys_found.append(key.index)
            else:
                if key.char*5 in generated_hash:
                    key.counts += 1

        for key in keys_to_remove:
            potential_keys.remove(key)
        match = regex.search(generated_hash)
        if match:
            potential_keys.append(PadKey(match.groups()[0], index))

        if len(keys_found) >= number_of_keys:
            break

    return max(index_of_keys_found)


def generate_hashed_keys(salt_string):
    for index, hash_key in generate_keys(salt_string):
        for i in range(2016):
            hash_key = md5_hash(hash_key)
        yield index, hash_key

if __name__ == '__main__':
    salt = 'qzyelonm'
    keys_generator = partial(generate_keys, salt)
    print('Part1: ', index_of_key(keys_generator, 64))

    keys_generator = partial(generate_hashed_keys, salt)
    print('Part 2:', index_of_key(keys_generator, 64))
