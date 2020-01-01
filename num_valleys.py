import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    lvl =0
    v =0
    for i in s:
        if i == 'U':
            lvl+=1
        else:
            lvl-=1
        if lvl == 0 and i == 'U':
            v+=1
    return v


if __name__ == '__main__':
    n = 12
    s = ['D','D','U','U','D','D','U','D','U','U','U','D']
    result = countingValleys(n, s)
    print(result)

