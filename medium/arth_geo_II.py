"""
Have the function ArthGeo(str) take the array of numbers being passed and return the string "Airthmetic" if sequence follow airthmetic pattern,
return the string "Geometric" if sequence follow geometric pattern. If neither return -1
"""
import math


def airth_geo_II(arr):
    print(arr)
    if is_arth(arr):
        return "Airthmetic"
    elif is_geo(arr):
        return "Geometric"
    return "-1"


def is_arth(arr):
    l =len(arr)
    last_dig = arr[l-1]
    firt_dig = arr[0]
    d = (last_dig-firt_dig)//(l-1)
    for i in range(l-1):
        if not (arr[i+1]- arr[i]) == d:
            return False
    return True


def is_geo(arr):
    l = len(arr)
    firt_dig = arr[0]
    sec_digit = arr[1]
    r = sec_digit//firt_dig
    for i in range(l-1):
        if not (arr[i+1]// arr[i]) == r:
            return False
    return True




if __name__ == "__main__":
    ar = [2,4,6,7,10,12]
    print(airth_geo_II(ar))
    ar2 = [3, 0, -3, -6, -9]
    print(airth_geo_II(ar2))
    ar3 = [2, 6, 18, 54]
    print(airth_geo_II(ar3))
