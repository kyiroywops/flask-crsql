import dao.users as dao

def listar():
    return dao.listar()

class Usuario:
    def __init__(self, rut="", nombre="", email="", passwd="", ingreso=""):
        self.rut=rut
        self.nombre=nombre
        self.email=email
        self.password=passwd
        self.ingreso=ingreso
    def __str__(self):
        return f"Rut: {self.rut} \nNombre: {self.nombre} \nEmail: {self.email} \nPassword: {self.password} \nIngreso: {self.ingreso}"

    def getRut(self):
        return self.rut
    def setRut(self, rut):
        self.rut=rut
    def delRut(self):
        pass
    Rut=property(getRut, setRut, delRut)

    def getNombre(self):
        return self.nombre
    def setNombre(self, nom):
        self.nombre=nom
    def delNombre(self):
        pass
    Nombre=property(getNombre, setNombre, delNombre)

    def getEmail(self):
        return self.email
    def setEmail(self, ema):
        self.email=ema
    def delEmail(self):
        pass
    Email=property(getEmail, setEmail, delEmail)

    def getPasswd(self):
        return self.password
    def setPasswd(self, pwd):
        self.password = pwd
    def delPasswd(self):
        pass
    Password=property(getPasswd, setPasswd, delPasswd)

    def getIngreso(self):
        return self.ingreso
    def setIngreso(self, crea):
        self.ingreso = crea
    def delIngreso(self):
        pass
    Ingreso=property(getIngreso, setIngreso, delIngreso)

    def agregar(self):
        dao.agregar(self)

    def buscar(self):
        dao.buscar(self)

    def actualizar(self):
        dao.actualizar(self)

    def eliminar(self):
        dao.eliminar(self)