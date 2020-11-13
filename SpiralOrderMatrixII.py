class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        # გაჭირვება მაჩვენე და გაქცევას გაჩვენებ ;დ
        result = []
        for i in range(A):
            result.append([0] * A)
        dir = 0
        cnt = 0
        i = 0
        j = 0
        while cnt < A * A:
            if dir == 0:
                while True:
                    if j == A or result[i][j] != 0:
                        j -= 1
                        break
                    result[i][j] = cnt + 1
                    cnt += 1
                    j += 1
                dir = 1
                i += 1
            elif dir == 1:
                while True:
                    if i == A or result[i][j] != 0:
                        i -= 1
                        break
                    result[i][j] = cnt + 1
                    cnt += 1
                    i += 1
                j -= 1
                dir = 2
            elif dir == 2:
                while True:
                    if j == -1 or result[i][j] != 0:
                        j += 1
                        break
                    result[i][j] = cnt + 1
                    cnt += 1
                    j -= 1
                i -= 1
                dir = 3
            elif dir == 3:
                while True:
                    if i == -1 or result[i][j] != 0:
                        i += 1
                        break
                    result[i][j] = cnt + 1
                    cnt += 1
                    i -= 1
                j += 1
                dir = 0
        return result
