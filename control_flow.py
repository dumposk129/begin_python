# if Statements
# x = int(input("Please enter an integer "))
# print(x)
# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')

# for Statements
# words = ['cat', 'windows', 'defenestrate']
# for w in words:
#     print(w, len(w))

# break and continue Statements and else Clauses on Loops
# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#         else:
#             # loop fell through without finding a factor
#             print(n, 'is a prime number')

# Defining Function
# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a + b
#
# print(fib(2000))
#
# # List
# print(list(range(3, 6)))

# Lambda Expression
# def make_incrementor(n):
#     return lambda x: x + n
# f = make_incrementor(42)
# print(f(0))

# pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
# pairs.sort(key = lambda pair: pair[1])
# print(pairs)
