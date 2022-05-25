# importation des modules
import os
import pathlib
from datetime import datetime

# importation des modeles
from chess_tournament.models.player import Player
from chess_tournament.models.match import Match
from chess_tournament.models.round import Round
from chess_tournament.models.tournament import TournamentSwiss, TIME_CONTROLE_STANDARD
from chess_tournament.models.property import Property
from chess_tournament.models.date_property import DateProperty
from chess_tournament.models.multiple_choices_property import MultipleChoicesProperty
from chess_tournament.models.gender_property import GenderProperty

"""
match_1 : player_1 vs player_2
match_2 : player_3 vs player_4
match_3 : player_5 vs player_6
match_4 : player_7 vs player_8
match_5 : player_2 vs player_7
match_6 : player_4 vs player_2
match_7 : player_4 vs player_2

"""
# ________Set up player variable________
name = Property()
forname = Property()
birth_date = DateProperty()
gender = Property()
rank = Property()

# _________PLAYER 1___________
serialized_player_1 = {
    "name": "paul",
    "forname": "michel",
    "birth_date": "01/01/2001",
    "gender": "H",
    "rank": 0,
}
name.set_value("paul")
forname.set_value("michel")
birth_date.set_value("01/01/2001")
gender.set_value("H")
rank.set_value(0)

player_1 = Player(
    name=name, forname=forname, birth_date=birth_date, gender=gender, rank=rank
)

# _________PLAYER 2___________
serialized_player_2 = {
    "name": "george",
    "forname": "louis",
    "birth_date": "10/05/1995",
    "gender": "H",
    "rank": 10,
}
name.set_value("george")
forname.set_value("louis")
birth_date.set_value("10/05/1995")
gender.set_value("H")
rank.set_value(10)

player_2 = Player(
    name=name, forname=forname, birth_date=birth_date, gender=gender, rank=rank
)

# _________PLAYER 3___________
serialized_player_3 = {
    "name": "paulette",
    "forname": "vuiton",
    "birth_date": "15/11/1955",
    "gender": "F",
    "rank": 100,
}
name.set_value("paulette")
forname.set_value("vuiton")
birth_date.set_value("15/11/1955")
gender.set_value("F")
rank.set_value(100)


player_3 = Player(
    name=name, forname=forname, birth_date=birth_date, gender=gender, rank=rank
)

# _________PLAYER 4___________
serialized_player_4 = {
    "name": "despins",
    "forname": "Amedee",
    "birth_date": "11/12/1977",
    "gender": "F",
    "rank": 12,
}
name.set_value("despins")
forname.set_value("Amedee")
birth_date.set_value("11/12/1977")
gender.set_value("F")
rank.set_value(12)

player_4 = Player(
    name=name, forname=forname, birth_date=birth_date, gender=gender, rank=rank
)

# _________PLAYER 5___________
serialized_player_5 = {
    "name": "baupré",
    "forname": "dominic",
    "birth_date": "28/08/1988",
    "gender": "H",
    "rank": 26,
}
name.set_value("baupré")
forname.set_value("dominic")
birth_date.set_value("28/08/1988")
gender.set_value("H")
rank.set_value(26)

player_5 = Player(
    name=name, forname=forname, birth_date=birth_date, gender=gender, rank=rank
)

# _________PLAYER 6___________
serialized_player_6 = {
    "name": "deserres",
    "forname": "arthur",
    "birth_date": "12/08/1977",
    "gender": "H",
    "rank": 56,
}
name.set_value("deserres")
forname.set_value("arthur")
birth_date.set_value("12/08/1977")
gender.set_value("H")
rank.set_value(56)

player_6 = Player(
    name=name, forname=forname, birth_date=birth_date, gender=gender, rank=rank
)

# _________PLAYER 7___________
serialized_player_7 = {
    "name": "gosselin",
    "forname": "jessamine",
    "birth_date": "01/10/2002",
    "gender": "F",
    "rank": 5,
}
name.set_value("gosselin")
forname.set_value("jessamine")
birth_date.set_value("01/10/2002")
gender.set_value("F")
rank.set_value(5)

