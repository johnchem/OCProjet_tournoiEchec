from datetime import datetime as dt

class Property:
	""" gere le tranfert et le controle des valeurs au modele
	
	.message : message pour l'usager
	.error_message : message en cas d'erreur sur la valeur introduite
	.value : velur de la propriété 
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


class MultipleChoicesProperty(Property)
	def __init__(self, text, list_value):
		super().__init__(text):
		self.list_value = list_value
		self._range = range(1, len(list_value)+1)

	def set_value(self, value):
		input_wrong = True
		for 
		while input_wrong:
			if value.isnumeric() : user_input = int(user_input)
			if user_input in :
				input_conform = True
		return user_input


if __name__ == "__main__":
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
