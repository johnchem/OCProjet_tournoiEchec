import copy  # module to avoid modify the original testing data

# import data
import chess_tournament.unittest.test_data as test_data

# import function to test
from chess_tournament.controller.deserializer import (
    deserialize_tournament,
    deserialize_player,
    deserialize_round,
    deserialize_match,
)


def test_deserialize_player(players_serialized, player, text=""):
    print(text)
    players_serialized = copy.deepcopy(players_serialized)
    output = deserialize_player(**players_serialized)
    assert (
        output == player
    ), f"erreur lors de l'import d'un joueur \n {vars(output)} \n {vars(player)}"


def test_deserialize_match(match_serialized, match, text=""):
    print(text)
    match_serialized = copy.deepcopy(match_serialized)
    output = deserialize_match(**match_serialized)
    assert output == match, f"erreur lors de l'import d'un match \n {vars(output)}"


def test_deserialize_round(round_serialized, round, text=""):
    print(text)
    round_serialized = copy.deepcopy(round_serialized)
    output = deserialize_round(**round_serialized)
    assert output == round, f"erreur lors de l'import d'un round \n {vars(output)}"


def test_deserialize_tournament(tournament_serialised, tournament, text=""):
    print(text)
    tournament_serialised = copy.deepcopy(tournament_serialised)
    output = deserialize_tournament(**tournament_serialised)
    assert (
        output == tournament
    ), f"erreur lors de l'import d'un tournois \n {vars(tournament)} \n {vars(output)}"


if __name__ == "__main__":

    list_test_player = [
        (test_data.serialized_player_1, test_data.player_1),
        (test_data.serialized_player_2, test_data.player_2),
        (test_data.serialized_player_3, test_data.player_3),
        (test_data.serialized_player_4, test_data.player_4),
        (test_data.serialized_player_5, test_data.player_5),
        (test_data.serialized_player_6, test_data.player_6),
        (test_data.serialized_player_7, test_data.player_7),
        (test_data.serialized_player_8, test_data.player_8),
    ]

    list_test_match = [
        (test_data.serialized_match_1, test_data.match_1),
        (test_data.serialized_match_2, test_data.match_2),
        (test_data.serialized_match_3, test_data.match_3),
        (test_data.serialized_match_4, test_data.match_4),
        (test_data.serialized_match_5, test_data.match_5),
        (test_data.serialized_match_6, test_data.match_6),
    ]

    list_test_round = [(test_data.serialized_round_1, test_data.round_1),
                       (test_data.serialized_round_2, test_data.round_2)]

    list_test_tournament = [
        (test_data.serialised_tournament_1, test_data.tournament_1),
        (test_data.serialised_tournament_2, test_data.tournament_2),
        (test_data.serialised_tournament_3, test_data.tournament_3),
    ]

    i = 1
    print("_____test_deserialize_player______")
    for ser_player, player in list_test_player:
        test_deserialize_player(ser_player, player, f"player {i}")
        i += 1
    print("")

    i = 1
    print("_____test_deserialize_match______")
    for ser_match, match in list_test_match:
        test_deserialize_match(ser_match, match, f"match {i}")
        i += 1

    i = 1
    print("_____test_deserialize_round______")
    for ser_round, rnd in list_test_round:
        test_deserialize_round(ser_round, rnd, f"round {i}")
        i += 1

    i = 1
    print("_____test_deserialize_tournament______")
    for ser_tournament, tournament in list_test_tournament:
        test_deserialize_tournament(ser_tournament, tournament, f"tournament {i}")
        i += 1