player_7 = Player(
    name=name, forname=forname, birth_date=birth_date, gender=gender, rank=rank
)

# _________PLAYER 8___________
serialized_player_8 = {
    "name": "guernon",
    "forname": "alice",
    "birth_date": "22/06/1994",
    "gender": "F",
    "rank": 59,
}
name.set_value("guernon")
forname.set_value("alice")
birth_date.set_value("22/06/1994")
gender.set_value("F")
rank.set_value(59)

player_8 = Player(
    name=name, forname=forname, birth_date=birth_date, gender=gender, rank=rank
)

# _________MATCH 1___________
serialized_match_1 = {
    "player_1": {"player": serialized_player_1, "score": 1, "color": "black"},
    "player_2": {"player": serialized_player_2, "score": 0, "color": "white"},
}

match_1 = Match(player_1, player_2)
match_1.player_1["score"] = 1
match_1.player_1["color"] = "black"
match_1.player_2["score"] = 0
match_1.player_2["color"] = "white"

# _________MATCH 2___________
serialized_match_2 = {
    "player_1": {"player": serialized_player_3, "score": 1, "color": "black"},
    "player_2": {"player": serialized_player_4, "score": 0, "color": "white"},
}

match_2 = Match(player_3, player_4)
match_2.player_1["score"] = 1
match_2.player_1["color"] = "black"
match_2.player_2["score"] = 0
match_2.player_2["color"] = "white"

# _________MATCH 3___________
serialized_match_3 = {
    "player_1": {"player": serialized_player_5, "score": 0.5, "color": "black"},
    "player_2": {"player": serialized_player_6, "score": 0.5, "color": "white"},
}

match_3 = Match(player_5, player_6)
match_3.player_1["score"] = 0.5
match_3.player_1["color"] = "black"
match_3.player_2["score"] = 0.5
match_3.player_2["color"] = "white"

# _________MATCH 4___________
serialized_match_4 = {
    "player_1": {"player": serialized_player_7, "score": 0, "color": "black"},
    "player_2": {"player": serialized_player_8, "score": 1, "color": "white"},
}

match_4 = Match(player_7, player_8)
match_4.player_1["score"] = 0
match_4.player_1["color"] = "black"
match_4.player_2["score"] = 1
match_4.player_2["color"] = "white"

# _________MATCH 5___________
serialized_match_5 = {
    "player_1": {"player": serialized_player_2, "score": 0, "color": "white"},
    "player_2": {"player": serialized_player_7, "score": 1, "color": "black"},
}

match_5 = Match(player_2, player_7)
match_5.player_1["score"] = 0
match_5.player_1["color"] = "white"
match_5.player_2["score"] = 1
match_5.player_2["color"] = "black"

# _________MATCH 6___________
serialized_match_6 = {
    "player_1": {"player": serialized_player_4, "score": 0.5, "color": "black"},
    "player_2": {"player": serialized_player_2, "score": 0.5, "color": "white"},
}

match_6 = Match(player_4, player_2)
match_6.player_1["score"] = 0.5
match_6.player_1["color"] = "black"
match_6.player_2["score"] = 0.5
match_6.player_2["color"] = "white"

# _________MATCH 7___________
serialized_match_7 = {
    "player_1": {"player": serialized_player_1, "score": 1, "color": "white"},
    "player_2": {"player": serialized_player_6, "score": 0, "color": "black"},
}

match_7 = Match(player_1, player_6)
match_7.player_1["score"] = 1
match_7.player_1["color"] = "white"
match_7.player_2["score"] = 0
match_7.player_2["color"] = "black"

# _________MATCH 8___________
serialized_match_8 = {
    "player_1": {"player": serialized_player_3, "score": 0, "color": "black"},
    "player_2": {"player": serialized_player_2, "score": 1, "color": "white"},
}

