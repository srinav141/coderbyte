def fact_test(num):
    if num == 1:
        return 1
    return num * fact_test(num-1)

if __name__ == "__main__":
    r = fact_test(8)
    print(r)