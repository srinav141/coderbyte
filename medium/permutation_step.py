"""
have the function PermutationStep(num) //take the num parameter being passed and return the next number greater //than num using the same digits.
 For example: if num is 123 return 132, //if it's 12453 return 12534. If a number has no greater permutations, //return -1 (ie. 999).
"""

def permutation_step(number):

    nu =str(number)
    print('Given num: {}'.format(nu))
    num =[]
    for c in nu:
        num.append(int(c))
    l = len(nu)
    for i in range(l-1,0,-1):
        if num[i] > num[i-1]:
            break;
    if i==0:
        return -1

    x = num[i-1]
    smallest = i
    for j in range(i+1, l):
        if num[j] > x and num[j] < num[smallest]:
            smallest = j

    num[smallest], num[i - 1] = num[i - 1], num[smallest]

    x = 0  # Converting list upto i-1 into number
    for j in range(i):
      x = x * 10 + num[j]
    # Sort the digits after i-1 in ascending order
    num = sorted(num[i:])
    # converting the remaining sorted digits into number
    for j in range(l-i):
        x = x * 10 + num[j]

    return x


if __name__ == "__main__":
    res = permutation_step(12453)
    print(res)

