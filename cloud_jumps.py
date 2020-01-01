import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    j = 0
    l = len(c)
    i = 0
    while i < l-1:
        if i+2 <= l-1 and c[i+2] == 0:
            i = i+2
        else:
            i = i+1
        j+=1
    return j




if __name__ == '__main__':


    n = 6

    #c = [0, 0, 0, 0, 1, 0]
    c = [0, 0, 1, 0,0, 1, 0]

    result = jumpingOnClouds(c)
    print(result)
