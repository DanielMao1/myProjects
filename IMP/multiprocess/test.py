import multiprocessing as mp

# def f(x):
#     return x*x
#
# if __name__=='__main__':
#     with Pool(5) as p:
#         print(p.map(f,[1,2,3]))

# def f(name):
#     print('hello', name)
#
# if __name__ == '__main__':
#     p = mp.Process(target=f, args=('bob',))
#     p.start()
#     p.join()
import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print('hello', name)

if __name__ == '__main__':
    info('main line')
    p = mp.Process(target=f, args=('bob',))
    p.start()
    p.join()