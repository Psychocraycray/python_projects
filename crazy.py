import random


class Cards:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank['rank']} of {self.suit}"


class Deck:
    def __init__(self):
        self.card = []
        suits = ["spades", "clubs", "heart", "diamonds"]
        ranks = [
               {"rank": "A", "value": 5},
               {"rank": "2", "value": 2},
               {"rank": "3", "value": 3},
               {"rank": "4", "value": 4},
               {"rank": "5", "value": 5},
               {"rank": "6", "value": 6},
               {"rank": "7", "value": 7},
               {"rank": "8", "value": 8},
               {"rank": "9", "value": 9},
               {"rank": "10", "value": 10},
               {"rank": "J", "value": 10},
               {"rank": "Q", "value": 10},
               {"rank": "K", "value": 10},
        ]
