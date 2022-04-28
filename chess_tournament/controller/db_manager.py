from chess_tournament.models.player import Player
from chess_tournament.models.tournament import TournamentSwiss
from tinydb import TinyDB

def save_player_data(player, db_file):
	'''
	player : dictionnary 
	db_file : path
	'''
	try :
		db = TinyDB(db_file)
		players_table = db.table('players')
		#players_table.truncate()	# clear the table first
		print("local 1")
		if player["id"] is "":
			print("local 2")
			print(f'player : \n {player}')
			id_number =players_table.insert(player)
			print(type(id_number))
			print(f"id_number {id_number}")
			print("local 3")
			return (True, id_number)
		else:
			players_table.update(player, doc_id = player["id"])
		return (True, player["id"])
	except BaseException as err:
		print(f'error save : {err}')
		return False

def load_player_data(db_file):
	try :
		db = TinyDB(db_file)
		players_table = db.table('players')
		return players_table.all()
	except BaseException as err:
		print(err)
		return err

def save_tournament_data(tournament, db_file):
	try : 
		db = TinyDB(db_file)
		tournament_table = db.table('tournament')
		if tournament["id"] is "":
			id_number = tournament_table.insert(tournament)
			tournament["id"] = id_number
		else:
			tournament_table.update(tournament, doc_id = tournament["id"])
		return True
	except BaseException as err:
		print(err)
		return False

def load_tournament_data(db_file):
	try :
		db = TinyDB(db_file)
		players_table = db.table('tournament')
		result = players_table.all()
		return result
	except BaseException as err:
		print(err)
		return err

if __name__ == "__main__":
	pass