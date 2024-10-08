class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        trans = [[-1 for i in range(len(matrix))] for j in range(len(matrix[0]))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                trans[j][i] = matrix[i][j]
        return trans