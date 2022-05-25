from math import trunc
import copy

TIME_CONTROLE_STANDARD = ["bullet", "blitz", "coup rapide"]


class Tournament:
    """
    _________________________
    name.value : str
    location.value : str
    date.value : datetime
    duration.value : int
    number_of_round.value : int
    time_control.value : str
    rounds : [round]
    players : [player]
    number_of_round.value : int
    description.value : str
    current_round = 0
    dict_opponent = {}
    dict_score = {}
    id = int
    """

    def __init__(
        self,
        *,
        name,
        location,
        date,
        duration,
        time_control,
        number_of_round=4,
        description="",
    ):
        self.name = name.value
        self.location = location.value
        self.date = date.value
        self.duration = duration.value
        self.number_of_round = number_of_round.value
        self.time_control = time_control.value
        self.rounds = []
        self.players = []
        self.description = description.value
        self._current_round = 0
        self.dict_opponent = {}
        self.dict_score = {}
        self.id = ""  # generated and handle with db

    def add_player(self, player):
        """add a new player in the tournament"""
        self.players.append(player)
        # add the player in the tracking dict.
        self.dict_score[player.name] = 0
        self.dict_opponent[player.name] = []

    def is_full(self):
        """check if there are 8 and no more players"""
        if len(self.players) >= 8:
            return True
        else:
            return False

    def start_new_round(self):
        return self.player_group_generation()

    def end_round(self):
        self.rounds[self.current_round - 1].end_round()

    def set_result(self):
        self.rounds[self.current_round - 1].set_result()

    def player_group_generation(self):
        """not implemented from standart tournament"""
        pass

    def get_players_opponent(self):
        tmp_list = []
        # list of all the match
        for round_played in self.rounds:
            tmp_list += round_played.get_players_opponent()

        # list the opponnent faced by a player
        for player, opponent in tmp_list:
            if player.name in self.dict_opponent:
                self.dict_opponent[player.name].append(opponent.name)
            else:
                self.dict_opponent[player.name] = [opponent.name]

    def get_players_score(self):
        tmp_list = [
            match for x in self.rounds if x.is_done for match in x.get_players_score()
        ]

        for player, score in tmp_list:
            if player.name in self.dict_score:
                self.dict_score[player.name] += score
            else:
                self.dict_score[player.name] = score

    def serialize(self):
        serialized_tournament = copy.deepcopy(vars(self))
        del serialized_tournament["dict_opponent"]
        del serialized_tournament["dict_score"]
        serialized_tournament["date"] = serialized_tournament["date"].strftime(
            "%d/%m/%Y"
        )
        serialized_tournament["players"] = [x.serialize() for x in self.players]
        serialized_tournament["rounds"] = [x.serialize() for x in self.rounds]
        return serialized_tournament

    def __str__(self):
        a = [
            f"Nom : {self.name}",
            f"Lieu : {self.location}",
            f"A partir du {self.date} pendant {self.duration} jours",
            f"{self.number_of_round} tours avec la régle {self.time_control}",
        ]
        return "\n".join(a)

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            # don't attempt to compare against unrelated types
            return NotImplemented

        """
        compare the rounda, as there are ordered,
        they can be compare side to side
        """
        for x, y in zip(self.rounds, other.rounds):
            if x != y:
                return False

        """
        iterate through the players list and record if
        they are a match or not
        """
        player_compare = []
        for x in self.players:
            player_not_found = True
            for y in other.players:
                if x == y:
                    player_not_found = False
            player_compare.append(player_not_found)

        list_compare = [
            self.name != other.name,
            self.location != other.location,
            self.date != other.date,
            self.duration != other.duration,
            self.number_of_round != other.number_of_round,
            self.time_control != other.time_control,
            *player_compare,
            self.description != other.description,
            self.current_round != other.current_round,
        ]
        # return False if any difference exist between self and other
        return not any(list_compare)

    def get_current_round(self):
        return len(self.rounds)

    def set_current_round(self, value):
        self._current_round = value

    current_round = property(get_current_round, set_current_round)


class TournamentSwiss(Tournament):
    """tournament with the swiss systeme"""

    def player_group_generation(self):
        # catch if not enough players in the game
        if len(self.players) < 8:
            return None

        # catch 1st tournament round
        if self.current_round == 0:
            # sort the player
            list_players_sorted = sorted(self.players, key=lambda x: int(x.rank))
            # define the middle of the list, which also the number of matches
            nbr_match = trunc(len(list_players_sorted) / 2)
            # split the list in two
            upper_half = list_players_sorted[:nbr_match]
            bottom_half = list_players_sorted[nbr_match:]

            return zip(upper_half, bottom_half)

        # catch error if round >1 but no score recorded or no round history
        if len(self.dict_score) == 0 or len(self.dict_opponent) == 0:
            return None

        # process for any round >1

        # create a list to sort player
        list_players_sorted = []
        for player in self.players:
            list_players_sorted.append(
                (player, self.dict_score[player.name], int(player.rank))
            )

        def sort_function(x): return (x[1], x[2])
        # sort the players by score then rank
        list_players_sorted.sort(key=sort_function)
        # remove the filtering part
        list_players_sorted = [x[0] for x in list_players_sorted]
        # define the middle of the list, which also the number of matches
        nbr_match = trunc(len(list_players_sorted) / 2)
        # split the list in two
        upper_half = list_players_sorted[:nbr_match]
        bottom_half = list_players_sorted[nbr_match:]

        return players_already_faced(upper_half, bottom_half, self.dict_opponent)


def players_already_faced(list_1, list_2, comparison_dict):
    for index, player in enumerate(list_1):
        player2 = list_2[index]

        while comparison_dict[player.name] == player2.name:
            tmp_index = index + 1
            if tmp_index < len(list_2):
                player2 = list_2[tmp_index]
            else:
                # add the next available player
                list_2.insert(index, list_2[tmp_index])
                # remove it from its original place
                list_2.pop(tmp_index + 1)

    return zip(list_1, list_2)


if __name__ == "__main__":
    pass
