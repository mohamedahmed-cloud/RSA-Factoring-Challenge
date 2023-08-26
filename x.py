#!/usr/bin/env python3
# factors challenge

import sys

def check_factor(*args):
    if len(args) != 3:
        count = 0
        num2 = 1
        for a in args:
            if count > 1:
                num2 *= a
            count += 1
    else:
        num2 = args[2]

    num1 = args[1]
    num = args[0].replace(':', '=')

    if num2 > num1:
        numcp = num1
        num1 = num2
        num2 = numcp

    return f"{num}{num1}*{num2}"

if len(sys.argv) != 2:
    print('Usage: factors <file>')
    sys.exit(1)
else:
    filename = sys.argv[1]

    with open(filename, 'r') as file:
        for line in file:
            result = subprocess.check_output(['factor', line], universal_newlines=True)
            factors = list(map(int, result.split()[1:]))
            result_str = check_factor(*factors)
            print(result_str)
