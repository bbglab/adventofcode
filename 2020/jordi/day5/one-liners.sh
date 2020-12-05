#!/bin/bash

# Part One
cat input.txt | xargs -I {} /bin/bash -c "echo \"ibase=2;obase=A;\$(echo {} | cut -c 1-7 | tr 'F' '0' | tr 'B' '1') * 8 + \$(echo {} | cut -c 8-10 | tr 'L' '0' | tr 'R' '1')\"" | bc | sort -n | tail -n 1

# Part Two
cat <(cat input.txt | xargs -I {} /bin/bash -c "echo \"ibase=2;obase=A;\$(echo {} | cut -c 1-7 | tr 'F' '0' | tr 'B' '1') * 8 + \$(echo {} | cut -c 8-10 | tr 'L' '0' | tr 'R' '1') + 1\"" | bc) <(cat input.txt | xargs -I {} /bin/bash -c "echo \"ibase=2;obase=A;\$(echo {} | cut -c 1-7 | tr 'F' '0' | tr 'B' '1') * 8 + \$(echo {} | cut -c 8-10 | tr 'L' '0' | tr 'R' '1')\"" | bc) | sort -n | uniq -u | head -n2 | tail -n1

