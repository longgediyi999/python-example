from multiprocessing import Process, Pipe
import time


def f(conn):
    time.sleep(2)
    conn.send([42, None, 'hello'])
    conn.close()


if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    p.join()
    print(parent_conn.recv())