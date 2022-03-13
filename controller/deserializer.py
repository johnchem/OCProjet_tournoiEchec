from chess_tournament.models.property import Property
from chess_tournament.models.date_property import DateProperty
from chess_tournament.models.multiple_choices_property import MultipleChoicesProperty
from chess_tournament.models.tournament import TournamentSwiss

from chess_tournament.models.gender_property import GenderProperty


def deserialize_tournament(**kwarg):
	name = Property()
	name.set_value(kwarg["name"])
	
	location = Property()
	location.set_value(kwarg["location"])
	
	date = DateProperty()
	date.set_value(kwarg["date"])
	
	duration = Property()
	duration.set_value(kwarg["duration"])
	
	number_of_round = Property()
	number_of_round.set_value(kwarg["number_of_round"])

	time_control = MultipleChoicesProperty()
	time_control._set_value(kwarg["time_control"])

	description = Property()
	description.set_value(kwarg["description"])

	tournament = TournamentSwiss(name = name, 
			date = date,
			duration = duration,
			number_of_round = number_of_round,
			description = description,
			location = location,
			time_control = time_control)

	tournament.currentRound = kwarg["currentRound"]
	tournament.round = kwarg["rounds"]
	tournament.players = kwarg["players"]
	return tournament

def deserialize_player(**kwarg):
	if kwarg.has_key("name"):
		name = Property()
		name.set_value(kwarg["name"])
	
	if kwarg.has_key("forname"):
		forname = Property()
		forname.set_value(kwarg["forname"])
	
	if kwarg.has_key("birth_date"):
		birth_date = DateProperty()
		birth_date.set_value(kwarg["birth_date"])
	
	if kwarg.has_key("gender"):
		gender = Property()
		gender.set_value(kwarg["gender"])
	
	if kwarg.has_key("rank"):
		rank = Property()
		rank.set_value(kwarg["forname"])
	
	player = Player(name, forname, birth_date, gender, rank)

	if kwarg.has_key("opponents"):
		player.opponents = kwarg["opponents"]
	return player
