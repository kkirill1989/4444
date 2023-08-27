#Создайте класс Матрица. Добавьте методы для: вывода на печать, сравнения, сложения, *умножения матриц

from copy import deepcopy as d

class Matrix:
    """Класс для вывода на печать, сравнения и сложения матриц"""

    def __init__(self, matrix: list) -> None:
        """Создание экземпляра класса Matrix из списка списков"""
        self.matrix = matrix

    def show_matrix(self):
        """Вывод матрицы в консоль"""
        mat = ""
        for i in range(len(self.matrix)):
            mat = mat + '\t'.join(map(str,self.matrix[i])) + "\n"
        return mat
    
    def comparison(self, other):
        """Сравнение матриц"""
        result = ""
        if self.matrix < other.matrix: result = "Вторая матрица больше первой"
        elif self.matrix > other.matrix: result = "Первая матрица больше второй"
        else: result = "Матрицы равны"
        return result

    def __add__(self, other):
        """Сложение матриц"""
        result = []
        nums = []
        for i in range(len(self.matrix)): 
            for j in range(len(self.matrix[i])):
                summa = self.matrix[i][j] + other.matrix[i][j]
                nums.append(summa)
                if len(nums) == len(self.matrix[i]):
                    result.append(nums)
                    nums = []
        return result

if __name__ == "__main__":
    m1 = Matrix([[1, 2, 3], [4, 5, 6]])
    print(m1.show_matrix())
    m2 = Matrix([[7, 8, 9], [1, 2, 3]])
    print(m2.show_matrix())
    ms = m1 + m2
    print(ms)
    m3 = Matrix([[7, 8, 9], [1, 2, 3], [3, 4, 6]])
    m4 = Matrix([[7, 8, 9], [1, 2, 3]])
    mc = m4.comparison(m2)
    print(mc)