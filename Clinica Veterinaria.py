import tkinter as tk
from tkinter import messagebox

class Paciente:
    def __init__(self, nombre, especie, raza, edad, propietario):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.propietario = propietario
        self.historial_medico = []

    def agregar_historial_medico(self, consulta):
        self.historial_medico.append(consulta)

class Cita:
    def __init__(self, paciente, fecha, hora, descripcion):
        self.paciente = paciente
        self.fecha = fecha
        self.hora = hora
        self.descripcion = descripcion

class Medicamento:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

class SistemaClinica:
    def __init__(self):
        self.pacientes = []
        self.citas = []
        self.medicamentos = []

    def registrar_paciente(self, nombre, especie, raza, edad, propietario):
        paciente = Paciente(nombre, especie, raza, edad, propietario)
        self.pacientes.append(paciente)

    def programar_cita(self, paciente, fecha, hora, descripcion):
        cita = Cita(paciente, fecha, hora, descripcion)
        self.citas.append(cita)

    def registrar_medicamento(self, nombre, cantidad, precio):
        medicamento = Medicamento(nombre, cantidad, precio)
        self.medicamentos.append(medicamento)

    def generar_informe_pacientes(self):
        informe = "Pacientes:\n"
        for paciente in self.pacientes:
            informe += f"Nombre: {paciente.nombre}, Especie: {paciente.especie}, Raza: {paciente.raza}, Edad: {paciente.edad}, Propietario: {paciente.propietario}\n"
        return informe

    def generar_informe_citas(self):
        informe = "Citas:\n"
        for cita in self.citas:
            informe += f"Paciente: {cita.paciente.nombre}, Fecha: {cita.fecha}, Hora: {cita.hora}, Descripcion: {cita.descripcion}\n"
        return informe

    def generar_informe_medicamentos(self):
        informe = "Medicamentos:\n"
        for medicamento in self.medicamentos:
            informe += f"Nombre: {medicamento.nombre}, Cantidad: {medicamento.cantidad}, Precio: {medicamento.precio}\n"
        return informe

