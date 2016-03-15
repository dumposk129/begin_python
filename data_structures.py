# Tutorial method in data structures
# a = [66.25, 333, 333, 1, 1234.5]
# print(a.count(333), a.count(66.25), a.count('x'))
# a.insert(2, -1)
# print(a)
# a.append(333)
# print(a)
# a.index(66.25)
# print(a)
# a.remove(1)
# print(a)
# a.reverse()
# print(a)
# a.sort()
# print(a)
# a.pop()
# print(a)


# List as Stacks
# stack = [3,4,5,6]
# stack.append(7)
# print(stack)
# stack.pop()
# print(stack)


# Lists as Queues
# from collections import deque
# queue = deque(["Eric", "John", "Michael"])
# queue.append("Terry")
# queue.append("Graham")
# print(queue.popleft())
#
# print(queue.popleft())
# print(queue)


# List Comprehensions
# squares = []
# for x in range(10):
#     squares.append(x**2)
# print(squares)
# squares = list(map(lambda x: x**2, range(10)))
# print(squares)
# squares = [x**2 for x in range(10)]
# print(squares)

# print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])
# print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x == y])

# combs = []
# for x in [1,2,3]:
#     for y in [3,1,4]:
#         if x != y:
#             combs.append((x, y))
#
# print(combs)

# vec = [-4, -2, 0, 2, 4]
# print([x * 2 for x in vec])
#
# print([x for x in vec if x >= 0])
# print([x for x in vec if x <= 0])
#
# print([abs(x) for x in vec])

# freshFruit = ['banana', 'loganberry', 'passion fruit']
# print([weapon.strip() for weapon in freshFruit])
# # create a list of 2-tuples like (number, square)
# print([(x, x ** 2) for x in range(6)])
# vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print([num for elem in vec for num in elem])


# matrix = [
#     [1, 2, 3, 4, 5],
#     [5, 6, 7, 8, 10],
#     [9, 10, 11, 12, 0],
#     [13, 14, 15, 16, 8]
# ]
# print([[row[i] for row in matrix] for i in range(4)])
# transposed = []
# for i in range(4):
#     transposed.append([row[i] for row in matrix])
#
# print(transposed)

# print(list(zip(*matrix)))


# Delete delete statement
# a = [-1, 1, 66.25, 333, 333, 1234.5]
# del a[0]
# print(a)

# empty = ()
# singleton = 'hello'
# print(len(empty))
# print(len(singleton))


# Set
# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# print(basket)
# print('orange' in basket)
# print('carrot' in basket)
# a = set('abracadabra')
# b = set('alacazam')
# print(a)        # unique letters in a
# print(a - b)    # letters in a but not in b
# print(a | b)    # letters in either a or b
# print(a & b)    # letters in both a and b
# print(a ^ b)    # letters in a or b but both


# Dictionaries
# tel = {'jack':4098, 'sape':4139}
# tel['guido'] = 4127
# print(tel)
# print(tel['jack'])
#
# print(list(tel.keys()))

# dictation = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
# print(dictation)

# Looping Techniques
# knights = {'gallahad': 'the pure', 'robin': 'the brave'}
# for k, v in knights.items():
#     print(k, v);
#
# for i, v in enumerate(['tic', 'tac', 'toe']):
#     print(i, v)
#
# questions = ['name', 'quest', 'favorite color']
# answer = ['lancelot', 'the holy grail', 'blue']
# for q, a in zip(questions, answer):
#     print('What is your{0}? It is {1}.'.format(q, a))
#
# for i in reversed(range(1, 10, 2)):  # range(start, finish, increase)
#     print(i)
#
# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# for i in sorted(set(basket)):
#     print(i)

# import math
# raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5,
#             float('NaN'), 47.8]
# filtered_data = []
# for value in raw_data:
#     if not math.isnan(value):
#         filtered_data.append(value)
#
# print(filtered_data)