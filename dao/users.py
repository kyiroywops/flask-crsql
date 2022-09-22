import dao.conexion
import modelo.users as model

def conectar():
    conn = dao.conexion.conectar()
    return conn

# C
def agregar(u):
        sql="""insert into usuario (rut,nombre,email,password,ingreso) values (?,?,?,?,?)"""
        conn=conectar()
        cmd=conn.cursor()
        datos = [u.rut,u.nombre,u.email,u.password,u.ingreso]
        print(datos)
        cmd.executemany(sql,datos)
        cmd.close()
        conn.commit()

# R
def buscar(u):
    sql="select rut, nombre, email, password, ingreso from usuario where rut='" + u.Rut + "'"
    u.Rut=None
    conn = conectar()
    cmd = conn.cursor()
    cmd.execute(sql)
    lista=cmd.fetchall()
    cmd.close()
    conn.commit()
    if len(lista) > 0:
        tupla=lista[0]
        u.Rut=tupla[0]
        u.Nombre=tupla[1]
        u.Email=tupla[2]
        u.Password=tupla[3]
        u.Ingreso=tupla[4]

# U
def actualizar(u):
    sql="""update usuario set nombre=?, email=?, password=?, ingreso=? where rut=?"""
    conn = conectar()
    cmd = conn.cursor()
    datos = [u.nombre,u.email,u.password,u.ingreso,u.rut]
    cmd.execute(sql,datos)
    cmd.close()
    conn.commit()

# D
def eliminar(u):
    sql="delete from usuario where rut='" + u.Rut + "'"
    conn = conectar()
    cmd = conn.cursor()
    cmd.execute(sql)
    cmd.close()
    conn.commit()

def listar():
    sql="select * from usuario"
    conn = conectar()
    cmd = conn.cursor()
    cmd.execute(sql)
    lisUsers=cmd.fetchall()
    cmd.close()
    conn.commit()
    return lisUsers