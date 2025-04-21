# 54. Spiral Matrix
class Solution:
    def spiralOrder(self, matrix):
        acc = []

        self.start_order(matrix, acc)

        return acc

    def start_order(self, matrix, acc):
        self.slice_top(matrix, acc)

    def slice_top(self, matrix, acc):
        if len(matrix) != 0:
            acc += matrix[0]
            matrix.pop(0)
            
            self.slice_right(matrix, acc)


    def slice_right(self, matrix, acc):
        for item in matrix:
            if len(item) > 0:
                acc.append(item.pop())

        self.slice_bottom(matrix, acc)

    def slice_bottom(self, matrix, acc):
        if len(matrix) != 0:
            acc += reversed(matrix.pop())
            
            self.slice_left(matrix, acc)

    def slice_left(self, matrix, acc):
        tmp = []
        for item in matrix:
            if len(item) > 0:
                tmp.append(item.pop(0))

        acc += reversed(tmp)
        self.slice_top(matrix, acc)

            
# [
#     [01,02,03,04],
#     [05,06,07,08],
#     [09,10,11,12],
#     [13,14,15,16],
#     [17,18,19,20],
#     [21,22,23,24]
# ]