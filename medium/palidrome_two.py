"""
Have the function PalindromeTwo(str) take the str parameter being passed and return the string true if the parameter is a palindrome,
(the string is the same forward as it is backward) otherwise return the string false.
The parameter entered may have punctuation and symbols but they should not affect whether the string is in fact a palindrome.
For example: “Anne, I vote more cars race Rome-to-Vienna” should return true.
"""


def palindrome_two(st):

    res_st = ''.join(e for e in st if e.isalnum()).lower()
    rev_st = res_st[::-1]
    if res_st == rev_st:
        return True
    return False




if __name__ == '__main__':
    result = palindrome_two('Anne, I vote more cars race Rome-to-Vienna')
    print(result)