match_8 = Match(player_3, player_2)
match_8.player_1["score"] = 0
match_8.player_1["color"] = "black"
match_8.player_2["score"] = 1
match_8.player_2["color"] = "white"

# _________MATCH 9___________
serialized_match_9 = {
    "player_1": {"player": serialized_player_8, "score": 0, "color": "white"},
    "player_2": {"player": serialized_player_4, "score": 1, "color": "black"},
}

match_9 = Match(player_8, player_4)
match_9.player_1["score"] = 0
match_9.player_1["color"] = "white"
match_9.player_2["score"] = 1
match_9.player_2["color"] = "black"

# _________MATCH 10___________
serialized_match_10 = {
    "player_1": {"player": serialized_player_5, "score": 0.5, "color": "black"},
    "player_2": {"player": serialized_player_7, "score": 0.5, "color": "white"},
}

match_10 = Match(player_5, player_7)
match_10.player_1["score"] = 0.5
match_10.player_1["color"] = "black"
match_10.player_2["score"] = 0.5
match_10.player_2["color"] = "white"

# _________MATCH 11___________
serialized_match_11 = {
    "player_1": {"player": serialized_player_1, "score": 0.5, "color": "black"},
    "player_2": {"player": serialized_player_5, "score": 0.5, "color": "white"},
}

match_11 = Match(player_1, player_5)
match_11.player_1["score"] = 0.5
match_11.player_1["color"] = "black"
match_11.player_2["score"] = 0.5
match_11.player_2["color"] = "white"

# _________MATCH 12___________
serialized_match_12 = {
    "player_1": {"player": serialized_player_2, "score": 1, "color": "white"},
    "player_2": {"player": serialized_player_8, "score": 0, "color": "black"},
}

match_12 = Match(player_2, player_8)
match_12.player_1["score"] = 1
match_12.player_1["color"] = "white"
match_12.player_2["score"] = 0
match_12.player_2["color"] = "black"

# _________MATCH 13___________
serialized_match_13 = {
    "player_1": {"player": serialized_player_3, "score": 0, "color": "black"},
    "player_2": {"player": serialized_player_6, "score": 1, "color": "white"},
}

match_13 = Match(player_3, player_6)
match_13.player_1["score"] = 0
match_13.player_1["color"] = "black"
match_13.player_2["score"] = 1
match_13.player_2["color"] = "white"

# _________MATCH 14___________
serialized_match_14 = {
    "player_1": {"player": serialized_player_4, "score": 0, "color": "white"},
    "player_2": {"player": serialized_player_7, "score": 1, "color": "black"},
}

match_14 = Match(player_4, player_7)
match_14.player_1["score"] = 0
match_14.player_1["color"] = "white"
match_14.player_2["score"] = 1
match_14.player_2["color"] = "black"

# _________MATCH 15___________
serialized_match_15 = {
    "player_1": {"player": serialized_player_1, "score": 0, "color": "white"},
    "player_2": {"player": serialized_player_7, "score": 1, "color": "black"},
}

match_15 = Match(player_1, player_7)
match_15.player_1["score"] = 0
match_15.player_1["color"] = "white"
match_15.player_2["score"] = 1
match_15.player_2["color"] = "black"

# _________MATCH 16___________
serialized_match_16 = {
    "player_1": {"player": serialized_player_2, "score": 0, "color": "black"},
    "player_2": {"player": serialized_player_4, "score": 1, "color": "white"},
}

match_16 = Match(player_2, player_4)
match_16.player_1["score"] = 0
match_16.player_1["color"] = "black"
match_16.player_2["score"] = 1
match_16.player_2["color"] = "white"

# _________MATCH 17___________
serialized_match_17 = {
    "player_1": {"player": serialized_player_5, "score": 0, "color": "white"},
    "player_2": {"player": serialized_player_3, "score": 1, "color": "black"},
}

match_17 = Match(player_5, player_3)
match_17.player_1["score"] = 0
match_17.player_1["color"] = "white"
match_17.player_2["score"] = 1
match_17.player_2["color"] = "black"

