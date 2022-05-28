# import module
from datetime import datetime
from tinydb import TinyDB
import pathlib
import copy
import os

# import models
from chess_tournament.models.tournament import (TIME_CONTROLE_STANDARD,
                                                TournamentSwiss)
from chess_tournament.models.property import Property
from chess_tournament.models.date_property import DateProperty
from chess_tournament.models.multiple_choices_property import MultipleChoicesProperty
from chess_tournament.models.gender_property import GenderProperty
from chess_tournament.models.player import Player
from chess_tournament.models.round import Round
from chess_tournament.models.match import Match

import chess_tournament.controller.deserializer as deserializer
import chess_tournament.controller.controller as controller
import chess_tournament.views.base as base

# testing data
TOURN_NAME = "Championnat mondial 2022"
TOURN_LOCATION = "Budapest"
TOURN_DATE = "18/06/2022"
TOURN_DURATION = "1"
TOURN_NB_ROUND = 4
TOURN_TIME_CONTROL = "coup rapide"
TOURN_DESCRIPTION = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."

# Player : name, forname, birth_date, gender, rank
PLAYER_1 = ["Guyot", "Colette", "28/02/1998", "F", 1]
PLAYER_2 = ["Soler", "Alfred", "27/04/1976", "H", 2]
PLAYER_3 = ["Bureau", "Margot", "06/11/2000", "F", 3]
PLAYER_4 = ["Pommier", "Anatole", "19/07/1964", "M", 4]
PLAYER_5 = ["Quentin", "Charles", "14/11/2001", "M", 5]
PLAYER_6 = ["Hamel", "Luce", "21/10/1989", "F", 6]
PLAYER_7 = ["Leclercq", "Sylvestre", "29/12/1986", "M", 7]
PLAYER_8 = ["Normand", "Adeline", "17/03/1981", "F", 8]

PLAYERS_DATA = [PLAYER_1, PLAYER_2,
                PLAYER_3, PLAYER_4,
                PLAYER_5, PLAYER_6,
                PLAYER_7, PLAYER_8]

# match : [(player_1, score_1), (player_2, score_2)]
ROUND_1 = [[PLAYER_1, 1, PLAYER_5, 0],
           [PLAYER_2, 1, PLAYER_6, 0],
           [PLAYER_3, 0.5, PLAYER_7, 0.5],
           [PLAYER_4, 0, PLAYER_8, 1],
           ]

ROUND_2 = [[PLAYER_1, 1, PLAYER_2, 0],
           [PLAYER_8, 0, PLAYER_3, 1],
           [PLAYER_7, 0, PLAYER_4, 1],
           [PLAYER_5, 0.5, PLAYER_6, 0.5],
           ]

ROUND_3 = [[PLAYER_1, 0.5, PLAYER_3, 0.5],
           [PLAYER_2, 1, PLAYER_4, 0],
           [PLAYER_8, 0, PLAYER_5, 1],
           [PLAYER_6, 0, PLAYER_7, 1],
           ]

ROUND_4 = [[PLAYER_1, 1, PLAYER_7, 0],
           [PLAYER_2, 0, PLAYER_3, 1],
           [PLAYER_5, 0, PLAYER_4, 1],
           [PLAYER_8, 1, PLAYER_6, 0],
           ]

DB_ADDRESS = pathlib.Path(__file__).parent.absolute().joinpath("DB_unitest_fonctionnel.json")


def test_create_tournament():
    # Set up Tournament variable
    name = Property()
    location = Property()
    date = DateProperty()
    duration = Property()
    number_of_round = Property()
    time_control = MultipleChoicesProperty()
    time_control.list_value = TIME_CONTROLE_STANDARD
    description = Property()

    name.set_value(TOURN_NAME)
    location.set_value(TOURN_LOCATION)
    date.set_value(TOURN_DATE)
    duration.set_value(TOURN_DURATION)
    number_of_round.set_value(TOURN_NB_ROUND)
    time_control.set_value(str(TIME_CONTROLE_STANDARD.index(TOURN_TIME_CONTROL)+1))
    description.set_value(TOURN_DESCRIPTION)

    # creation of the tournament
    tourn = TournamentSwiss(name=name,
                            location=location,
                            date=date,
                            duration=duration,
                            number_of_round=number_of_round,
                            time_control=time_control,
                            description=description,
                            )

    # testing
    assert isinstance(tourn, TournamentSwiss)
    assert tourn.name == TOURN_NAME
    assert tourn.location == TOURN_LOCATION
    assert tourn.date == datetime.strptime(TOURN_DATE, "%d/%m/%Y")
    assert tourn.duration == TOURN_DURATION
    assert tourn.number_of_round == TOURN_NB_ROUND
    assert tourn.time_control == TOURN_TIME_CONTROL
    assert tourn.description == TOURN_DESCRIPTION

    return tourn


