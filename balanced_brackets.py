import math
import os
import random
import re
import sys

CLOSE_MATCH_GUIDE = {
    ']': '[',
    ')': '(',
    '}': '{'
}

def isMatched(closeChar, lastChar):
    if closeChar not in CLOSE_MATCH_GUIDE:
        return False
    return CLOSE_MATCH_GUIDE[closeChar] == lastChar

def isStackBalanced(s):
    stack = []
    for c in s:
        if c in CLOSE_MATCH_GUIDE:
            if len(stack) == 0:
                return False
            pop = stack.pop()
            if not isMatched(c, pop):
                return False
        else:
            stack.append(c)
    if len(stack) > 0:
        return False
    return True


def isBalanced(s):
    if isStackBalanced(s):
        return 'YES'
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
