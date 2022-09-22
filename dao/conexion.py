import sqlite3

def conectar():
    conn=sqlite3.connect("datos.db")
    return conn