from tinydb import TinyDB, Query


def save_player_data(player, db_file):
    """
    player : dictionnary
    db_file : path
    """
    try:
        db = TinyDB(db_file)
        players_table = db.table("players")
        # players_table.truncate()	# clear the table first
        if player["id"] == "":
            filter = Query()
            id_number = players_table.upsert(player, filter.name == player["name"])
            return True, id_number
        else:
            players_table.update(player, doc_ids=[int(player["id"])])
        return True, player["id"]
    except BaseException as err:
        print(f"error save : {err}")
        return False, err


def load_player_data(db_file):
    try:
        db = TinyDB(db_file)
        players_table = db.table("players")
        return players_table.all()
    except BaseException as err:
        print(err)
        return err


def save_tournament_data(tournament, db_file):
    try:
        db = TinyDB(db_file)
        tournament_table = db.table("tournament")

        # sauvegarde du tournois
        if tournament["id"] == "":
            filter = Query()
            id_number = tournament_table.upsert(tournament, filter.name == tournament["name"])
            tournament["id"] = id_number
        else:
            id_number = tournament["id"]
            tournament_table.update(tournament, doc_ids=[int(id_number)])

        # sauvegarde des joueurs present dans la partie
        list_id_player = []
        if len(tournament["players"]) > 0:
            for player in tournament["players"]:
                a, player_id = save_player_data(player, db_file)
                list_id_player.append(player_id)
        else:
            list_id_player = None

        return True, id_number, list_id_player

    except BaseException as err:
        print(err)
        return False, err, None


def load_tournament_data(db_file):
    try:
        db = TinyDB(db_file)
        tournament_table = db.table("tournament")
        result = tournament_table.all()
        return result
    except BaseException as err:
        print(err)
        return err


if __name__ == "__main__":
    pass
