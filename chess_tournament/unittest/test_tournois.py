import copy
import random 

from chess_tournament.models.tournament import TournamentSwiss
from chess_tournament.models.player import Player

from chess_tournament.models.property import Property
from chess_tournament.models.date_property import DateProperty
from chess_tournament.models.multiple_choices_property import MultipleChoicesProperty

from chess_tournament.unittest.test_data import *

def test_create_tournament():
	name = Property()
	location = Property()
	date = DateProperty()
	duration = Property()
	number_of_round = Property()
	time_control = MultipleChoicesProperty()
	time_control.list_value = TIME_CONTROLE_STANDARD
	description = Property()
	
	name.set_value("test1")
	location.set_value("montpelier")
	date.set_value("15/12/1988")
	duration.set_value(1)
	number_of_round.set_value(5)
	time_control.set_value("2")
	description.set_value("truc machin")

	tournament = TournamentSwiss(name = name,
							   location = location,
							   date = date,
							   duration = duration,
							   number_of_round = number_of_round,
							   time_control = time_control,
							   description = description)

	assert isinstance(tournament, TournamentSwiss)
	assert tournament.name == "test1"
	assert tournament.location == "montpelier"
	assert tournament.date == datetime.strptime("15/12/1988", "%d/%m/%Y")
	assert tournament.duration == 1
	assert tournament.number_of_round == 5
	assert tournament.time_control == TIME_CONTROLE_STANDARD[1]
	assert tournament.description == "truc machin"

def test_add_player():
	#get testing data
	tournament == copy.deepcopy(tournament_1)
	player == copy.deepcopy(player_1)

	#initialise and control the initial setup
	tournament.players = []
	assert len(tournament.players) == 0
	
	#testing
	tournament.add_player(player)
	assert len(tournament.players) == 1
	assert tournament.players[0] == player

def test_if_tournament_is_full():
	#get testing data
	tournament == copy.deepcopy(tournament_1)
	player == copy.deepcopy(player_1)

	#initialise and control the initial setup
	assert len(tournament.players) == 8
	
	#testing
	tournament.add_player(player)
	assert len(tournament.players) == 9
	assert tournament.players[-1] == player

def test_start_new_round():
	#get testing data
	tournament == copy.deepcopy(tournament_1)

	#initialize data
	tournament.current_round = 1
	tournament.rounds = []
	name_round = f'round{tournament.current_round}'
	round = Round(name_round)

	#testing
	tournament.start_new_tournament(round)
	assert tournament[-1].name == "round1"
	assert (datetime.now - tournament.begin_date_time).seconds < 10
	assert tournament.end_date_time == None
	assert len(tournament.match) == 0
	assert tournament.is_done == False

def test_generation_pairs_players():
	pass


def test_end_a_round():
	#get testing data
	tournament == copy.deepcopy(tournament_1)

	#initialize data
	tournament.current_round = 1
	tournament.rounds = []
	name_round = f'round{tournament.current_round}'
	round = Round# (name_round)
	tournament.start_new_tournament(round)

	#testing
	tournament.end_round()
	assert (datetime.now - tournament.end_date_time).seconds < 10
	assert tournament.is_done == True

def test_set_result_round():
	#get testing data
	tournament == copy.deepcopy(tournament_1)

	#initialize data
	tournament.current_round = 1
	tournament.rounds = []
	name_round = f'round{tournament.current_round}'
	round = Round(name_round)
	tournament.start_new_tournament(round)
	tournament.end_round()

	#testing
	assert (datetime.now - tournament.end_date_time).seconds < 10
	assert tournament.is_done == True

def test_add_round():
	#get 
	pass

def test_create_round(tournament, round_nb):
	tournament.player_group_generation()
	# assert is tournament.round, "truc" 
	for match in tournament.round[round_nb]:
		print(match)

def test_match(liste_joueur):
	liste_match = []
	liste_score = [0, 1, 0.5]
	for i in range(1,9):
		(joueur1, joueur2) = random.choices(liste_joueur, k=2)
		(score1, score2) = random.choices(liste_score, k=2)
		liste_match.append(tournois.match(joueur1, score1, joueur2, score2))
	[print(x) for x in liste_match]
	pass

if __name__ == "__main__":
	nvxJoueur = [("Tardiff", "Stephanie", "26/09/1967", "F", 15),
				("Connie", "Lam", "10/06/1986", "F", 12),
				("Cleveland","Noon","03/11/1938","M", 5),
				("Disalvo","Aaron","13/09/1967","M", 65),
				("Digiacomo","David","13/09/1944","M", 41),
				("Adela","Scanlon","10/01/1951","F", 11),
				("Galbraith","Rosemary","03/11/1970","F", 8),
				("Burroughs","Eric","03/09/1967","M",3)]
	
	name = Property()
	forname = Property()
	birth_date = DateProperty()
	gender = GenderProperty()
	rank = Property()

	liste_joueur = []
	for nom, prenom, date_de_naissance, sexe, classement in nvxJoueur:
		
		name.set_value(name)
		forname.set_value(prenom)
		birth_date.set_value(date_de_naissance)
		gender.set_value(sexe)
		rank.set_value(classement)
		
		liste_joueur.append(
			Player(name, forname, birth_date, gender, rank)
		)

	list_players_sorted = sorted(liste_joueur, key=lambda x : x.classement)

	for player in liste_joueur:
		print(f"joueur : {player.name} classement : {player.classement}")

	print("\n")
	
	for player in list_players_sorted:
		print(f"joueur : {player.name} classement : {player.classement}")