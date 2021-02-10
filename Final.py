class Planta(object):
	def __init__(self, nombre = "",especie = "",temporada = ""):
		self._nombre = nombre
		self._especie = especie
		self._temporada = temporada

	def getnombre(self):
		return(self._nombre)

	def getespecie(self):
		return(self._especie)

	def gettemporada(self):
		return(self._temporada)

	def Settemporada(self,temporada):
		self._temporada = temporada

class Jardin(Planta):
	def __init__(self, p):
		self.p = p
	'''	
	def Jardin(self, j):
		emplazamiento = j.emplazamiento
		numplantas = j.numplantas
		for i in range(0,100):
			if j.p[i] != None:
				p[i] = Planta(j.p[i].getnombre(),j.p[i].getespecie(),j.p[i].gettemporada())
			else:
				p[i] = None
	'''

	def Plantar(self, n = "", esp = "", tiempo = ""):
		numplantas = 0
		if numplantas >= 100:
			print("No caben más plantas en el jardín")
		else:
			lp = []
			NuevaPlanta = Planta(n,esp)
			lp.append(NuevaPlanta)
			a = input("Ingrese temporada: ")
			Planta.Settemporada(a)
			#lp.append(a)
			'''
			for i in 100:
				if p[i] == None:
					p[i] = lp
					break
			numplantas += 1
			'''
	'''		
	def Arrancar(nombre= "", esp = ""):
		numplantas = 10
		p = []
		if numplantas == 0:
			print("No quedan plantas en el jardín")
		else:
			for i in range100:
				if nombre == p[i].getnombre() and esp == p[i].getespecie():
					p[i].remove()
					p[i] = None
					numplantas -= 1
					break
	'''
#Inicio pedorro >:C
ob1= Planta("Rosa","flor","verano")
#Prueba = Jardin(ob1)
Prueba = Jardin(1)
Prueba.Plantar(ob1)