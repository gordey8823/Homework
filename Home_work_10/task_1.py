from typing import List


class Matrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        el = self.matrix[0]
        for elem in self.matrix:
            if len(elem) != len(el):
                raise ValueError('fail initialization matrix')

    def __str__(self):
        return str('\n'.join([f"| {' '.join([str(el) for el in i])} |" for i in self.matrix]))

    def __add__(self, other):
        for i in range(len(self.matrix)):
            for i_2 in range(len(other.matrix[i])):
                self.matrix[i][i_2] = self.matrix[i][i_2] + other.matrix[i][i_2]
        return Matrix.__str__(self)


if __name__ == '__main__':
    first_matrix = Matrix([[1, 2], [3, 4], [5, 6]])
    second_matrix = Matrix([[6, 5], [4, 3], [2, 1]])
    print(first_matrix)
    print(second_matrix)
    # """
    # | 1 2 |
    # | 3 4 |
    # | 5 6 |
    # """
    print(first_matrix + second_matrix)
    # """
    # | 7 7 |
    # | 7 7 |
    # | 7 7 |
    # """
    # fail_matrix = Matrix([[1, 2], [3, 4, 7], [5, 6]])
    """
    Traceback (most recent call last):
      ...
    ValueError: fail initialization matrix
    """
