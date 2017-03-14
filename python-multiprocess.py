#  -*- coding: utf-8 -*-
# Example for multiprocessing

from multiprocessing import Process
import os, time, psutil


def child(i):
    print("I'm a child process of %d and my pid is: %d and my name is:%d" % (os.getppid(),os.getpid(),i))
    time.sleep(2)
    print('%d is end.' % i)
    print(psutil.pid_exists(os.getpid()))


if __name__ == '__main__':
    for i in range(5):
        p = Process(target=child,args=(i,))
        p.start()
    print('This is main process.')
