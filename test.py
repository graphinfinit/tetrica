
"""
Сложность - log2(n) двоичный логарифм от длины строки
в моих условиях 0.035204786 сек
"""

array = "111111111111111111111111100000000"
def task1(array):
    start = 0
    end = len(array)-1
    index = 0
    while start <= end:
        m = (start+end)//2
        if array[m] == '0':
            end = m - 1
            index = m
        else:
            start = m + 1
    return index

print(task1(array))





