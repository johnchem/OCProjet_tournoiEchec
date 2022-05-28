from chess_tournament.models.player import Player


def test_joueur():
    nvxJoueur = [
        ("Tardiff", "Stephanie", "26/09/1967", "F"),
        ("Connie", "Lam", "10/06/1986", "F"),
        ("Cleveland", "Noon", "03/11/1938", "M"),
        ("Disalvo", "Aaron", "13/09/1967", "M"),
        ("Digiacomo", "David", "13/09/1944", "M"),
        ("Adela", "Scanlon", "10/01/1951", "F"),
        ("Galbraith", "Rosemary", "03/11/1970", "F"),
        ("Burroughs", "Eric", "03/09/1967", "M"),
    ]
    for nom, prenom, date_de_naissance, sexe in nvxJoueur:
        test = Player(nom, prenom, date_de_naissance, sexe)
        print(test)
    return None


if __name__ == "__main__":
    test_joueur()
