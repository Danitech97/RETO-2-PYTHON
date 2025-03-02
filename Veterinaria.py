import json
from abc import ABC, abstractmethod
from datetime import datetime
from os import path

# Clase abstracta para el historial de servicios
class HistorialServicio(ABC):
    @abstractmethod
    def agregar_servicio(self, servicio):
        pass

    @abstractmethod
    def mostrar_historial(self):
        pass

# Clase para gestionar clientes
class Cliente:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono
        self.mascotas = []

    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)

    def __str__(self):
        return f"Cliente: {self.nombre}, Teléfono: {self.telefono}"

# Clase para gestionar mascotas
class Mascota:
    def __init__(self, nombre, especie, raza):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.historial = HistorialMascota()

    def __str__(self):
        return f"Mascota: {self.nombre}, Especie: {self.especie}, Raza: {self.raza}"

# Clase para el historial de mascotas
class HistorialMascota(HistorialServicio):
    def __init__(self):
        self.servicios = []

    def agregar_servicio(self, servicio):
        self.servicios.append(servicio)

    def mostrar_historial(self):
        if not self.servicios:
            print("No hay servicios registrados.")
        else:
            for servicio in self.servicios:
                print(f" - {servicio}")

# Clase para gestionar citas
class Cita:
    def __init__(self, cliente, mascota, fecha, servicio):
        self.cliente = cliente
        self.mascota = mascota
        self.fecha = fecha
        self.servicio = servicio

    def __str__(self):
        return f"Cita: {self.fecha}, Cliente: {self.cliente.nombre}, Mascota: {self.mascota.nombre}, Servicio: {self.servicio}"

# Decorador para validar la fecha de la cita
def validar_fecha(func):
    def wrapper(*args, **kwargs):
        fecha = args[2]
        try:
            datetime.strptime(fecha, "%Y-%m-%d")
            return func(*args, **kwargs)
        except ValueError:
            print("Error: Formato de fecha incorrecto. Use YYYY-MM-DD.")
    return wrapper

# Factory para crear citas
class CitaFactory:
    @staticmethod
    @validar_fecha
    def crear_cita(cliente, mascota, fecha, servicio):
        return Cita(cliente, mascota, fecha, servicio)

# Clase principal para gestionar la veterinaria
class Veterinaria:
    def __init__(self):
        self.clientes = []
        self.citas = []

    def agregar_cliente(self, cliente):
        if any(c.nombre == cliente.nombre for c in self.clientes):
            print("Error: Ya existe un cliente con ese nombre.")
        else:
            self.clientes.append(cliente)
            print(f"Cliente {cliente.nombre} registrado con éxito.")

    def buscar_cliente(self, nombre):
        for cliente in self.clientes:
            if cliente.nombre == nombre:
                return cliente
        print("Error: Cliente no encontrado.")
        return None

    def agregar_cita(self, cita):
        self.citas.append(cita)
        print(f"Cita para {cita.mascota.nombre} registrada con éxito.")

    def cancelar_cita(self, fecha, nombre_mascota):
        cita_a_cancelar = None
        for cita in self.citas:
            if cita.fecha == fecha and cita.mascota.nombre == nombre_mascota:
                cita_a_cancelar = cita
                break
        if cita_a_cancelar:
            self.citas.remove(cita_a_cancelar)
            print(f"Cita del {fecha} para {nombre_mascota} cancelada.")
        else:
            print("Error: Cita no encontrada.")

    def mostrar_clientes(self):
        if not self.clientes:
            print("No hay clientes registrados.")
        else:
            for cliente in self.clientes:
                print(cliente)
                for mascota in cliente.mascotas:
                    print(f"  {mascota}")

    def mostrar_citas(self):
        if not self.citas:
            print("No hay citas programadas.")
        else:
            for cita in self.citas:
                print(cita)

    def guardar_datos(self, archivo):
        datos = {
            "clientes": [
                {
                    "nombre": c.nombre,
                    "telefono": c.telefono,
                    "mascotas": [
                        {
                            "nombre": m.nombre,
                            "especie": m.especie,
                            "raza": m.raza,
                            "historial": m.historial.servicios
                        }
                        for m in c.mascotas
                    ]
                }
                for c in self.clientes
            ],
            "citas": [
                {
                    "cliente": c.cliente.nombre,
                    "mascota": c.mascota.nombre,
                    "fecha": c.fecha,
                    "servicio": c.servicio
                }
                for c in self.citas
            ]
        }
        with open(archivo, "w") as f:
            json.dump(datos, f, indent=4)
        print(f"Datos guardados en {archivo}.")

    def cargar_datos(self, archivo):
        if not path.exists(archivo):
            print("Error: Archivo no encontrado.")
            return
        with open(archivo, "r") as f:
            datos = json.load(f)
        for cliente_data in datos["clientes"]:
            cliente = Cliente(cliente_data["nombre"], cliente_data["telefono"])
            for mascota_data in cliente_data["mascotas"]:
                mascota = Mascota(mascota_data["nombre"], mascota_data["especie"], mascota_data["raza"])
                mascota.historial.servicios = mascota_data["historial"]
                cliente.agregar_mascota(mascota)
            self.clientes.append(cliente)
        for cita_data in datos["citas"]:
            cliente = self.buscar_cliente(cita_data["cliente"])
            if cliente:
                mascota = next((m for m in cliente.mascotas if m.nombre == cita_data["mascota"]), None)
                if mascota:
                    cita = CitaFactory.crear_cita(cliente, mascota, cita_data["fecha"], cita_data["servicio"])
                    if cita:
                        self.citas.append(cita)
        print(f"Datos cargados desde {archivo}.")

