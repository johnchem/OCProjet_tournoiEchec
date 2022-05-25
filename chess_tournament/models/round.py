from datetime import datetime
import copy


class Round:
    """
    _________________________
    nom : str
    begin_date_time : datetime
    end_date_time : datetime
    match : [match]
    is_done = bool

    -------------------------
    .addMatch(match) -> None
    .end_round() -> None
    .get_match_list() -> none
    """

    def __init__(self, name: str):
        self.name = name
        self.begin_date_time = datetime.now()
        self.end_date_time = None
        self.match = []
        self.is_done = False

    def add_match(self, match):
        self.match.append(match)

    def end_round(self):
        self.end_date_time = datetime.now()
        self.is_done = True

    def get_match_list(self):
        pass

    def set_result(self):
        pass

    def get_players_opponent(self):
        list_opponent = []
        for match in self.match:
            list_opponent.append((match.player_1["player"], match.player_2["player"]))
            list_opponent.append((match.player_2["player"], match.player_1["player"]))
        return list_opponent

    def get_players_score(self):
        score_player = []
        for match in self.match:
            score_player.append((match.player_1["player"], match.player_1["score"]))
            score_player.append((match.player_2["player"], match.player_2["score"]))
        return score_player

    def serialize(self):
        serialized_round = copy.deepcopy(vars(self))
        serialized_round["begin_date_time"] = serialized_round[
            "begin_date_time"
        ].strftime("%d/%m/%Y %X")
        if self.end_date_time:
            serialized_round["end_date_time"] = serialized_round[
                "end_date_time"
            ].strftime("%d/%m/%Y %X")
        else:
            del serialized_round["end_date_time"]
        serialized_round["match"] = [x.serialize() for x in self.match]
        return serialized_round

    def __repr__(self):
        if self.is_done:
            return (
                f"{self.name}"
                f' le {self.begin_date_time.strftime("%d/%m/%Y")}'
                f' entre {self.begin_date_time.strftime("%X")}'
                f' et {self.end_date_time.strftime("%X")}'
            )
        else:
            return (
                f"{self.name}"
                f' le {self.begin_date_time.strftime("%d/%m/%Y")}'
                f' en cours depuis {self.begin_date_time.strftime("%X")}'
            )

    def __eq__(self, other):
        if not isinstance(other, Round):
            # don't attempt to compare against unrelated types
            return NotImplemented
        # compare the different matchs
        # store true in a list is a match is not found
        match_compare = []
        for x in self.match:
            match_not_found = True
            for y in other.match:
                if x == y:
                    match_not_found = False
            match_compare.append(match_not_found)

        list_compare = [
            self.name != other.name,
            self.begin_date_time != other.begin_date_time,
            self.end_date_time != other.end_date_time,
            *match_compare,
        ]
        # return false if any difference exist between self and other
        return not any(list_compare)
