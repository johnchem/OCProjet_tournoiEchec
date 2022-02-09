from datetime import datetime as dt

class Property:
	""" gere le tranfert et le controle des valeurs au modele
	
	.message : message pour l'usager
	.error_message : message en cas d'erreur sur la valeur introduite
	.value : valeur de la propriété 
	._control_function : fonction de controle de la valeur
	
	# en implementation
	._type : type de la valeur désiré (outils convertion)
	._format : formatage de la date
	"""
	def __init__(self, text, **kargs):
		""" initialisation avec le message pour l'usager
		"""
		self.message = text

		# fonction a implementer
		#self._type = kwargs.get("type")
		#self._format = kargs.get("format")

	def set_control(self, function, errorText):
		""" stock les information necessaire pour controler
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
		if hasattr(self, "_control_function"):
			if self._control_function(value):
				self.value = value
				return True
			else: 
				return False
		else:
			self.value = value

	def set_defaut_value(self, value):
		self._defaut_value = value


class DateProperty(Property):
	"""
	class pour la gestion des parametres de date
	"""
	def set_value(self, value, format = "%d/%m/%Y"):
		try : 
			value = dt.strptime(value, format)
			if hasattr(self, "_control_function"):
				if self._control_function(value):
					self.value = value
					return True
				else: 
					return False
			else:
				self.value = value
				return True
		except ValueError:
			print("la date n'est pas correcte")
			return False


class MultipleChoicesProperty(Property):
	def __init__(self, prelim_text, list_value, text):
		super().__init__(text)
		self.list_value = list_value
		self.message = self._format_message(prelim_text, 
											list_value, 
											text)

	def _format_message(self, header, list_value, message):
		i = 1
		text_temp = "\n" + header + "\n"
		for item in list_value:
			text_temp += f"{i} : {item} \n"
			i += 1
		text_temp += message
		return text_temp

	def set_value(self, value):
		i = 1
		""" vérifie que la valeur est un nombre avant de le convertir en int"""
		if value.isnumeric():
			value = int(value)
		else:
			print(f"la valeur doit être un nombre")
			return False
		""" vérifie que la valeur est bien dans la liste de choix"""  
		if value in range(1, len(self.list_value)+1): 
			value = int(value) 
			""" """
			self.value = self.list_value[value-1]
			return True
		else : 
			print(f"la valeur doit être comprise entre 1 et {len(self.list_value)}")
			return False


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