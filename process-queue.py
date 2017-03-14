# -*- coding: utf-8 -*-
# Example for queue of multiprocess

import os, time
from multiprocessing import Process, Queue


def worker(q):

    print('This is a worker process.My pid is :%d.' % os.getpid())

    for i in range(5):
        print('Now worker put %d into the queue.' % i)
        q.put(i)
        time.sleep(2)

    print('Worker process end.')


def customer(q):

    print('This is a customer process. My pid is: %d.' % os.getpid())

    while True:
        val = q.get(True)
        print('I get %s from the worker.' % val)


if __name__ == '__main__':

    q = Queue()
    pw = Process(target=worker, args=(q,))
    pc = Process(target=customer, args=(q,))

    pw.start()
    pc.start()

    pw.join()
    pc.terminate()