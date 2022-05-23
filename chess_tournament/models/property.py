
class Property:
	""" gere le tranfert et le controle des valeurs au modele

	Attribut
	----------- 	
	message : str 
		message pour l'usager
	error_message : str
		message en cas d'erreur sur la valeur introduite
	value : 
		valeur de la propriété 
	_control_function : function
		fonction de controle de la valeur
	_defaut_value : 
		valeur par defaut de la propriété

	Methodes
	-----------
	set_control(function, errorText)
		mise en place de la fonction de control et du message d'erreur
	set_value(value)
		validation de la valeur et enregistre si conforme
	set_defaut_value(value):
		mise en place d'une valeur par defaut
	"""
	def __init__(self):
		""" initialisation """ 
		self.message = None
		self.value = None
		self._control_function = None
		self.error_message = None
		self._defaut_value = None

	def set_message(self, text):
		""" le message pour l'usager"""
		self.message = text

	def set_control(self, function, errorText):
		"""stock les information necessaire pour controler
		la valeur d'entree
		"""
		self._control_function = function
		self.error_message = errorText

	def set_value(self, value):
		"""
		controle la conformite de la valeur,
		renvoie True et enregistre la valeur si conforme
		sinon renvoie False
		"""
		#test si la valeur a une fonction de controle
		if self._control_function:
			# test la conformité de la valeur non vide
			if self._control_function(value) and value != "":
				self.value = value
				return True
			# test si une valeur par defaut existe et que la chaine est vide
			elif self._defaut_value != None and value == "":
				self.value = self._defaut_value
				print(f"{self.value} appliqué par défaut")
				return True
			# erreur si valeur non conforme ou sans valeur par defaut
			else: 
				print(self.error_message)
				return False
		# test si une valeur par defaut existe
		elif self._defaut_value != None and value == "":
			self.value = self._defaut_value
			print(f"{self.value} appliqué par défaut")
			return True
		else:
			self.value = value
			return True

	def set_defaut_value(self, value):
		self._defaut_value = value

if __name__ == "__main__":
	"""
	message = "test de l'introduction d'une date : "
	error_message = "pas de tournois dans le passé"
	DATE_LIMITE = dt.strptime("01/01/2000", "%d/%m/%Y")
	control_function = lambda x: x>DATE_LIMITE

	prop = Property(message)
	prop.set_control(control_function, error_message)
	while not prop.set_value(input(prop.message)):
		print(prop.error_message)

	print(prop.value)
	prop2 = Property("je m'en fou de la valeur : ")
	while not prop2.set_value(input(prop2.message)):
		pass
	"""
	prelim_text = "Quel gestion du temps voullez vous appliquer ? :"
	list_choix = ["Bullet","Blitz","Coup rapide"]
	text = "choix : "
	prop = MultipleChoicesProperty(prelim_text, list_choix, text)
	while not prop.set_value(input(prop.message)):
		pass
	print(prop.value)