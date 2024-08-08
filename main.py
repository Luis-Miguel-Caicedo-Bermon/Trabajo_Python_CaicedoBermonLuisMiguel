import json
def Abrircompras():
    datos=[]
    with open("ventas.json", encoding="utf8") as openfile:
        datos=json.load(openfile)
        return datos

def guardarcompras(midato):
    with open("ventas.json", "w") as mifile:
        json.dump(midato,mifile)
def AbrirEmpleados():
    datos=[]
    with open("ventas.json", encoding="utf8") as openfile:
        datos=json.load(openfile)
        return datos

def guardarEmpleados(midato):
    with open("ventas.json", "w") as mifile:
        json.dump(midato,mifile)
def AbrirMedicamentos():
    datos=[]
    with open("ventas.json", encoding="utf8") as openfile:
        datos=json.load(openfile)
        return datos

def guardarMedicamentos(midato):
    with open("ventas.json", "w") as mifile:
        json.dump(midato,mifile)
def AbrirPacientes():
    datos=[]
    with open("ventas.json", encoding="utf8") as openfile:
        datos=json.load(openfile)
        return datos

def guardarPacientes(midato):
    with open("ventas.json", "w") as mifile:
        json.dump(midato,mifile)
def AbrirProveedores():
    datos=[]
    with open("ventas.json", encoding="utf8") as openfile:
        datos=json.load(openfile)
        return datos

def guardarProveedores(midato):
    with open("ventas.json", "w") as mifile:
        json.dump(midato,mifile)
def AbrirVentas():
    datos=[]
    with open("ventas.json", encoding="utf8") as openfile:
        datos=json.load(openfile)
        return datos

def guardarVentas(midato):
    with open("ventas.json", "w") as mifile:
        json.dump(midato,mifile)