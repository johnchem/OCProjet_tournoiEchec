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
	except:
		return False	

def load_tournament_data(tournament, dbFile):
	db = TinyDB(dbFile)
	players_table = db.table('tournament')
	return players_table.all()

if __name__ == "__main__":
	import os
	import pathlib
	print(pathlib.Path(__file__).parent.absolute().joinpath("tutu.py"))

