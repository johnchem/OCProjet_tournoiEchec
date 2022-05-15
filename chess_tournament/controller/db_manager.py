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
		if player["id"] == "":
			id_number=players_table.insert(player)
			return True, id_number
		else:
			players_table.update(player, doc_ids = [player["id"]])
		return True, player["id"]
	except BaseException as err:
		print(f'error save : {err}')
		return False, err

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
		if tournament["id"] == "":
			id_number = tournament_table.insert(tournament)
			tournament["id"] = id_number
		else :
			id_number = tournament["id"]
			tournament_table.update(tournament, doc_ids=[id_number])
		return True, id_number
	except BaseException as err:
		print(err)
		return False, err

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