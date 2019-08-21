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


#INTERFAZ DE USO

jefe1 = jefeDeProyecto("bulbasaur","1","1996-2-27")
jefe2 = jefeDeProyecto("ivysaur","2","1996-2-27")
jefe3 = jefeDeProyecto("venusaur","3","1996-2-27")

class Menu:

	def __init__(self):
		self.opciones = {
						"1": self.ingresar_voluntario
						"2": self.crear_proyecto
						"3": self.gestionar_proyecto
						"4": self.visualizar
						"5": self.
						}

	def display_menu(self):
		print("""
			1: Ingresa un voluntario
			2: Crear un proyecto
			3: Gestionar proyecto
			4: Visualizar
			5: Eliminar
			6: Salir
			""")

	def run(self):
		running = True
		while running:
		self.display_menu()
		eleccion = input("Ingrese opcion:")
		accion = self.opciones.get(eleccion)
		if accion:
			accion()
		else:
			print("{0} no es una opcion valida".format(eleccion))
		if eleccion == '5':
			running = False

	def ingresar_voluntario(self):
		nombre = input("Ingresa tu nombre")
		edad = int(input("Ingresa tu edad"))

		date_entry = input('Ingresa la fecha en formato YYYY-MM-DD')
		year, month, day = map(int, date_entry.split('-'))
		fechaIngreso = dt.date(year, month, day)

		proximaAccion = input("Ingresa tu proxima accion") 				



a = input("Ingresa la accion a realizar")

if a == "1":
	vol = input("Que tipo de voluntario eres?") #Recibe un string que indica el 
	#tipo de voluntario
	if vol == "jefe":
		regJ = registro()
		jefe = jefeDeProyecto(regJ[0],regJ[1],regJ[2],regJ[3])
		lista_voluntarios[0].append(jefe)
	else if vol == "analista":
		regA = registro()
		esp = input("Cual es tu especializacion?")
		analista = Analista(regA[0],regA[1],regA[2],regA[3],esp)
		lista_voluntarios[1].append(analista)
	else if vol == "obrero":
		regO = registro()
		obrero = Analista(regO[0],regO[1],regO[2],regO[3])
		lista_voluntarios[2].append(obrero)