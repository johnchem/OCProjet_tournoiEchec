

# from models.property import Property
from tournoisEchecs.models.property import Property

def test_num(message, errorMessage, controlfunction):
	prop = Property()
	prop.setMessage(message, errorMessage)
	assert prop._message == message
	prop.setControl(controlfunction)
	prop.setvalue()

if __name__ == "__main__":
	test_num("test de l'introduction de chiffre : ",
			"Un nombre est requis pour cette valeur",
			lambda x: x.isnumeric())