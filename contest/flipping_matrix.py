# for _ in range(int(input().strip())):
#     n = int(input().strip())
#     n2 = 2 * n
#     maxSum = 0
#
#     matrix = [0] * n2
#     for i in range(n2):
#         matrix[i] = [int(x) for x in input().strip().split(' ')]
def flippingMatrix(matrix):
    n2 = 2*n
    matrixSum=0
    for x in range(n):
        for y in range(n):
            matrixSum += max([matrix[x][y],
                           matrix[x][n2 - 1 - y],
                           matrix[n2 - 1 - x][y],
                           matrix[n2 - 1 - x][n2 - 1 - y]])

    return matrixSum
if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        n = int(input().strip())
        matrix = []
        for matrix_i in range(2*n):
            matrix_t = [int(matrix_temp) for matrix_temp in input().strip().split(' ')]
            matrix.append(matrix_t)
        result = flippingMatrix(matrix)
        print(result)

