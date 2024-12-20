from typing import List


class Solution:
	def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
		c_matrix = list(zip(*matrix))
		M, N = len(matrix), len(matrix[0])
		for c in range(N):
			for r in range(M):
				if matrix[r][c] == -1:
					matrix[r][c] = max(c_matrix[c])
		return matrix
