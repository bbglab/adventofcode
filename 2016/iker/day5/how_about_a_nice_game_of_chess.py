import hashlib


def md5_hash(string):
    m = hashlib.md5()
    m.update(string.encode('ascii'))
    return m.hexdigest()


def find_password(id):
    counter = 0
    password = ""
    while len(password) < 8:
        hash_code = md5_hash(id+str(counter))
        if hash_code.startswith("00000"):
            password += hash_code[5]
        counter += 1
    return password

def find_password2(id):
    counter = 0
    password = [None] * 8
    while None in password:
        hash_code = md5_hash(id+str(counter))
        if hash_code.startswith("00000"):
            pos = hash_code[5]
            if pos in "01234567":
                pos = int(pos)
                if password[pos] is None:
                    password[pos] = hash_code[6]
        counter += 1
    return ''.join(password)

if __name__ == '__main__':
    id = 'cxdnnyjw'
    print('Part1: ', find_password(id))

    print('Part 2:', find_password2(id))
