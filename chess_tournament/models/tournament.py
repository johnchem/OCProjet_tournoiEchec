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
        self.number_of_round = int(number_of_round.value)
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
        # reset dict_opponent
        self.dict_opponent = {key: list() for key in self.dict_opponent.keys()}
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
        # reset dict_score
        self.dict_score = dict.fromkeys(self.dict_score, 0)
        # list of player and score for all the played match
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
        compare the round, as there are ordered,
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
            self._current_round != other._current_round,
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

        def sort_by_score(x): return (x[1])
        def sort_by_rank(x): return (x[2])
        # sort the players by score then rank
        list_players_sorted.sort(key=sort_by_rank, reverse=False)
        list_players_sorted.sort(key=sort_by_score, reverse=True)
        # remove the values used for the sorting
        list_players_sorted = [x[0] for x in list_players_sorted]
        print(list_players_sorted)

        return players_already_faced(list_players_sorted, self.dict_opponent)


def players_already_faced(sorted_players, comparison_dict):
    list_1, list_2 = [], []
    for player in sorted_players:
        if player in list_1 or player in list_2:
            continue

        # list of the remaining adversaire sorted
        def available(adv, player):
            test_1 = adv.name not in comparison_dict[player.name]
            test_2 = adv not in list_1 + list_2
            test_3 = adv != player
            return test_1 and test_2 and test_3
        player_available = [p for p in sorted_players if available(p, player)]

        # 1st player go to 1st list
        list_1.append(player)

        # adversaire go to the 2nd list
        first_available_player = player_available[0]
        list_2.append(first_available_player)

    return zip(list_1, list_2)


if __name__ == "__main__":
    pass
