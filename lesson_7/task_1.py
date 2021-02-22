class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        massive = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        for i in range(len(self.list_1)):

            for j in range(len(self.list_2[i])):
                massive[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in massive]))

    def __str__(self, massive=None):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in massive]))


my_matrix = Matrix([[5, 8, 13],
                    [21, 34, 55],
                    [89, 144, 233]],
                   [[3, 19, 11],
                    [9, 15, 25],
                    [69, 31, 168]])

print(my_matrix.__add__())
