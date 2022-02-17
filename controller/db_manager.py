from tinydb import TinyDB

def save_player_data(players, dbFile):
	try : 
		db = TinyDB(dbFile)
		players_table = db.table('players')
		players_table.truncate()	# clear the table first
		players_table.insert_multiple(serialized_players)
		return True
	except:
		return False

def load_player_data(dbFile):
	db = TinyDB(dbFile)
	players_table = db.table('players')
	return players_table.all()

def save_tournament_data(tournament, dbFile):
	try : 
		db = TinyDB(dbFile)
		tournament_table = db.table('tournament')
		tournament_table.truncate()	# clear the table first
		tournament_table.insert_multiple(serialized_players)
		return True
	except BaseException as err:
		return err

def load_tournament_data(dbFile):
	try :
		db = TinyDB(dbFile)
		players_table = db.table('tournament')
		return players_table.all()
	except BaseException as err:
		return err

if __name__ == "__main__":
	import os
	import pathlib
	
	from chess_tournament.models.player import Player
	from chess_tournament.models.tournament import TournamentSwiss, TIME_CONTROLE_STANDARD
	from chess_tournament.models.property import Property
	from chess_tournament.models.dateProperty import DateProperty
	from chess_tournament.models.multipleChoicesProperty import MultipleChoicesProperty
	from chess_tournament.models.genderProperty import GenderProperty

	name = Property("Nom : ")
	name.set_value("toto")
	location = Property("Lieu : ")
	location.set_value("tours")
	date = DateProperty("Date (JJ/MM/YYYY): ")
	date.set_value("12/01/2021")
	duration = Property("Durée : ")
	duration.set_value(1)
	round_nbr = Property("Nombre de tours (defaut 4) : ")
	round_nbr.set_value(4)
	time_control = MultipleChoicesProperty("test", 
			"blitz", "test")
	time_control.set_value("blitz")
	description = Property("Desciption : \n")
	description.set_value("test1")

	tournois = TournamentSwiss(name = name, 
							location = location, 
							date = date,
							duration = duration,
							number_of_round = round_nbr,
							description = description)

	name = Property("name")
	forname = Property("forname")
	birth_date = DateProperty("birth_date")
	gender = GenderProperty("gender")
	rank = Property("rank")
	
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
	birth_date.set_value("15/18/1955")
	gender.set_value("F")
	rank.set_value(100)
	joueur3 = Player(name, forname, birth_date, gender, rank)

	DB_ADDRESS = pathlib.Path(__file__).parent.absolute().joinpath("DB_unitest.json") # absolule path
	save_player_data([joueur1.serialize], DB_ADDRESS)