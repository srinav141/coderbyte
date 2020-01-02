"""
have the function ArrayAdditionI(arr) take the array * * of numbers stored in arr and return the string true
if any combination of numbers * * in the array can be added up to equal the largest number in the array, otherwise * * return the string false.
 For example: if arr contains [4, 6, 23, 10, 1, 3] the * * output should return true because 4 + 6 + 10 + 3 = 23.
 The array will not be empty, * * will not contain all the same elements, and may contain negative numbers.
"""


def arr_addition(arr):
    arr.sort()
    print('sorted array {}'.format(arr))
    l =len(arr)
    max_num = arr[l-1]
    curr_sum = 0
    i =1

    while i <l-2:
        curr_sum =get_sum(arr[i:l-1])
        if curr_sum < max_num:
            break
        if curr_sum == max_num:
            return True
        i+=1
    return False



def get_sum(arr):
    curr_sum = 0
    for i in arr :
        curr_sum = curr_sum+i
    return curr_sum


def arr_add_2(arr):
    arr.sort()
    print('sorted array {}'.format(arr))
    l = len(arr)
    max_num = arr[l - 1]
    i = j = 0
    curr_sum = 0
    while i < l-1 and j < l-1:
        if curr_sum < max_num:
            curr_sum = curr_sum+arr[j]
            j+=1
        if curr_sum > max_num:
            curr_sum = curr_sum-arr[i]
            i+=1
        if curr_sum == max_num:
            return True
    return False


if __name__ == "__main__":
    arr = [4, 6, 10,23, 1, 3]
    res = arr_addition(arr)
    print(res)
    res = arr_add_2(arr)
    print(res)
