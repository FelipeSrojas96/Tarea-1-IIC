import datetime as dt
#CLASE PROYECTOS Y SUS ESPECIALIZACIONES DE CONCIENTIZACION Y EJECUCION

class Proyectos:

	def __init__(self, nombre, descripcion = None, fechaInicio = None, estado = "Planificacion", jefeProyecto = None logs = None):
		self.nombre = nombre
		self.descripcion = descripcion
		self.fechaInicio = fechaInicio
		self.estado = estado
		self.jefeProyecto = jefeProyecto
		self.logs = logs

	def edicion(self, parametro):
		if parametro == "nombre":
			self.nombre = input("Ingresa el nuevo nombre")
		else if parametro = "descripcion"	
			self.nombre = input("Ingresa la descripcion")
		else if parametro = "descripcion"	
		

class Concientizacion(Proyectos):

	def __init__(self, nombre, descripcion = None, fechaInicio = None, estado = "Planificacion", jefeProyecto = None, analistas = None , obreros = None, logs = None, tema, impacto):
		super().__init__(nombre, descripcion, fechaInicio, estado, jefeProyecto, analistas, obreros, logs)
		
		self.tema = tema
		self.impacto = impacto

class Ejecucion(Proyectos):

	def __init__(self, nombre, descripcion = None, fechaInicio = None, estado = "Planificacion", jefeProyecto = None, analistas = None , obreros = None, logs = None, ciudad, costo):
		super().__init__(nombre, descripcion, fechaInicio, estado, jefeProyecto, analistas, obreros, logs)

		self.ciudad = ciudad
		self.costo = costo

#CLASES PARA LOS VOLUNTARIOS Y SUS RESPECTIVAS HERENCIAS DE LA CLASE SUPER Voluntarios

class Voluntarios:
	
	def __init__(self, nombre, edad, fechaIngreso, proximaAccion = None):
		self.nombre = nombre
		self.edad = edad
		self.fechaIngreso = fechaIngreso
		self.proximaAccion = proximaAccion	

	def accion(self):
		self.proximaAccion = input("Proxima accion a realizar")

class jefeDeProyecto(Voluntarios):

	def __init__(self, nombre, edad, fechaIngreso, proximaAccion = None):
		super().__init__(nombre, edad, fechaIngreso, proximaAccion)

		self.proyectos_acargo = []

class Analista(Voluntarios):

	def __init__(self, nombre, edad, fechaIngreso, proximaAccion, especializacion):
		super().__init__(nombre, edad, fechaIngreso, proximaAccion)

		self.especializacion = especializacion

class Obrero(Voluntarios):

	def __init__(self, nombre, edad, fechaIngreso, proximaAccion):
		super().__init__(nombre, edad, fechaIngreso, proximaAccion)				

#CLASES PARA LAS INSTITUCIONES

class Instituciones:

	def __init__(self, apoyo, nombre):
		self.apoyo = apoyo
		self.nombre = nombre

class InstitucionPublica(Instituciones):

	def __init__(self, apoyo, nombre):
		super().__init__(apoyo, nombre)

class InstitucionPrivada(Instituciones):

	def __init__(self, apoyo, nombre):
		super().__init__(apoyo, nombre)		

class InstitucionSocial(Instituciones):

	def __init__(self, apoyo, nombre):
		super().__init__(apoyo, nombre)

print("Bienvenido a la interfaz. Realiza una accion")
print("1: Ingresa un voluntario")
print("2: Crear un proyecto")
print("3: Gestionar proyecto")
print("4: Visualizar")
print("5: Eliminar")
print("6: Salir")

#Funcion para manejar el registro. fechaIngreso corresponde a una tupla de tipo (año,mes,dia)
def registro():
	nombre = input("Ingresa tu nombre")
	edad = int(input("Ingresa tu edad"))

	date_entry = input('Ingresa la fecha en formato YYYY-MM-DD')
	year, month, day = map(int, date_entry.split('-'))
	fechaIngreso = datetime.date(year, month, day)
	proximaAccion = input("Ingresa tu proxima accion")

	return [nombre, edad , fechaIngreso, proximaAccion]

lista_voluntarios = [[],[],[]]

a = input("Ingresa la accion a realizar")

if a == 1:
	vol = input("Que tipo de voluntario eres?") #Recibe un string que indica el 
	#tipo de voluntario
	if vol = "jefe":
		regJ = registro()
		jefe = jefeDeProyecto(regJ[0],regJ[1],regJ[2],regJ[3])
		lista_voluntarios[0].append(jefe)
	else if vol = "analista":
		regA = registro()
		esp = input("Cual es tu especializacion?")
		analista = Analista(regA[0],regA[1],regA[2],regA[3],esp)
		lista_voluntarios[1].append(analista)
	else if vol = "obrero":
		