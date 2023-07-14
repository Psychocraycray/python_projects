import random


class Cards:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank['rank']} of {self.suit}"


class Deck:  # this is the class that holds the deck of cards
    def __init__(self):
        self.cards = []
        suits = ["spades", "clubs", "hearts", "diamonds"]
        ranks = [
               {"rank": "A", "value": 11},
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
        for suit in suits:
            for rank in ranks:
                self.cards.append(Cards(suit, rank))  # we are using the for loop to list the cards

    def shuffle(self):  # this method is shuffling the deck we want to be out_put
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self, number):  # this method is doing the dealing of cards
        cards_dealt = []
        for c in range(number):
            if len(self.cards) > 0:
                card = self.cards.pop()
                cards_dealt.append(card)
        return cards_dealt


card1 = Cards("heart", {"rank": "J", "value": 10})
print(card1)
