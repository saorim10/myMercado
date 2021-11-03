import pymysql


conn = pymysql.connect(
        user='root',
        password='root',
        host='127.0.0.1',
        db='mymercado'
    )
cursor = conn.cursor()


def conectar():
    conn = pymysql.connect(
        user='root',
        password='root',
        host='127.0.0.1',
        db='mymercado'
    )

    cursor = conn.cursor()
    return conn, cursor


def desconectar():
    cursor.close()
    conn.close()
