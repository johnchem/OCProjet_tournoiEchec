# importation des modules
import os
import pathlib

# importation des modeles
from chess_tournament.models.player import Player
from chess_tournament.models.tournament import TournamentSwiss, TIME_CONTROLE_STANDARD
from chess_tournament.models.property import Property
from chess_tournament.models.date_property import DateProperty
from chess_tournament.models.multiple_choices_property import MultipleChoicesProperty
from chess_tournament.models.gender_property import GenderProperty

#importation du controlleur
from chess_tournament.controller.db_manager import save_player_data, save_tournament_data

def test_save_tournament(tournament, db_file):
	serialized_tournament = tournament.serialize()
	try:
		save_tournament_data(serialized_tournament, db_file)
		print(serialized_tournament)
	except BaseException as err:
		return err


def test_save_players(players, db_file):
	players_serialized = []
	for player in players:
		players_serialized.append(player.serialize())
	print(players_serialized)
	save_player_data(players_serialized, db_file)


def create_dummy_tournament():
	name = Property()
	location = Property()
	date = DateProperty()
	duration = Property()
	round_nbr = Property()
	time_control = MultipleChoicesProperty()
	description = Property()
	
	name.set_value("toto")
	location.set_value("tours")
	date.set_value("12/05/2021")
	duration.set_value(1)
	round_nbr.set_value(4)
	time_control.list_value = TIME_CONTROLE_STANDARD
	time_control.set_value("1")
	description.set_value("test1")

	tournois = TournamentSwiss(name = name, 
							location = location, 
							date = date,
							duration = duration,
							time_control = time_control,
							number_of_round = round_nbr,
							description = description)
	return tournois


def create_dummy_player():
	name = Property()
	forname = Property()
	birth_date = DateProperty()
	gender = GenderProperty()
	rank = Property()
	
	name.set_value("paul")
	forname.set_value("michel")
	birth_date.set_value("01/01/2001")
	gender.set_value("H")
	rank.set_value(0)
	joueur1 = Player(name, forname, birth_date, gender, rank)

	name.set_value("george")
	forname.set_value("louis")
	birth_date.set_value("10/05/1995")
	gender.set_value("H")
	rank.set_value(10)
	joueur2 = Player(name, forname, birth_date, gender, rank)

	name.set_value("paulette")
	forname.set_value("vuiton")
	birth_date.set_value("15/11/1955")
	gender.set_value("F")
	rank.set_value(100)
	joueur3 = Player(name, forname, birth_date, gender, rank)

	return [joueur1, joueur2, joueur3]

if __name__ == "__main__":
	DB_ADDRESS = pathlib.Path(__file__).parent.absolute().joinpath("DB_unitest.json") # absolule path
	test_save_players(create_dummy_player(), DB_ADDRESS)
	test_save_tournament(create_dummy_tournament(), DB_ADDRESS)