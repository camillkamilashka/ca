import matplotlib.pyplot as plt
import numpy as np

# графики по урокам из книги

# 1
# plt.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
# plt.show()

# 2
# x = np.linspace(0, 10, 50)
# y1 = x
#
# y2 = [i**2 for i in x]
#
# plt.title('Зависимости: у1 = хб у2 = х^2')
# plt.xlabel('x')
# plt.ylabel('y1, y2')
# plt.grid()
# plt.plot(x, y1, x, y2)
#
# plt.show()

# 3
# fruits = ['apple', 'peach', 'orange', 'banana', 'melon']
# counts = [34, 25, 43, 31, 17]
# plt.bar(fruits, counts)
# plt.title('Fruits!')
# plt.xlabel('Fruit')
# plt.ylabel('Count')
#
# plt.show()

# 4
# x = [1, 5, 10, 15, 20]
# y = [1, 7, 3, 5, 11]
# plt.plot(x, y, label='steel price')
# plt.title('Chart price', fontsize=15)
# plt.xlabel('Day', fontsize=12, color='blue')
# plt.ylabel('Price', fontsize=12, color='blue')
# plt.legend()
# plt.grid(True)
# plt.text(15, 4, 'grow up!')
#
# plt.show()

# 5
# x = [1, 5, 10, 15, 20]
# y = [1, 7, 3, 5, 11]
#
# fig,  axs = plt.subplots(2, 2, figsize=(12, 7))
# axs[0, 0].plot(x, y, '-')
# axs[0, 1].plot(x, y, '--')
# axs[1, 0].plot(x, y, '-.')
# axs[1, 1].plot(x, y, ':')
#
# plt.show()

# 6
x = [1, 5, 10, 15, 20]
y1 = [1, 7, 3, 5, 11]
y2 = [4, 3, 1, 8, 12]

line1 = plt.plot(x, y1, 'o-b')
line2 = plt.plot(x, y2, 'o-.m')
plt.legend((line2, line1), ['L2', 'L1'])

plt.show()
