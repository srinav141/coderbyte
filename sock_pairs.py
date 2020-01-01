import math
import os
import random
import re
import sys
from collections import Counter


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    d = {}
    for i in ar:
        if i in d.keys():
            d[i] = d[i] + 1
        else:
            d[i] = 1

    no_pairs = 0
    for k, v in d.items():
        no_pairs+=v//2
    return no_pairs


if __name__ == '__main__':


    n = 9

    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

    print(Counter(ar))

    result = sockMerchant(n, ar)
    print(result)

