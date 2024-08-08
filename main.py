import json
from datetime import datetime,timezone
def Abrircompras():
    datos=[]
    with open("Compras.json", encoding="utf8") as openfile:
        datos=json.load(openfile)
        return datos

def guardarcompras(midato):
    with open("Compras.json", "w") as mifile:
        json.dump(midato,mifile)
def AbrirEmpleados():
    datos=[]
    with open("Empleados.json", encoding="utf8") as openfile:
        datos=json.load(openfile)
        return datos

def guardarEmpleados(midato):
    with open("Empleados.json", "w") as mifile:
        json.dump(midato,mifile)
def AbrirMedicamentos():
    datos=[]
    with open("Medicamentos.json", encoding="utf8") as openfile:
        datos=json.load(openfile)
        return datos

def guardarMedicamentos(midato):
    with open("Medicamentos.json", "w") as mifile:
        json.dump(midato,mifile)
def AbrirPacientes():
    datos=[]
    with open("Pacientes.json", encoding="utf8") as openfile:
        datos=json.load(openfile)
        return datos

def guardarPacientes(midato):
    with open("Pacientes.json", "w") as mifile:
        json.dump(midato,mifile)
def AbrirProveedores():
    datos=[]
    with open("Proveedores.json", encoding="utf8") as openfile:
        datos=json.load(openfile)
        return datos

def guardarProveedores(midato):
    with open("Proveedores.json", "w") as mifile:
        json.dump(midato,mifile)
def AbrirVentas():
    datos=[]
    with open("Ventas.json", encoding="utf8") as openfile:
        datos=json.load(openfile)
        return datos

def guardarVentas(midato):
    with open("Ventas.json", "w") as mifile:
        json.dump(midato,mifile)

def menu():
    print("------Menú------\n"
          "1. ventas\n"
          "2. compras\n"
          "3. salir\n")
bucle=True
while bucle==True:
    menu()
    opc=int(input("Selecciona una opción: "))
    if opc==1:
        empleados=AbrirEmpleados()
        medicamentos=AbrirMedicamentos()
        ventas=AbrirVentas()
        pacientes=AbrirPacientes()
        print("----------VENTAS----------")
        print("informacion del paciente")
        nombre_paciente=input("ingresa el nombre: ")
        direccion_paciente=input("ingrese la direccion del paciente: ")
        numero_paciente=input("Ingresa el numero del paciente: ")
        print("Empleados")
        for i in empleados:
            print("-----------------------------")
            print("Nombre: ", i["nombre"])
            print("-----------------------------")
        
        bucle2=True
        while bucle2==True:
            nombre_empleado=input("Escribe el nombre del empleado que realizo la venta\n")
            for i in empleados:
                if i["nombre"]==nombre_empleado:
                    cargo=i["cargo"]
                    bucle2=False
        for i in medicamentos:
            print("-----------------------------")
            print("Nombre: ", i["nombre"])
            print("-----------------------------")
        
        bucle3=True
        while bucle3==True:
            nombre_medicamento=input("Escribe el nombre del medicamento: ")
            for i in medicamentos:
                if i["nombre"]==nombre_medicamento:
                    bucle4=True
                    while bucle4==True:
                        cantidad=int(input("cuanto quieres de este producto: "))
                        if i["stock"]>=cantidad:
                            i["stock"]=i["stock"]-cantidad
                            precio=i["precio"]
                            bucle4=False
                    bucle3=False
        fecha=datetime.now(timezone.utc)
        fecha_organizada=fecha.strftime("%Y-%m-%dT%H:%M:%SZ")
        ventas.append({"fechaVenta":fecha_organizada,"paciente":{"nombre":nombre_paciente,"direccion":direccion_paciente},
                       "empleado":{"nombre":nombre_empleado, "cargo":cargo},"medicamentosVendidos":{"nombreMedicamento":nombre_medicamento,"cantidadVendida":cantidad,"precio":precio}})
        pacientes.append({"nombre":nombre_paciente,"direccion":direccion_paciente,"telefono":numero_paciente})
        guardarMedicamentos(medicamentos)
        guardarVentas(ventas)
        guardarPacientes(pacientes)
    
    if opc==2:
        compras=Abrircompras()
        medicamentos=AbrirMedicamentos()
        proveedores=AbrirProveedores()
        print("--------COMPRAR--------")
        print("Información del proveedor")
        nombre_proveedor=input("Nombre: ")
        contacto_proveedor=input("Contacto: ")
        direccion_proveedor=input("Dirección: ")
        for i in medicamentos:
            print("-----------------------------")
            print("Nombre: ", i["nombre"])
            print("-----------------------------")
        bucle3=True
        while bucle3==True:
            nombre_medicamento=input("Escribe el nombre del medicamento: ")
            for i in medicamentos:
                if i["nombre"]==nombre_medicamento:
                    cantidad=int(input("cuanto quieres de este producto: "))
                    i["stock"]+=cantidad
                    bucle3=False
        precio_compra=int(input("Precio: "))
        fecha=datetime.now(timezone.utc)
        fecha_organizada=fecha.strftime("%Y-%m-%dT%H:%M:%SZ")
        compras.append({"fechaCompra":fecha_organizada,"proveedor":{"nombre":nombre_proveedor,"contacto":contacto_proveedor},
                        "medicamentosComprados":[{"nombreMedicamento":nombre_medicamento,"cantidadComprada":cantidad,"precioCompra":precio_compra}]})
        proveedores.append({"nombre":nombre_proveedor,"contacto":contacto_proveedor,"direccion":direccion_proveedor})
        guardarcompras(compras)
        guardarProveedores(proveedores)
        guardarMedicamentos(medicamentos)
    if opc==3:
        bucle=False