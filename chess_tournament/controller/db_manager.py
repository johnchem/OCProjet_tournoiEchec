from tinydb import TinyDB

def save_player_data(players, dbFile):
	try : 
		db = TinyDB(dbFile)
		players_table = db.table('players')
		#players_table.truncate()	# clear the table first
		players_table.insert_multiple(players)
		return True
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
		#tournament_table.truncate()	# clear the table first
		tournament_table.insert(tournament)
		return True
	except BaseException as err:
		print(err)
		return err

def load_tournament_data(dbFile):
	try :
		db = TinyDB(dbFile)
		players_table = db.table('tournament')
		return players_table.all()
	except BaseException as err:
		print(err)
		return err

if __name__ == "__main__":
	pass