# _________MATCH 18___________
serialized_match_18 = {
    "player_1": {"player": serialized_player_6, "score": 1, "color": "black"},
    "player_2": {"player": serialized_player_8, "score": 0, "color": "white"},
}

match_18 = Match(player_6, player_8)
match_18.player_1["score"] = 1
match_18.player_1["color"] = "black"
match_18.player_2["score"] = 0
match_18.player_2["color"] = "white"

# _________ROUND 1___________
serialized_round_1 = {
    "name": "round1",
    "begin_date_time": "12/05/2015 10:25:12",
    "end_date_time": "12/05/2015 15:36:15",
    "match": [
        serialized_match_1,
        serialized_match_2,
        serialized_match_3,
        serialized_match_4,
    ],
    "is_done": True,
}

round_1 = Round("round1")
round_1.begin_date_time = datetime.strptime("12/05/2015 10:25:12", "%d/%m/%Y %X")
round_1.end_date_time = datetime.strptime("12/05/2015 15:36:15", "%d/%m/%Y %X")
round_1.match = [match_1, match_2, match_3, match_4]
round_1.is_done = True

# _________ROUND 2___________
serialized_round_2 = {
    "name": "round2",
    "begin_date_time": "15/10/2005 12:25:50",
    "end_date_time": "15/10/2005 18:36:45",
    "match": [
        serialized_match_1,
        serialized_match_3,
        serialized_match_4,
        serialized_match_6,
    ],
    "is_done": True,
}

round_2 = Round("round2")
round_2.begin_date_time = datetime.strptime("15/10/2005 12:25:50", "%d/%m/%Y %X")
round_2.end_date_time = datetime.strptime("15/10/2005 18:36:45", "%d/%m/%Y %X")
round_2.match = [match_1, match_3, match_4, match_6]
round_2.is_done = True

# _________ROUND 3___________
serialized_round_3 = {
    "name": "round3",
    "begin_date_time": "13/05/2015 09:10:35",
    "end_date_time": "13/05/2015 10:35:26",
    "match": [
        serialized_match_7,
        serialized_match_8,
        serialized_match_9,
        serialized_match_10,
    ],
    "is_done": True,
}

round_3 = Round("round3")
round_3.begin_date_time = datetime.strptime("13/05/2015 09:10:35", "%d/%m/%Y %X")
round_3.end_date_time = datetime.strptime("13/05/2015 10:35:26", "%d/%m/%Y %X")
round_3.match = [match_7, match_8, match_9, match_10]
round_3.is_done = True

# _________ROUND 4___________
serialized_round_4 = {
    "name": "round4",
    "begin_date_time": "13/05/2015 11:15:30",
    "end_date_time": "13/05/2015 11:25:45",
    "match": [
        serialized_match_11,
        serialized_match_12,
        serialized_match_13,
        serialized_match_14,
    ],
    "is_done": True,
}

round_4 = Round("round4")
round_4.begin_date_time = datetime.strptime("13/05/2015 11:15:30", "%d/%m/%Y %X")
round_4.end_date_time = datetime.strptime("13/05/2015 11:25:45", "%d/%m/%Y %X")
round_4.match = [match_11, match_12, match_13, match_14]
round_4.is_done = True

# _________ROUND 5___________
serialized_round_5 = {
    "name": "round5",
    "begin_date_time": "13/05/2015 13:18:15",
    "end_date_time": "13/05/2015 13:49:32",
    "match": [
        serialized_match_15,
        serialized_match_16,
        serialized_match_17,
        serialized_match_18,
    ],
    "is_done": True,
}

round_5 = Round("round5")
round_5.begin_date_time = datetime.strptime("13/05/2015 13:18:15", "%d/%m/%Y %X")
round_5.end_date_time = datetime.strptime("13/05/2015 13:49:32", "%d/%m/%Y %X")
round_5.match = [match_15, match_16, match_17, match_18]
round_5.is_done = True