def test_create_player(list_data_player):
    # Set up player variable
    name = Property()
    forname = Property()
    birth_date = DateProperty()
    gender = GenderProperty()
    rank = Property()

    data_name, data_forname, data_birth_date, data_gender, data_rank = list_data_player
    name.set_value(data_name)
    forname.set_value(data_forname)
    birth_date.set_value(data_birth_date)
    gender.set_value(data_gender)
    rank.set_value(data_rank)

    player = Player(name=name,
                    forname=forname,
                    birth_date=birth_date,
                    gender=gender,
                    rank=rank,
                    )

    # testing
    assert isinstance(player, Player)
    assert player.name == data_name
    assert player.forname == data_forname
    assert player.birth_date == datetime.strptime(data_birth_date, "%d/%m/%Y")
    assert player.gender == data_gender
    assert player.rank == data_rank

    return player


def test_add_player_to_tournament(tournament, player):
    nb_player_before_add = len(tournament.players)
    tournament.add_player(player)

    # testing
    assert len(tournament.players) == nb_player_before_add + 1
    assert player.name in tournament.dict_score
    assert player.name in tournament.dict_opponent

    return tournament


def test_create_round(tournament, control_set):
    player_pairs = tournament.player_group_generation()
    pairs = copy.deepcopy(player_pairs)

    # testing pair creation
    assert player_pairs is not None
    for control, p in zip(control_set, list(pairs)):
        c_player_1, _, c_player_2, _ = control
        player_1, player_2 = p
        assert c_player_1[0] == player_1.name
        assert c_player_2[0] == player_2.name

    # definition du nom du round et creation
    current_round = tournament.current_round + 1
    next_round_name = f"Tour_{current_round}"
    next_round = Round(next_round_name)

    # creation des match et ajout au round
    for x, y in player_pairs:
        new_match = Match(x, y)
        next_round.add_match(new_match)
    tournament.rounds.append(next_round)

    return tournament


def test_end_round(tournament, control_set):
    score_init = copy.deepcopy(tournament.dict_score)
    tournament.end_round()

    for match, control in zip(tournament.rounds[-1].match, control_set):
        _, score_1, _, score_2 = control
        match.set_result(score_1, score_2)
    tournament.get_players_opponent()
    tournament.get_players_score()

    for player_1, score_p1, player_2, score_p2 in control_set:
        assert player_2[0] in tournament.dict_opponent[player_1[0]]
        assert tournament.dict_score[player_1[0]] - score_init[player_1[0]] == score_p1
        assert tournament.dict_score[player_2[0]] - score_init[player_2[0]] == score_p2

    return tournament


def test_save_tournament(tournament, data_base):
    # save tournamenent in the database
    tourn_serialized = tournament.serialize()
    _, tourn_id, player_id = controller.save_tournament_data(tourn_serialized, data_base)
    tourn_id = tourn_id[0]
    # send id to the object
    tournament.id = tourn_id
    print(tournament.id)
    for player, value in zip(tournament.players, player_id):
        player.id = value

    # reload the serialized object
    db = TinyDB(data_base)
    tournament_table = db.table("tournament")
    result = tournament_table.get(doc_id=tourn_id)

    reload_tournament = deserializer.deserialize_tournament(**result)
    assert tournament == reload_tournament


def test_reload_tournament(tournament, data_base):
    history_tournament = controller.load_tournament_data(data_base)

    def get_tournament(result, id):
        for tourn in result:
            if tourn.doc_id == id:
                return tourn
    chosen_tournament = get_tournament(history_tournament, tournament.id)

    # importation des données
    deserialized_tourn = deserializer.deserialize_tournament(**chosen_tournament)

    assert deserialized_tourn == tournament


def test_tournament_closure(tournament):
    views = base.Views()
    os.system("pause")
    views.grille_americaine(tournament)


if __name__ == "__main__":
    print("\n", "_____test_create_tournament______")
    tournament = test_create_tournament()

    list_player = []
    i = 0
    print("\n", "_____test_create_player______")
    for data in PLAYERS_DATA:
        i += 1
        list_player.append(test_create_player(data))
        print(f'joueur {i} créé')

    print("\n", "_____test_add_player_to_tournament______")
    i = 0
    for player in list_player:
        i += 1
        tournament = test_add_player_to_tournament(tournament, player)
        print(f'joueur {i} ajoutée')

    print("\n", "_____test_create_round_1_____")
    tournament = test_create_round(tournament, ROUND_1)
    print("\n", "_____test_end_round_1_____")
    tournament = test_end_round(tournament, ROUND_1)

    print("\n", "_____test_create_round_2_____")
    tournament = test_create_round(tournament, ROUND_2)
    print("\n", "_____test_end_round_2_____")
    tournament = test_end_round(tournament, ROUND_2)

    print("\n", "_____test_create_round_3_____")
    tournament = test_create_round(tournament, ROUND_3)
    print("\n", "_____test_end_round_3_____")
    tournament = test_end_round(tournament, ROUND_3)

    print("\n", "_____test_create_round_4_____")
    tournament = test_create_round(tournament, ROUND_4)
    print("\n", "_____test_end_round_4_____")
    tournament = test_end_round(tournament, ROUND_4)

    print("\n", "_____test_save_tournament______")
    test_save_tournament(tournament, DB_ADDRESS)

    print("\n", "_____test_reload_tournament______")
    test_reload_tournament(tournament, DB_ADDRESS)

    print("\n", "_____test_tournament_closure______")
    test_tournament_closure(tournament)

    print("\n", "_____end_of_testing______")