class InterfazGrafica:
    def __init__(self, sistema_clinica):
        self.sistema_clinica = sistema_clinica
        self.ventana = tk.Tk()
        self.ventana.title("Sistema de Gestión de Clínica Veterinaria")

        # Crear menú
        self.menu = tk.Menu(self.ventana)
        self.ventana.config(menu=self.menu)

        # Opción para registrar paciente
        self.menu_pacientes = tk.Menu(self.menu)
        self.menu.add_cascade(label="Pacientes", menu=self.menu_pacientes)
        self.menu_pacientes.add_command(label="Registrar paciente", command=self.registrar_paciente)

        # Opción para programar cita
        self.menu_citas = tk.Menu(self.menu)
        self.menu.add_cascade(label="Citas", menu=self.menu_citas)
        self.menu_citas.add_command(label="Programar cita", command=self.programar_cita)

        # Opción para registrar medicamento
        self.menu_medicamentos = tk.Menu(self.menu)
        self.menu.add_cascade(label="Medicamentos", menu=self.menu_medicamentos)
        self.menu_medicamentos.add_command(label="Registrar medicamento", command=self.registrar_medicamento)

        # Opción para generar informes
        self.menu_informes = tk.Menu(self.menu)
        self.menu.add_cascade(label="Informes", menu=self.menu_informes)
        self.menu_informes.add_command(label="Pacientes", command=lambda: messagebox.showinfo("Informe pacientes", self.sistema_clinica.generar_informe_pacientes()))
        self.menu_informes.add_command(label="Citas", command=lambda: messagebox.showinfo("Informe citas", self.sistema_clinica.generar_informe_citas()))
        self.menu_informes.add_command(label="Medicamentos", command=lambda: messagebox.showinfo("Informe medicamentos", self.sistema_clinica.generar_informe_medicamentos()))

    def registrar_paciente(self):
        ventana_registro = tk.Toplevel(self.ventana)
        ventana_registro.title("Registrar paciente")

        # Entradas para datos del paciente
        tk.Label(ventana_registro, text="Nombre:").pack()
        entrada_nombre = tk.Entry(ventana_registro)
        entrada_nombre.pack()

        tk.Label(ventana_registro, text="Especie:").pack()
        entrada_especie = tk.Entry(ventana_registro)
        entrada_especie.pack()

        tk.Label(ventana_registro, text="Raza:").pack()
        entrada_raza = tk.Entry(ventana_registro)
        entrada_raza.pack()

        tk.Label(ventana_registro, text="Edad:").pack()
        entrada_edad = tk.Entry(ventana_registro)
        entrada_edad.pack()

        tk.Label(ventana_registro, text="Propietario:").pack()
        entrada_propietario = tk.Entry(ventana_registro)
        entrada_propietario.pack()

        # Botón para registrar paciente
        def registrar():
            nombre = entrada_nombre.get()
            especie = entrada_especie.get()
            raza = entrada_raza.get()
            edad = entrada_edad.get()
            propietario = entrada_propietario.get()
            self.sistema_clinica.registrar_paciente(nombre, especie, raza, edad, propietario)
            ventana_registro.destroy()

        tk.Button(ventana_registro, text="Registrar", command=registrar).pack()

    def programar_cita(self):
        ventana_registro = tk.Toplevel(self.ventana)
        ventana_registro.title("Programar cita")

        # Entradas para datos de la cita
        tk.Label(ventana_registro, text="Paciente:").pack()
        entrada_paciente = tk.Entry(ventana_registro)
        entrada_paciente.pack()

        tk.Label(ventana_registro, text="Fecha:").pack()
        entrada_fecha = tk.Entry(ventana_registro)
        entrada_fecha.pack()

        tk.Label(ventana_registro, text="Hora:").pack()
        entrada_hora = tk.Entry(ventana_registro)
        entrada_hora.pack()

        tk.Label(ventana_registro, text="Descripción:").pack()
        entrada_descripcion = tk.Entry(ventana_registro)
        entrada_descripcion.pack()

        # Botón para programar cita
        def programar():
            paciente = entrada_paciente.get()
            fecha = entrada_fecha.get()
            hora = entrada_hora.get()
            descripcion = entrada_descripcion.get()
            self.sistema_clinica.programar_cita(paciente, fecha, hora, descripcion)
            ventana_registro.destroy()

        tk.Button(ventana_registro, text="Programar", command=programar).pack()

    def registrar_medicamento(self):
        ventana_registro = tk.Toplevel(self.ventana)
        ventana_registro.title("Registrar medicamento")

        # Entradas para datos del medicamento
        tk.Label(ventana_registro, text="Nombre:").pack()
        entrada_nombre = tk.Entry(ventana_registro)
        entrada_nombre.pack()

        tk.Label(ventana_registro, text="Cantidad:").pack()
        entrada_cantidad = tk.Entry(ventana_registro)
        entrada_cantidad.pack()

        tk.Label(ventana_registro, text="Precio:").pack()
        entrada_precio = tk.Entry(ventana_registro)
        entrada_precio.pack()

        # Botón para registrar medicamento
        def registrar():
            nombre = entrada_nombre.get()
            cantidad = entrada_cantidad.get()
            precio = entrada_precio.get()
            self.sistema_clinica.registrar_medicamento(nombre, cantidad, precio)
            ventana_registro.destroy()

        tk.Button(ventana_registro, text="Registrar", command=registrar).pack()

    def ejecutar(self):
        self.ventana.mainloop()

# Crear sistema de clínica
sistema_clinica = SistemaClinica()

# Crear interfaz gráfica
interfaz_grafica = InterfazGrafica(sistema_clinica)

# Ejecutar interfaz gráfica
interfaz_grafica.ejecutar()