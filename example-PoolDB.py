import threading, time
import cx_Oracle
from DBUtils.PooledDB import PooledDB


def func_ora_mkdsn(host, port, sid):
    dsn = cx_Oracle.makedsn(host, port, sid)
    return dsn


def worker(pool, i):
    print('I am the worker of %d.' % i)
    conn = pool.connection()
    print('I am the worker of %d. I get the connection.' % i)
    cur = conn.cursor()
    rs = cur.execute("select username,status,module from v$session where username='TEST'")
    print(rs.fetchall())
    time.sleep(5)
    print('I am the worker of %d. I release the connection.' % i)
    cur.close()
    conn.close()


if __name__ == '__main__':
    dsn = func_ora_mkdsn('x.x.x.x', '1521', 'sid')
    pool = PooledDB(creator=cx_Oracle, user='test', password='test', dsn=dsn, mincached=2, maxcached=5, maxconnections=5, blocking=True)
    for i in range(20):
        p = threading.Thread(target=worker, args=(pool,i))
        p.start()