import os

import re

from gevent.pywsgi import _InvalidClientInput

tls_regex = re.compile(r'([a-z])(?!\1)([a-z])\2\1(?![^[]*\])')

tls_invalid_regex = re.compile(r'([a-z])(?!\1)([a-z])\2\1(?=[^[]*\])')
# if a ABBA is found within [] the IP is invalid

aba_regex = re.compile(r'(?=([a-z])(?!\1)([a-z])\1)(?![^[]*\])')

def count_ips_with_tls(ips):
    counts = 0
    for ip in ips:
        if tls_regex.search(ip) and not tls_invalid_regex.search(ip):
            counts += 1
    return counts

def count_ips_with_ssl(ips):
    counts = 0
    for ip in ips:
        matches = aba_regex.findall(ip)
        for match in matches:
            a, b = match
            if re.search(r'(?='+b+a+b+r')(?=[^[]*\])', ip):
                counts += 1
                break
    return counts


if __name__ == '__main__':
    dir = os.path.dirname(__file__)
    file = os.path.join(dir, 'input.txt')
    ips = []
    with open(file) as fd:
        for line in fd:
            ips.append(line.strip())
    print('Part1: ', count_ips_with_tls(ips))

    print('Part 2:', count_ips_with_ssl(ips))
