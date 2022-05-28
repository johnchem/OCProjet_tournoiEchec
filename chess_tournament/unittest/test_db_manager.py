# importation des modules
import pathlib
import copy
from tinydb import TinyDB

# importation des modeles
from chess_tournament.models.player import Player
from chess_tournament.models.date_property import DateProperty

# importation du controlleur
from chess_tournament.controller.db_manager import (
    save_player_data,
    save_tournament_data,
    load_tournament_data,
)
from chess_tournament.controller.deserializer import (
    deserialize_tournament,
    deserialize_player,
)

# import data for testing
import chess_tournament.unittest.test_data as test_data


def test_save_tournament(tournament, db_file):
    serialized_tournament = tournament.serialize()
    try:
        save_tournament_data(serialized_tournament, db_file)
        print(serialized_tournament)
        return True
    except BaseException as err:
        print(err)
        exit()


def test_save_player(player, db_file):
    player_serialized = player.serialize()
    save_player_data(player_serialized, db_file)
    print("sauvegarde reussi")


def test_update_player(player, db_file, parameter_modifier, text=""):
    """
    player : Player
    db_file : Path
    parameter_modifier : list[tupple]
    text = str
    """
    print(text)
    # import testing data
    modified_player = copy.deepcopy(player)
    original_player = copy.deepcopy(player)

    # setting the parameter
    print(id(modified_player))
    result = save_player_data(modified_player.serialize(), db_file)
    modified_player.id = result[1]

    print("modification")
    print(vars(modified_player))
    # moditication des valeurs
    for key, new_value in parameter_modifier:
        setattr(modified_player, key, new_value)
    # sauvegarde dans la db and recupération de l'ID
    save_player_data(modified_player.serialize(), db_file)

    print("récupération du joueur via son id")
    # reimportation du joueur depuis la db
    db = TinyDB(db_file)
    players_table = db.table("players")
    print(f"id = {modified_player.id}")
    imported_player = players_table.get(doc_id=int(modified_player.id))
    print(imported_player)
    if isinstance(imported_player, Player):
        imported_player = deserialize_player(**imported_player)
    else:
        print("erreur durant l'importation du joueur")

    # contrôle
    assert imported_player == modified_player, print(
        f"{imported_player} {modified_player}"
    )
    for key, new_value in parameter_modifier:
        assert getattr(imported_player, key) != getattr(original_player, key)


def test_update_tournament(tournament, db_file, parameter_modifier, text=""):
    """
    player : Player
    db_file : Path
    parameter_modifier : list[tupple]
    text = str
    """
    print(text)
    # import testing data
    modified_tournament = copy.deepcopy(tournament)
    original_tournament = copy.deepcopy(tournament)

    # setting the parameter
    print("1er save du joueur")
    print(id(modified_tournament))
    save_player_data(modified_tournament.serialize(), db_file)

    print("modification")
    for key, new_value in parameter_modifier:
        setattr(modified_tournament, key, new_value)
    print("2nd sauvegarde")
    _, modified_tournament.id = save_tournament_data(
        modified_tournament.serialize(), db_file
    )

    print("récupération du joueur via son id")
    db = TinyDB(db_file)
    tournament_table = db.table("tournament")
    print(f"id = {modified_tournament.id}")
    imported_tournament = tournament_table.get(doc_id=modified_tournament.id)
    imported_tournament = deserialize_tournament(**imported_tournament)

    # contrôle
    assert imported_tournament == modified_tournament, print(
        f"{imported_tournament} {modified_tournament}"
    )
    for key, new_value in parameter_modifier:
        assert getattr(imported_tournament, key) != getattr(original_tournament, key)


def test_read_tournament_data(db_file):
    list_tournament = load_tournament_data(db_file)
    print(list_tournament)


if __name__ == "__main__":
    DB_ADDRESS = (
        pathlib.Path(__file__).parent.absolute().joinpath("DB_unitest.json")
    )  # absolule path
    # test_save_tournament(create_dummy_tournament(), DB_ADDRESS)
    # test_read_tournament_data(DB_ADDRESS)
    print("\n _____test_save_tournament______")
    test_save_tournament(test_data.tournament_2, DB_ADDRESS)

    print("\n _____test_update_player______")
    test_update_player(
        test_data.player_1,
        DB_ADDRESS,
        [("name", "roger"), ("forname", "paul"), ("rank", "12")],
        "test update",
    )

    print("\n _____test_update_tournament____")
    date = DateProperty("24/03/2022")
    text = "orem ipsum dolor sit amet, consectetur adipiscing elit. Nullam blandit ultrices scelerisque."
    test_update_tournament(
        test_data.tournament_1, [("name", "tutu"), ("date", date), ("description", text)]
    )
