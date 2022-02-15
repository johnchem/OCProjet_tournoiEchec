from models.property import Property
from datetime import datetime as dt


class DateProperty(Property):
	"""
	gere le tranfert et le controle des valeurs de date au modele	

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
	set_value(value, format = "%d/%m/%Y")
		validation de la valeur et enregistre si conforme
	set_defaut_value(value): Pas implementé
		mise en place d'une valeur par defaut
	
	"""
	def set_value(self, value, format = "%d/%m/%Y"):
		try : 
			value = dt.strptime(value, format)
			if hasattr(self, "_control_function"):
				if self._control_function(value):
					self.value = value
					return True
				else:
					print(self.error_message)
					return False
			else:
				self.value = value
				return True
		except ValueError:
			print("la date n'est pas correcte")
			return False

	def __str__():
		return f"{self.value.strftime('%d/%m/%Y')}"
