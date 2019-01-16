from multiprocessing import Pool
from multiprocessing import Process

# https://docs.python.org/3/library/multiprocessing.html#multiprocessing-programming
# First example is using the Pool object, which is a way of parallelizing
# the execution of a function across multiple input values, distributing
# the input data across processes (data parallelism).

# def f(x):
#     return x*x
#
#
# print(__name__)
# if __name__ == '__main__':
#     with Pool(5) as p:
#         print(p.map(f, (1, 2, 3)))  # also works with [1, 2, 3]


def f(name):
    print('hello', name)


if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
