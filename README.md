# Veterinaria Huella Feliz

¡Bienvenido al sistema de gestión de la Veterinaria Huella Feliz! Este proyecto es una aplicación de consola en Python diseñada para gestionar clientes, mascotas, citas y servicios en una veterinaria. El sistema utiliza conceptos avanzados de programación orientada a objetos (POO) como clases abstractas, herencia, polimorfismo, encapsulamiento, factory y decoradores, además de ofrecer una interacción exclusiva por terminal.

---

## Características principales

### 1) Requerimientos funcionales
- **Registro de clientes**: Permite registrar nuevos clientes con su nombre y teléfono.
- **Registro de mascotas**: Permite registrar mascotas asociadas a un cliente, incluyendo nombre, especie y raza.
- **Gestión de citas**: Permite programar, cancelar y visualizar citas para las mascotas.
- **Historial de servicios**: Mantiene un registro de los servicios realizados a cada mascota.
- **Persistencia de datos**: Guarda y carga los datos en un archivo JSON para mantener la información entre sesiones.

### 2) Gestión de clientes y mascotas
- **Clientes**: Los clientes pueden registrarse en el sistema con su nombre y teléfono. Cada cliente puede tener una o más mascotas asociadas.
- **Mascotas**: Las mascotas se registran con su nombre, especie y raza. Cada mascota tiene un historial de servicios que se puede consultar.

### 3) Gestión de citas
- **Programación de citas**: Permite programar citas para una mascota, indicando la fecha y el servicio a realizar.
- **Cancelación de citas**: Permite cancelar citas existentes.
- **Visualización de citas**: Muestra todas las citas programadas.

### 4) Historial de servicios
- Cada mascota tiene un historial de servicios que registra todos los servicios realizados.
- El historial se puede consultar en cualquier momento para ver los servicios anteriores.

### 5) Interacción exclusivamente por terminal
- El sistema se maneja completamente a través de una interfaz de terminal, con un menú interactivo que guía al usuario en cada paso.

### 6) Factory
- Se utiliza un patrón **Factory** para la creación de citas, lo que permite validar y crear instancias de citas de manera controlada.

### 7) Decoradores
- Se implementa un **decorador** para validar el formato de la fecha al programar una cita, asegurando que cumpla con el formato `YYYY-MM-DD`.

### 8) Clases abstractas
- Se utiliza una **clase abstracta** (`HistorialServicio`) para definir la estructura base del historial de servicios, permitiendo la implementación de métodos abstractos como `agregar_servicio` y `mostrar_historial`.

### 9) Encapsulamiento
- Los atributos de las clases están encapsulados, y se accede a ellos mediante métodos, garantizando el control sobre cómo se modifican o consultan los datos.

### 10) Herencia
- La clase `HistorialMascota` hereda de la clase abstracta `HistorialServicio`, implementando los métodos requeridos para gestionar el historial de servicios.

### 11) Polimorfismo
- El método `mostrar_historial` de la clase `HistorialMascota` es un ejemplo de polimorfismo, ya que implementa la funcionalidad definida en la clase abstracta `HistorialServicio`.

### 12) Entrada y validación
- El sistema valida las entradas del usuario, como el formato de la fecha y la existencia de clientes y mascotas, para evitar errores y garantizar la integridad de los datos.

---

## Requisitos

- Python 3.x

---
## Repositorio
   ```bash
  https://github.com/Danitech97/RETO-2-PYTHON.git
