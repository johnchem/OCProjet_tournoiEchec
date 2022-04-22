from chess_tournament.models.player import Player
from chess_tournament.models.tournament import TournamentSwiss
from tinydb import TinyDB

def save_player_data(player, dbFile):
	'''
	player : dictionnary 
	db_file : path

	'''
	try :
		db = TinyDB(dbFile)
		players_table = db.table('players')
		#players_table.truncate()	# clear the table first
		if player["id"] is None:
			id_number = players_table.insert(player)
			return True, id_number
		else:
			players_table.update(player, doc_id = player["id"])
		return True, player["id"]
	except BaseException as err:
		print(err)
		return False

def load_player_data(dbFile):
	try :
		db = TinyDB(dbFile)
		players_table = db.table('players')
		return players_table.all()
	except BaseException as err:
		print(err)
		return err

def save_tournament_data(tournament, dbFile):
	try : 
		db = TinyDB(dbFile)
		tournament_table = db.table('tournament')
		if tournament["id"] is None:
			id_number = tournament_table.insert(tournament)
			tournament["id"] = id_number
		else:
			tournament_table.update(tournament, doc_id = tournament["id"])
		return True
	except BaseException as err:
		print(err)
		return False

def load_tournament_data(dbFile):
	try :
		db = TinyDB(dbFile)
		players_table = db.table('tournament')
		result = players_table.all()
		return result
	except BaseException as err:
		print(err)
		return err

if __name__ == "__main__":
	pass