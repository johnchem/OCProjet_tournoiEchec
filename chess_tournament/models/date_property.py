from chess_tournament.models.property import Property
from datetime import datetime as dt


class DateProperty(Property):
	"""
	gere le tranfert et le controle des valeurs de date au modele	

	Attribut
	----------- 	
	
	Methodes
	-----------
	set_value(value, format = "%d/%m/%Y")
		validation de la valeur et enregistre si conforme	
	"""
	def set_value(self, value, format = "%d/%m/%Y"):
		try : 
			value = dt.strptime(value, format)
			if self._control_function:
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
			print(f"la date n'est pas correcte {value}")
			return False

	def __str__():
		return f"{self.value.strftime('%d/%m/%Y')}"
