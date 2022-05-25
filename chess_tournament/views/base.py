import os

# terminal commandes
CLEAN_SCREEN = "CLS"


class Views:
    """
    no variable
    _______________________
    .__init__() -> none
    .welcome_page() -> None
    .main_menu_page(menu_item_list, tournament_name=None,
                        player_nb=None, current_round_name=None) -> int
    .report_menu_page(menu_item_list) -> int
    .get_tournament_data(parameter_dict) -> None
    .tournament_created(tournois) -> None
    .new_player_page(parameter_dict) -> dict
    .load_tournament_page(tournament_list) -> int
    .load_player_page(player_list) -> int
    .update_player(player, item) -> Property.value
    .round_recap(ronde) -> None
    .display_match(match) -> None
    .report_all_players(player_list) -> None
    .report_all_tourn(tourn_list) -> None
    .report_player_in_tourn(tourn_name, player_list) -> None
    .report_round_in_tourn(tourn_name, round_list): -> None
    .report_match_in_tourn(tourn_name, match_list) -> None
    .grille_americaine(tournament) -> None
    .ask_match_result(match) -> (int, int)
    .ask_to_create_tournament() -> None
    .error_input_match_result() -> None
    .not_implemented() -> None
    .max_number_players_reach() -> None
    .database_not_found() -> None
    .no_data_in_db(item) -> None
    .issues_database(error = None) -> None
    .save_performed_page() -> None
    .save_performed_message() -> None
    .error_save_page(error = None) -> None
    .general_error_message(error) -> None
    .exit_message(self) -> None
    .clear_screen() -> None:
    """

    def __init__(self):
        pass

    def welcome_page(self):
        """landing page"""
        os.system(CLEAN_SCREEN)
        print("Bienvenue dans Chess Manager")
        os.system("pause")

    def main_menu_page(
        self,
        menu_item_list,
        tournament_name=None,
        player_nb=None,
        current_round_name=None,
    ):
        """show the main menu, if a tournament is loaded
        the menu display the name, the current round and the number of player"""
        i = 1
        os.system(CLEAN_SCREEN)
        if tournament_name:
            print(f"tournois actuel : {tournament_name}")
        if player_nb:
            print(f"nombre de joueurs en lice : {player_nb}")
        if current_round_name:
            print(f"round actuel : {current_round_name}")

        print("________MENU PRINCIPAL________")
        for menu_item in menu_item_list:
            print(f"{i} : {menu_item}")
            i += 1
        return user_choices("indiquer votre choix : ", range(1, i + 1))

    def report_menu_page(self, menu_item_list):
        """menu for the different available report"""
        i = 1
        os.system(CLEAN_SCREEN)
        print("________RAPPORTS________")
        for menu_item in menu_item_list:
            print(f"{i} : {menu_item}")
            i += 1
        return user_choices("indiquer votre choix : ", range(1, i + 1))

    def get_tournament_data(self, parameter_dict):
        """display a form to create a new tournament"""
        os.system(CLEAN_SCREEN)
        print("CREATION D UN NOUVEAU TOURNOI")
        print("Veuillez remplir les champs ci-dessous \n")
        for item in parameter_dict.values():
            # demande à l'utilisateur la valeur tant que
            # celle-ci n'est pas conforme
            while not item.set_value(input(item.message)):
                pass
        return parameter_dict

    def tournament_created(self, tournois):
        """Resume the tournament data"""
        os.system(CLEAN_SCREEN)
        print("Le tournois à bien été crée \n")
        print("Rappel : ")
        print(f"Nom : {tournois.name}")
        print(f"Lieu : {tournois.location}")
        print(
            f"A partir du {tournois.date.strftime('%d/%m/%Y')} pendant {tournois.duration} jours"
        )
        print(f"{tournois.number_of_round} tours avec la régle {tournois.time_control}")
        print("")
        os.system("pause")

    def new_player_page(self, parameter_dict):
        """display a form to create a new player"""
        os.system(CLEAN_SCREEN)
        print("_Creation d'un nouveau joueur_")
        for item in parameter_dict.values():
            # demande à l'utilisateur la valeur tant que
            # celle-ci n'est pas conforme
            while not item.set_value(input(item.message)):
                pass
        return parameter_dict

    def load_tournament_page(self, tournament_list):
        """print the list of the recorded tournaments"""
        os.system(CLEAN_SCREEN)
        print("Chargement d'un ancien tournois")
        i = 1
        for item in tournament_list:
            print(f"{i} : {item}")
            i += 1
        return user_choices("indiquer votre choix : ", range(1, i + 1))

    def load_player_page(self, player_list):
        """print the list of the recorded players"""
        os.system(CLEAN_SCREEN)
        print("Chargement d'un joueur enregistré")
        i = 1
        for item in player_list:
            print(f"{i} : {item}")
            i += 1
        return user_choices("indiquer votre choix : ", range(1, i + 1))

    def update_player(self, player, item):
        """page to update the selected player data"""
        print(
            "classement actuel de",
            f"{player.forname} {player.name}",
            f": {player.rank}",
        )

        # demande à l'utilisateur la valeur tant que
        # celle-ci n'est pas conforme
        while not item.set_value(input(item.message)):
            pass
        return item

    def round_recap(self, ronde):
        """show the resume of a round"""
        clear_screen()
        if ronde.is_done:
            print(
                f"{ronde.name}"
                f' le {ronde.begin_date_time.strftime("%d/%m/%Y")}'
                f' entre {ronde.begin_date_time.strftime("%X")}'
                f' et {ronde.end_date_time.strftime("%X")}'
            )
        else:
            print(
                f"{ronde.name}"
                f' le {ronde.begin_date_time.strftime("%d/%m/%Y")}'
                f' en cours depuis {ronde.begin_date_time.strftime("%X")}'
            )
        print("____________MATCH_____________")
        for match in ronde.match:
            self.display_match(match)
        os.system("pause")

    def display_match(self, match):
        """show the resume of a match"""
        match_not_done = (
            match.player_1["score"] is None or match.player_2["score"] is None
        )
        p1, p2 = match.player_1["player"], match.player_2["player"]
        p1_full_name = f"{p1.name} {p1.forname}"
        p2_full_name = f"{p2.name} {p2.forname}"

        if match_not_done:
            print(
                f'{p1_full_name:>25} ({match.player_1["color"]}) - ',
                f': - ({match.player_2["color"]}) {p2_full_name:<25}',
            )
        else:
            print(
                f'{p1_full_name:>20} ({match.player_1["color"]})',
                f' {match.player_1["score"]} ',
                f': {match.player_2["score"]} ',
                f'({match.player_2["color"]}) {p2_full_name:<25}',
            )

    def report_all_players(self, player_list):
        """report of all the players in the db"""
        clear_screen()
        template = "{:<25}|{:^4}|{:^17}|{:^4}"
        title_list = ["Joueur", "Sexe", "Date de naissance", "Rang"]
        title = template.format(*title_list)
        print(title)
        print("_" * 53)
        for player in player_list:
            print(template.format(*player))
        os.system("pause")

    def report_all_tourn(self, tourn_list):
        """report of all the players in the db"""
        clear_screen()
        template = "{:<25}|{:^10}|{:^10}|{:^5}|{:^17}|{:^12}|{:^7}"
        title_list = [
            "Nom",
            "Lieu",
            "Date",
            "Durée",
            "Contrôle du temps",
            "Nb de joueur",
            "Terminé",
        ]
        title = template.format(*title_list)
        print(title)
        print("_" * 90)
        for tourn in tourn_list:
            print(template.format(*tourn))
        os.system("pause")

    def report_player_in_tourn(self, tourn_name, player_list):
        """report the players sign in the tournament"""
        clear_screen()
        template = "{:<25}|{:^4}|{:^17}|{:^4}"
        print(f"Joueurs présents au tournois : {tourn_name}")
        title_list = ["Joueur", "Sexe", "Date de naissance", "Rang"]
        title = template.format(*title_list)
        print(title)
        print("_" * 53)
        for player in player_list:
            print(template.format(*player))
        os.system("pause")

    def report_round_in_tourn(self, tourn_name, round_list):
        """report of the round in the tournament"""
        clear_screen()
        template = "{:<10}|{:^12}|{:^12}|{:^12}|{:^4}"
        print(f"Rondes pour le tournois : {tourn_name}")
        title_list = ["Nom", "Date", "Heure début", "Heure fin", "Termine"]
        title = template.format(*title_list)
        print(title)
        print("_" * 57)
        for r in round_list:
            print(template.format(*r))
        os.system("pause")

    def report_match_in_tourn(self, tourn_name, match_list):
        """report of all the match in tournament"""
        clear_screen()
        template = "{:<25}|{:^4}|{:^7}|{:^5}|{:^5}|{:^7}|{:^4}|{:>25}"
        print(f"Match pour le tournois : {tourn_name}")
        title_list = [
            "Joueur 1",
            "rank",
            "Couleur",
            "Score",
            "Score",
            "Couleur",
            "rank",
            "Joueur 2",
        ]
        title = template.format(*title_list)
        print(title)
        print("_" * 89)
        for r in match_list:
            print(template.format(*r))
        os.system("pause")

    def grille_americaine(self, tournament):
        """show the grille americain at the end of a tournament"""
        list_players = [[x] for x in tournament.players]
        list_match = [y for x in tournament.rounds for y in x.match]

        for match in list_match:
            p1, p2 = match.player_1, match.player_2
            resultat_p1, resultat_p2 = resultat_match(p1, p2)
            for item in list_players:
                if item[0] == p1["player"]:
                    item.append(resultat_p1)
                if item[0] == p2["player"]:
                    item.append(resultat_p2)

        for item in list_players:
            score = tournament.dict_score[item[0].name]
            item.append(score)
        list_players.sort(key=lambda x: x[-1], reverse=True)

        clear_screen()
        template = "{:<25}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:5}"
        title_list = (
            ["joueur", "rank"]
            + [f"R{x}" for x in range(1, tournament.number_of_round + 1)]
            + ["score"]
        )
        title = template.format(*title_list)
        print(title)
        print("_" * 60)
        for item in list_players:
            print(
                template.format(
                    f"{item[0].name} {item[0].forname}", f"{item[0].rank}", *item[1:]
                )
            )

        os.system("pause")

    def ask_match_result(self, match):
        """ """
        p1, p2 = match.player_1["player"], match.player_2["player"]

        clear_screen()
        print(f"{p1.name} {p1.forname} vs {p2.name} {p2.forname}")
        score_p1 = float(input(f"{p1.name} : "))
        score_p2 = float(input(f"{p2.name} : "))
        return (score_p1, score_p2)

    def ask_to_create_tournament(self):
        print_message(
            "vous devez créer un nouveau tournois avant d'ajouter des joueurs"
        )

    def error_input_match_result(self):
        print_message(
            "le score introduit ne correspond pas au résultats valide",
            "gagnant : 1  perdant : 0 nul : 0.5 pour les 2 joueurs",
        )

    def not_implemented(self):
        print_message("cette fonction n'est pas encore implementée")

    def max_number_players_reach(self):
        print_message("vous avez atteint le nombre maximal de joueur dans cette partie")

    def database_not_found(self):
        print_message("aucune base de donnée trouvée")

    def no_data_in_db(self, item):
        print_message(f"pas de {item} disponible")

    def issues_database(self, error=None):
        if error is not None:
            print_message(
                "Problème lors de l'importation de la base de donnée\n",
                f"erreur rencontré : {error}",
            )
        else:
            print_message("Problème lors de l'importation de la base de donnée")

    def save_performed_page(self):
        print_message("Données sauvegardé \n")

    def save_performed_message(self):
        print("Données sauvegardé")

    def error_save_page(self, error=None):
        if error is not None:
            print_message(
                "Echec de la sauvegarde des données ", f"\nerreur rencontré : {error}"
            )
        else:
            print_message("Echec de la sauvegarde des données")

    def general_error_message(self, error):
        print_message("erreur :", f"{error}")

    def exit_message(self):
        os.system(CLEAN_SCREEN)
        print("Au revoir et bonne journée")

    def clear_screen(self):
        clear_screen()


def clear_screen():
    os.system(CLEAN_SCREEN)


def print_message(*text):
    os.system(CLEAN_SCREEN)
    print(*text)
    os.system("pause")


def resultat_match(player_1, player_2):
    score_p1, score_p2 = "", ""
    if player_1["score"] == 0:
        score_p1, score_p2 = "-", "+"
    elif player_1["score"] == 1:
        score_p1, score_p2 = "+", "-"
    else:
        score_p1, score_p2 = "=", "="

    score_p1 += f'{player_2["player"].rank}'
    score_p2 += f'{player_1["player"].rank}'

    if player_1["color"] == "black":
        score_p1 += "B"
        score_p2 += "W"
    else:
        score_p1 += "W"
        score_p2 += "B"

    return score_p1, score_p2


def user_choices(text, values):
    input_wrong = True
    while input_wrong:
        user_input = input(text)
        if user_input.isnumeric():
            user_input = int(user_input)
        if user_input in values:
            input_wrong = False
    return user_input


if __name__ == "__main__":
    pass