# Menú interactivo
def menu():
    veterinaria = Veterinaria()
    archivo_datos = "veterinaria_data.json"

    while True:
        print("\n----- BIENVENIDA A LA VETERINARIA HUELLA FELIZ -----")
        print("1. Registrar cliente")
        print("2. Registrar mascota")
        print("3. Gestion de citas")
        print("4. Historial")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del cliente: ")
            telefono = input("Teléfono del cliente: ")
            cliente = Cliente(nombre, telefono)
            veterinaria.agregar_cliente(cliente)

        elif opcion == "2":
            nombre_cliente = input("Nombre del cliente: ")
            cliente = veterinaria.buscar_cliente(nombre_cliente)
            if cliente:
                nombre_mascota = input("Nombre de la mascota: ")
                especie = input("Especie de la mascota: ")
                raza = input("Raza de la mascota: ")
                mascota = Mascota(nombre_mascota, especie, raza)
                cliente.agregar_mascota(mascota)
                print(f"Mascota {nombre_mascota} registrada con éxito.")
            else:
                print("Error: Cliente no encontrado.")

        elif opcion == "3":
            print("\n----- GESTION DE CITAS -----")
            print("1. Programar cita")
            print("2. Cancelar cita")
            print("3. Mostrar citas programadas")
            print("4. Mostrar clientes y mascotas")
            print("5. Volver al menu principal")
            
            sub_opcion = input("Seleccione una opcion: ")
            if sub_opcion == "1":
                nombre_cliente = input("Nombre del cliente: ")
                cliente = veterinaria.buscar_cliente(nombre_cliente)
                if cliente:
                    nombre_mascota = input("Nombre de la mascota: ")
                    mascota = next((m for m in cliente.mascotas if m.nombre == nombre_mascota), None)
                    if mascota:
                        fecha = input("Fecha de la cita (YYYY-MM-DD): ")
                        servicio = input("Servicio a realizar: ")
                        cita = CitaFactory.crear_cita(cliente, mascota, fecha, servicio)
                        if cita:
                            veterinaria.agregar_cita(cita)
                    else:
                        print("Error: Mascota no encontrada.")
            elif sub_opcion == "2":
                fecha = input("Fecha de la cita a cancelar (YYYY-MM-DD): ")
                nombre_mascota = input("Nombre de la mascota: ")
                veterinaria.cancelar_cita(fecha, nombre_mascota)
            elif sub_opcion == "3":
                veterinaria.mostrar_citas()
            elif sub_opcion == "4":
                veterinaria.mostrar_clientes()
            elif sub_opcion == "5":
                continue
            else:
                print("Opción no válida. Intente de nuevo.")

        elif opcion == "4":
            nombre_cliente = input("Nombre del cliente: ")
            cliente = veterinaria.buscar_cliente(nombre_cliente)
            if cliente:
                nombre_mascota = input("Nombre de la mascota: ")
                mascota = next((m for m in cliente.mascotas if m.nombre == nombre_mascota), None)
                if mascota:
                    print(f"\nHistorial de servicios de {nombre_mascota}:")
                    mascota.historial.mostrar_historial()
                else:
                    print("Error: Mascota no encontrada.")
            else:
                print("Error: Cliente no encontrado.")

        elif opcion == "5":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()