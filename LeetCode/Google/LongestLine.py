def transform(mat):
  for i in range(len(mat)):
		for j in range(len(mat[i])):
			mat[i][j] = [mat[i][j], mat[i][j], mat[i][j], mat[i][j]]


class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        result = 0
        transform(mat)
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                h = mat[i][j][0]
                v = mat[i][j][1]
                ld = mat[i][j][2]
                rd = mat[i][j][3]
                if j > 0 and h == 1:
                    h += mat[i][j - 1][0]
                if i > 0 and v == 1:
                    v += mat[i - 1][j][1]
                if i > 0 and j > 0 and ld == 1:
                    ld += mat[i - 1][j - 1][2]
                if i > 0 and j < len(mat[0]) - 1 and rd == 1:
                    rd += mat[i - 1][j + 1][3]
                mat[i][j] = [h, v, ld, rd]
                result = max(result, h, v, ld, rd)
        return result
