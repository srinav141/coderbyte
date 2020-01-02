"""
* Have the function LetterCountI(str) take the str parameter being passed and return * * the first word with the greatest number of repeated letters.
 For example: * * "Today, is the greatest day ever!" should return greatest because it has 2 e's * * (and 2 t's) and
 it comes before ever which also has 2 e's. If there are no words * * with repeating letters return -1.
 Words will be separated by spaces.
"""
import collections

def letter_count(str):
    curr_index =0
    curr_count = 0
    str_list = str.split()
    print(str_list)
    for c,i in enumerate(str_list):
        count = get_repeat_count(i)
        if count > curr_count:
            curr_count = count
            curr_index = c
    if curr_count == 0:
        return -1
    return str_list[curr_index]


def get_repeat_count(str):
    c = collections.Counter(str)
    count = 0
    for k,v in c.items():
        if v > 1:
            count+=1
    return count


if __name__ == "__main__":
    max_count_st = letter_count("Today, is the greatest day ever!")
    print(max_count_st)
    max_count_st = letter_count("Today! new")
    print(max_count_st)
