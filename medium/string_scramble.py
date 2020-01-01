# Using the Python language, have the function StringScramble(str1,str2) take both parameters being passed and return # the string true
# if a portion of str1 characters can be rearranged to match str2, otherwise return the string false.
# For example: if str1 is "rkqodlw" and str2 is "world" the output should return true. Punctuation and symbols will # not be entered with the parameters.


def string_scramble(str1,str2):
    inner_string = str2
    outer_string = str1

    if len(str1) >= len(str2):
        for c in inner_string:
            if c not in outer_string:
                return False
            updated_str = outer_string.replace(c,"",1)
            outer_string = updated_str
        return True
    return False


if __name__ == '__main__':
   res = string_scramble("rkqodlw","world")
   print(res)





