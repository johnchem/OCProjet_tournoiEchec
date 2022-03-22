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

name = Property()
forname = Property()
birth_date = DateProperty()
gender = Property()
rank = Property()

#_________PLAYER 1___________
serialized_player_1 = {"name":"paul",
						"forname":"michel",
						"birth_date":"01/01/2001",
						"gender":"H",
						"rank":0}
name.set_value("paul")
forname.set_value("michel")
birth_date.set_value("01/01/2001")
gender.set_value("H")
rank.set_value(0)

player_1 = Player(name = name,
				forname = forname,
				birth_date = birth_date,
				gender = gender,
				rank = rank)

#_________PLAYER 2___________
serialized_player_2 = {"name":"george",
						"forname":"louis",
						"birth_date":"10/05/1995",
						"gender":"H",
						"rank":10}
name.set_value("george")
forname.set_value("louis")
birth_date.set_value("10/05/1995")
gender.set_value("H")
rank.set_value(10)

player_2 = Player(name = name,
				forname = forname,
				birth_date = birth_date,
				gender = gender,
				rank = rank)

#_________PLAYER 3___________
serialized_player_3 = {"name":"paulette",
						"forname":"vuiton",
						"birth_date":"15/11/1955",
						"gender":"F",
						"rank":100}
name.set_value("paulette")
forname.set_value("vuiton")
birth_date.set_value("15/11/1955")
gender.set_value("F")
rank.set_value(100)


player_3 = Player(name = name,
				forname = forname,
				birth_date = birth_date,
				gender = gender,
				rank = rank)

#_________PLAYER 4___________
serialized_player_4 = {"name":"despins",
						"forname":"Amedee",
						"birth_date":"11/12/1977",
						"gender":"F",
						"rank":12}
name.set_value("despins")
forname.set_value("Amedee")
birth_date.set_value("11/12/1977")
gender.set_value("F")
rank.set_value(12)

player_4 = Player(name = name,
				forname = forname,
				birth_date = birth_date,
				gender = gender,
				rank = rank)

#_________PLAYER 5___________
serialized_player_5 = {"name":"baupré",
						"forname":"dominic",
						"birth_date":"28/08/1988",
						"gender":"H",
						"rank":26}
name.set_value("baupré")
forname.set_value("dominic")
birth_date.set_value("28/08/1988")
gender.set_value("H")
rank.set_value(26)

player_5 = Player(name = name,
				forname = forname,
				birth_date = birth_date,
				gender = gender,
				rank = rank)

#_________PLAYER 6___________
serialized_player_6 = {"name":"deserres",
						"forname":"arthur",
						"birth_date":"12/08/1977",
						"gender":"H",
						"rank":56}
name.set_value("deserres")
forname.set_value("arthur")
birth_date.set_value("12/08/1977")
gender.set_value("H")
rank.set_value(56)

player_6 = Player(name = name,
				forname = forname,
				birth_date = birth_date,
				gender = gender,
				rank = rank)						

#_________PLAYER 7___________
serialized_player_7 = {"name":"gosselin",
						"forname":"jessamine",
						"birth_date":"01/10/2002",
						"gender":"F",
						"rank":5}
name.set_value("gosselin")
forname.set_value("jessamine")
birth_date.set_value("01/10/2002")
gender.set_value("F")
rank.set_value(5)

player_7 = Player(name = name,
				forname = forname,
				birth_date = birth_date,
				gender = gender,
				rank = rank)						

#_________PLAYER 8___________
serialized_player_8 = {"name":"guernon",
						"forname":"alice",
						"birth_date":"22/06/1994",
						"gender":"F",
						"rank":59}
name.set_value("guernon")
forname.set_value("alice")
birth_date.set_value("22/06/1994")
gender.set_value("F")
rank.set_value(59)

player_8 = Player(name = name,
				forname = forname,
				birth_date = birth_date,
				gender = gender,
				rank = rank)						

#_________MATCH 1___________
serialized_match_1 = {"player_1":{"player":serialized_player_1,
								"score":1,
								"color":"black"},
					"player_2":{"player":serialized_player_2,
								"score":0,
								"color":"white"}}

