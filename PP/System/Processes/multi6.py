'''
Плюс многое другое: пулы процессов, менеджеры, блокировки,
условные переменные,...
'''
import os
from multiprocessing import Pool
def powers(x):
    print(os.getpid()) # раскомментируйте, чтобы увидеть работу потомков
    return 2 ** x
if __name__ == '_main__':
    workers = Pool(processes=5)
    results = workers.map(powers, [2]*100)
    print(results[:16])
    print(results[-2:])
    results = workers.map(powers, range(100))
    print(results[:16])
    print(results[-2:])
