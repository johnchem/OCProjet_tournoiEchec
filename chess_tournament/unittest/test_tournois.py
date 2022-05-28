import copy
from datetime import datetime

from chess_tournament.models.tournament import TournamentSwiss, TIME_CONTROLE_STANDARD
from chess_tournament.models.round import Round
from chess_tournament.models.property import Property
from chess_tournament.models.date_property import DateProperty
from chess_tournament.models.multiple_choices_property import MultipleChoicesProperty

import chess_tournament.unittest.test_data as test_data


def test_create_tournament():
    name = Property()
    location = Property()
    date = DateProperty()
    duration = Property()
    number_of_round = Property()
    time_control = MultipleChoicesProperty()
    time_control.list_value = TIME_CONTROLE_STANDARD
    description = Property()

    name.set_value("test1")
    location.set_value("montpelier")
    date.set_value("15/12/1988")
    duration.set_value(1)
    number_of_round.set_value(5)
    time_control.set_value("2")
    description.set_value("truc machin")

    tournament = TournamentSwiss(
        name=name,
        location=location,
        date=date,
        duration=duration,
        number_of_round=number_of_round,
        time_control=time_control,
        description=description,
    )

    assert isinstance(tournament, TournamentSwiss)
    assert tournament.name == "test1"
    assert tournament.location == "montpelier"
    assert tournament.date == datetime.strptime("15/12/1988", "%d/%m/%Y")
    assert tournament.duration == 1
    assert tournament.number_of_round == 5
    assert tournament.time_control == TIME_CONTROLE_STANDARD[1]
    assert tournament.description == "truc machin"


def test_add_player():
    # get testing data
    tournament = copy.deepcopy(test_data.tournament_1)
    player = copy.deepcopy(test_data.player_1)

    # initialise and control the initial setup
    tournament.players = []
    assert len(tournament.players) == 0

    # testing
    tournament.add_player(player)
    assert len(tournament.players) == 1
    assert tournament.players[0] == player


def test_if_tournament_is_full():
    # get testing data
    tournament = copy.deepcopy(test_data.tournament_1)
    player = copy.deepcopy(test_data.player_1)

    # initialise and control the initial setup
    assert len(tournament.players) == 8

    # testing
    tournament.add_player(player)
    assert len(tournament.players) == 9
    assert tournament.players[-1] == player


def test_start_new_round():
    # get testing data
    tournament = copy.deepcopy(test_data.tournament_1)

    # initialize data
    tournament.current_round = 1
    tournament.rounds = []
    name_round = f"round{tournament.current_round}"
    round = Round(name_round)
    tournament.add_round(round)

    # testing
    tournament.start_new_tournament(round)
    assert name_round == "round1"
    assert tournament[-1].name == name_round
    assert (datetime.now - tournament.begin_date_time).seconds < 10
    assert tournament.end_date_time is None
    assert len(tournament.match) == 0
    assert tournament.is_done is False


def test_generation_pairs_players_round_1():
    # get testing data
    tournament = copy.deepcopy(test_data.tournament_3)

    # initialize data
    tournament.current_round = 1
    tournament.rounds = []

    # testing
    player_list = tournament.player_group_generation()
    for x, y in player_list:
        print(f"{x} vs {y}")


def test_get_players_opponent():
    # get testing data
    tournament = copy.deepcopy(test_data.tournament_1)

    # testing
    tournament.get_players_opponent()
    output = tournament.dict_opponent
    print(output)


def test_end_a_round():
    # get testing data
    tournament = copy.deepcopy(test_data.tournament_1)

    # initialize data
    tournament.current_round = 1
    tournament.rounds = []
    round = Round  # (name_round)
    tournament.start_new_tournament(round)

    # testing
    tournament.end_round()
    assert (datetime.now - tournament.end_date_time).seconds < 10
    assert tournament.is_done is True


def test_set_result_round():
    # get testing data
    tournament = copy.deepcopy(test_data.tournament_1)

    # initialize data
    tournament.current_round = 1
    tournament.rounds = []
    name_round = f"round{tournament.current_round}"
    round = Round(name_round)
    tournament.start_new_tournament(round)
    tournament.end_round()

    # testing
    assert (datetime.now - tournament.end_date_time).seconds < 10
    assert tournament.is_done is True


def test_add_round():
    pass


def test_create_round(tournament, round_nb):
    tournament.player_group_generation()
    # assert is tournament.round, "truc"
    for match in tournament.round[round_nb]:
        print(match)


def test_match():
    pass


if __name__ == "__main__":
    pass