match_1 = Match(player_1, player_2)
match_1.player_1["score"] = 1
match_1.player_1["color"] = "black"
match_1.player_2["score"] = 0
match_1.player_2["color"] = "white"

#_________MATCH 2___________
serialized_match_2 = {"player_1":{"player":serialized_player_3,
								"score":1,
								"color":"black"},
					"player_2":{"player":serialized_player_4,
								"score":0,
								"color":"white"}}

match_2 = Match(player_3, player_4)
match_2.player_1["score"] = 1
match_2.player_1["color"] = "black"
match_2.player_2["score"] = 0
match_2.player_2["color"] = "white"

#_________MATCH 3___________
serialized_match_3 = {"player_1":{"player":serialized_player_5,
								"score":0.5,
								"color":"black"},
					"player_2":{"player":serialized_player_6,
								"score":0.5,
								"color":"white"}}

match_3 = Match(player_5, player_6)
match_3.player_1["score"] = 0.5
match_3.player_1["color"] = "black"
match_3.player_2["score"] = 0.5
match_3.player_2["color"] = "white"

#_________MATCH 4___________
serialized_match_4 = {"player_1":{"player":serialized_player_7,
								"score":0,
								"color":"black"},
					"player_2":{"player":serialized_player_8,
								"score":1,
								"color":"white"}}

match_4 = Match(player_7, player_8)
match_4.player_1["score"] = 0
match_4.player_1["color"] = "black"
match_4.player_2["score"] = 1
match_4.player_2["color"] = "white"	

#_________MATCH 5___________
serialized_match_5 = {"player_1":{"player":serialized_player_2,
								"score":0,
								"color":"white"},
					"player_2":{"player":serialized_player_7,
								"score":1,
								"color":"black"}}

match_5 = Match(player_2, player_7)
match_5.player_1["score"] = 0
match_5.player_1["color"] = "white"
match_5.player_2["score"] = 1
match_5.player_2["color"] = "black"

#_________MATCH 6___________
serialized_match_6 = {"player_1":{"player":serialized_player_4,
								"score":0.5,
								"color":"black"},
					"player_2":{"player":serialized_player_2,
								"score":0.5,
								"color":"white"}}

match_6 = Match(player_4, player_2)
match_6.player_1["score"] = 0.5
match_6.player_1["color"] = "black"
match_6.player_2["score"] = 0.5
match_6.player_2["color"] = "white"

#_________ROUND 1___________
serialized_round_1 = {"name":"round1",
					"begin_date_time": "12/05/2015 10:25:12",
					"end_date_time": "12/05/2015 15:36:15",
					"match": [serialized_match_1,
							serialized_match_2,
							serialized_match_3,
							serialized_match_4],
					"is_done": True}

round_1 = Round("round1")
round_1.begin_date_time = datetime.strptime("12/05/2015 10:25:12", "%d/%m/%Y %X")
round_1.end_date_time = datetime.strptime("12/05/2015 15:36:15", "%d/%m/%Y %X")
round_1.match = [match_1, match_2, match_3, match_4]
round_1.is_done = True

#_________ROUND 2___________
serialized_round_2 = {"name":"round2",
					"begin_date_time": "15/10/2005 12:25:50",
					"end_date_time": "15/10/2005 18:36:45",
					"match": [serialized_match_1,
							serialized_match_3,
							serialized_match_4,
							serialized_match_6],
					"is_done": True}

round_2 = Round("round2")
round_2.begin_date_time = datetime.strptime("15/10/2005 12:25:50", "%d/%m/%Y %X")
round_2.end_date_time = datetime.strptime("15/10/2005 18:36:45", "%d/%m/%Y %X")
round_2.match = [match_1, match_3, match_4, match_6]
round_2.is_done = True


#_________TOURNAMENT 1___________
serialised_tournament_1 = {"name":"test1",
						"localtion":"montpelier",
						"date":"15/12/1988",
						"duration": 1,
						"number_of_round": 5,
						"time_control": "blitz",
						"round":[serialized_round_1],
						"player":[serialized_player_1,
								serialized_player_2,
								serialized_player_3,
								serialized_player_4,
								serialized_player_5,
								serialized_player_6,
								serialized_player_7,
								serialized_player_8],
						"description":"truc machin",
						"current_round": 1}