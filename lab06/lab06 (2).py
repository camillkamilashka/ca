import itertools
def count_ones():
    expression = 4**511 + 2**511 - 511
    binary = bin(expression)[2:]  # преобразование в двоичную запись
    count = binary.count('1')  # подсчет количества единиц
    return count

print(count_ones())