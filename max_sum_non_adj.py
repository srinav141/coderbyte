def find_max_sum(arr):
    first_index_sum = get_sum(0,arr)
    second_index_sum = get_sum(1,arr)

    if first_index_sum > second_index_sum:
        print("max sum is {}".format(first_index_sum))
    else:
        print("max sum is {}".format(second_index_sum))


def get_sum(start_index,arr):
    s = len(arr)
    sum = arr[start_index]
    while start_index < s:
        j = start_index + 2
        k = start_index + 2
        if k >= s:
            k_val = 0
        else:
            k_val = arr[k]
        if j >= s:
            j_val = 0
        else:
            j_val = arr[j]
        if j_val > k_val:
            sum += arr[j]
            start_index = j
        else:
            sum += k_val
            start_index = k

    return sum


def find_max_sum2(arr):
    incl = 0
    excl = 0

    for i in arr:
        # Current max excluding i (No ternary in
        # Python)
        new_excl = excl if excl > incl else incl

        # Current max including i
        incl = excl + i
        excl = new_excl

        # return max of incl and excl
    return (excl if excl > incl else incl)


if __name__ == '__main__':
    find_max_sum([5, 5, 10, 100, 10, 5])
    find_max_sum([1,2,3])
    find_max_sum([1, 20, 3])
    find_max_sum2([5, 5, 10, 100, 10, 5])