# _________Set up Tournament variable_________
name = Property()
location = Property()
date = DateProperty()
duration = Property()
number_of_round = Property()
time_control = MultipleChoicesProperty()
time_control.list_value = TIME_CONTROLE_STANDARD
description = Property()

# _________TOURNAMENT 1___________
serialised_tournament_1 = {
    "name": "test1",
    "location": "montpelier",
    "date": "15/12/1988",
    "duration": 1,
    "number_of_round": 5,
    "time_control": "blitz",
    "rounds": [serialized_round_1],
    "players": [
        serialized_player_1,
        serialized_player_2,
        serialized_player_3,
        serialized_player_4,
        serialized_player_5,
        serialized_player_6,
        serialized_player_7,
        serialized_player_8,
    ],
    "description": "truc machin",
    "current_round": 1,
}

name.set_value("test1")
location.set_value("montpelier")
date.set_value("15/12/1988")
duration.set_value(1)
number_of_round.set_value(5)
time_control.set_value("2")
description.set_value("truc machin")

tournament_1 = TournamentSwiss(
    name=name,
    location=location,
    date=date,
    duration=duration,
    number_of_round=number_of_round,
    time_control=time_control,
    description=description,
)
tournament_1.rounds = [round_1]
tournament_1.players = [
    player_1,
    player_2,
    player_3,
    player_4,
    player_5,
    player_6,
    player_7,
    player_8,
]
tournament_1.current_round = 1

# _________TOURNAMENT 2___________
serialised_tournament_2 = {
    "name": "test2",
    "location": "paris",
    "date": "10/04/2010",
    "duration": 2,
    "number_of_round": 4,
    "time_control": "bullet",
    "rounds": [serialized_round_2],
    "players": [
        serialized_player_1,
        serialized_player_2,
        serialized_player_3,
        serialized_player_4,
        serialized_player_5,
        serialized_player_6,
        serialized_player_7,
        serialized_player_8,
    ],
    "description": "bazar",
    "current_round": 1,
}

name.set_value("test2")
location.set_value("paris")
date.set_value("10/04/2010")
duration.set_value(2)
number_of_round.set_value(4)
time_control.set_value("1")
description.set_value("bazar")

tournament_2 = TournamentSwiss(
    name=name,
    location=location,
    date=date,
    duration=duration,
    number_of_round=number_of_round,
    time_control=time_control,
    description=description,
)
tournament_2.rounds = [round_2]
tournament_2.players = [
    player_1,
    player_2,
    player_3,
    player_4,
    player_5,
    player_6,
    player_7,
    player_8,
]
tournament_2.current_round = 1

# _________TOURNAMENT 3___________
serialised_tournament_3 = {
    "name": "test3",
    "location": "Bordeaux",
    "date": "12/05/2015",
    "duration": 3,
    "number_of_round": 4,
    "time_control": "bullet",
    "rounds": [
        serialized_round_1,
        serialized_round_3,
        serialized_round_4,
        serialized_round_5,
    ],
    "players": [
        serialized_player_1,
        serialized_player_2,
        serialized_player_3,
        serialized_player_4,
        serialized_player_5,
        serialized_player_6,
        serialized_player_7,
        serialized_player_8,
    ],
    "description": "bazar",
    "current_round": 1,
}

name.set_value("test3")
location.set_value("Bordeaux")
date.set_value("12/05/2015")
duration.set_value(3)
number_of_round.set_value(4)
time_control.set_value("1")
description.set_value("bazar")

tournament_2 = TournamentSwiss(
    name=name,
    location=location,
    date=date,
    duration=duration,
    number_of_round=number_of_round,
    time_control=time_control,
    description=description,
)
tournament_2.rounds = [round_1, round_3, round_4, round_5]
tournament_2.players = [
    player_1,
    player_2,
    player_3,
    player_4,
    player_5,
    player_6,
    player_7,
    player_8,
]
tournament_2.current_round = 4
