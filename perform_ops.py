def perform_ops(A):
    m = len(A)
    n = len(A[0])
    B=[]
    for i in range(m):
        B.append([0]*n)
        for j in range(len(A[i])):
            B[i][n-1-j] = A[i][j]
    return B


if __name__ == '__main__':
    A= [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    B =perform_ops(A)
    print(B)
    for i in range(len(B)):
        for j in range(len(B[i])):
            print((B[i][j]))



