from models.property import Property

class MultipleChoicesProperty(Property):
	"""
	classe pour la gestion des propriétées à choix multiple
	._format_message : fonction pour l'affichage de la liste dz choix

	gere le tranfert et le controle des valeurs au modele

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
		"""vérifie que la valeur est un nombre avant de le convertir en int"""
		if value.isnumeric():
			value = int(value)
		else:
			print(f"la valeur doit être un nombre")
			return False
		"""vérifie que la valeur est bien dans la liste de choix"""  
		if value in range(1, len(self.list_value)+1): 
			value = int(value) 
			"""convertie le nombre choisie en choix de la liste"""
			self.value = self.list_value[value-1]
			return True
		else : 
			print(f"la valeur doit être comprise entre 1 et {len(self.list_value)}")
			return False