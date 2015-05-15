class tabla_de_sesgos :
	def __init__(self) :
		self.sesgo = None # 
		self.clase_de_sesgo = None # 
		pass
class marcador (reproductor, tabla_de_sesgos, registro_de_tiempos, medio) :
	def __init__(self) :
		pass
	def cargar_medio (self) :
		# returns 
		pass
	def marcar_tiempos (self) :
		# returns 
		pass
	def marcar_sesgo (self) :
		# returns 
		pass
	def indicar_idea_general (self) :
		# returns 
		pass
class reproductor :
	'''(NULL)'''
	def __init__(self) :
		pass
	def cargar_medio (self) :
		# returns 
		pass
class registro_de_tiempos :
	def __init__(self) :
		self.medio = None # 
		self.tiempo = None # 
		self.espacio = None # 
		pass
class medio :
	def __init__(self) :
		self.audio = None # 
		self.video = None # 
		self.texto = None # 
		self.imagen = None # 
		pass
