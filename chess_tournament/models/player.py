import copy


class Player:
    """gere le tranfert et le controle des valeurs au modele
    propriété pour le genre du joueur
    Force la valeur à être en majuscule

    Attribut
    -----------
    name : str
            nom du joueur
    forname : str
            prénom du joueur
    birth_date : datetime
            date de naissance du joueur
    gender : str
            sexe du joueur
    rank : int
            classement du joueur
    id : int
            identifiant du joueur sur la base de donnée

    Methodes
    -----------
    .__init__(name, forname, birth_date, gender, rank) -> Player
    .add_opponent(player)
    .is_opponent_already_faced(player):
    .serialize():
    .__repr__():
    .__eq__(other):
    .__enter__():
    .__exit__(*err):
    """

    def __init__(self, name, forname, birth_date, gender, rank):
        self.name = name.value
        self.forname = forname.value
        self.birth_date = birth_date.value
        self.gender = gender.value
        self.rank = int(rank.value)
        self.id = ""

    def add_opponent(self, player):
        self.opponent.append(player)

    def is_opponent_already_faced(self, player):
        return player in self.opponent

    def serialize(self):
        serialized_player = copy.deepcopy(vars(self))
        serialized_player["birth_date"] = serialized_player["birth_date"].strftime(
            "%d/%m/%Y"
        )
        return serialized_player

    def __repr__(self):
        return (
            f"{self.forname} {self.name} ({self.gender})"
            f' née le {self.birth_date.strftime("%d/%m/%Y")}'
            f" : {self.rank}"
        )

    def __eq__(self, other):
        if not isinstance(other, Player):
            # don't attempt to compare against unrelated types
            return NotImplemented
        list_compare = [
            self.name != other.name,
            self.forname != other.forname,
            self.birth_date != other.birth_date,
        ]
        # return false if any difference exist
        return not any(list_compare)

    def __enter__(self):
        return self

    def __exit__(self, *err):
        self.close()


if __name__ == "__main__":
    pass
