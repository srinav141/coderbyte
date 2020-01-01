"""
Have the function RunLength(str) take the str parameter being passed and return a compressed version of the string using the Run-length encoding algorithm.
This algorithm works by taking the occurrence of each repeating character and outputting that number along with a single character of the repeating sequence.
 example: "wwwggopp" would return 3w2g1o2p. The string will not contain any numbers, punctuation, or symbols.
"""
import collections


def run_length(st):
    c = collections.Counter(st)
    for k,v in c.items():
        print(str(v)+k,end='')


if __name__ == "__main__":
    run_length('wwwggopp')
