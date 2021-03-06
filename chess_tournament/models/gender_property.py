from chess_tournament.models.property import Property


class GenderProperty(Property):
    """gere le tranfert et le controle des valeurs au modele
    propriété pour le genre du joueur
    Force la valeur à être en majuscule

    Attribut
    -----------

    Methodes
    -----------
    set_value(value)
            validation de la valeur et enregistre si conforme
    """

    def set_value(self, value):
        """controle la conformite de la valeur,
        renvoie True et enregistre la valeur si conforme
        sinon renvoie False
        """
        # test si la valeur a une fonction de controle
        value = value.upper()
        if self._control_function:
            # test la conformité de la valeur non vide
            if self._control_function(value) and value != "":
                self.value = value
                return True
            # test si une valeur par defaut existe et que la chaine est vide
            elif not self._defaut_value and value == "":
                self.value = self._defaut_value
                print(f"{self.value} appliqué par défaut")
                return True
            # erreur si valeur non conforme ou sans valeur par defaut
            else:
                print(self.error_message)
                return False
        # test si une valeur par defaut existe
        elif not self._defaut_value and value == "":
            self.value = self._defaut_value
            print(f"{self.value} appliqué par défaut")
            return True
        else:
            self.value = value
            return True
