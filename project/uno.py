import random
"""
generate then uno deck of 108 cards.
parameter: None
Return values: deck - > list
"""
import random


def build_deck():
    deck = []
    colours = ["red", "green", "yellow", "blue"]
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "draw two", "skip", "reverse"]
    wilds = ["wild", "wild draw four"]
    for colour in colours:
        for value in values:
            card_val = "{} {}".format(colour, value)
            deck.append(card_val)
            if value != 0:
                deck.append(card_val)

    for i in range(4):
        deck.append(wilds[0])
        deck.append(wilds[1])
    return deck


"""
shuffles a list of items passed into it
parameters: deck ->
return values: deck -> list
"""


def shuffle_deck(deck):
    for card_pos in range(len(deck)):
        rand_pos = random.randint(0, 107)
        deck[card_pos], deck[rand_pos] = deck[rand_pos], deck[card_pos]
    return deck


"""
draws a card functon that draws specified number of cards off the top of the deck
parameter: num_cards -> integer
return: cards_drawn ->
"""


def draw_cards(num_cards):
    cards_drawn = []
    for x in range(num_cards):
        cards_drawn.append(uno_deck.pop(0))
    return cards_drawn


"""
print formatted list of player's hand
parameter: player -> int , player_hand -> list
return: None
"""


def show_hand(player, player_hand):
    print("player{}'s Turn".format(player+1))
    print("your hand")
    print("-" * 30)
    y = 1
    for card in player_hand:
        print("{}) {}".format(y, card))
        y += 1
    print("")


"""
check whether a player is able to player a card, or not
parameter: color -> sting, value -> string,  player_hand -> list
return: boolean
"""


def can_play(colour, value, player_hand):
    for card in player_hand:
        if "wild" in card:
            return True
        elif colour in card or value in card:
            return True
    return False


uno_deck = build_deck()
uno_deck = shuffle_deck(uno_deck)
uno_deck = shuffle_deck(uno_deck)
discards = []
print(uno_deck)
players = []
colours = ["red", "green", "yellow", "blue"]
num_players = int(input("how many players: "))
while num_players < 2 or num_players > 4:
    num_players = int(input("Error please enter a number in the range of (2 - 4) \nhow many players: "))
for player in range(num_players):
    players.append(draw_cards(5))

player_turn = 0
play_direction = 1
playing = True
discards.append(uno_deck.pop(0))
split_card = discards[0].split(" ", 1)
current_color = split_card[0]
if current_color != "wild":
    card_val = split_card[1]
else:
    card_val = "Any"
while playing:
    show_hand(player_turn, players[player_turn])
    print("card on top of discard pile: {}".format(discards[-1]))
    if can_play(current_color, card_val, players[player_turn]):
        card_chosen = int(input("which card do you want to play: "))
        while not can_play(current_color, card_val, [players[player_turn][card_chosen - 1]]):
            card_chosen = int(input("not a valid card. which card do you want to play: "))
            print("you have played: {}".format(players[player_turn][card_chosen-1]))
        discards.append(players[player_turn].pop(card_chosen-1))
    else:
        print("you can not play. you have to draw a card.")
        players[player_turn].extend(draw_cards(1))
    print("")

    # check of special cards
    split_card = discards[0].split(" ", 1)
    current_color = split_card[0]
    if len(split_card) == 1:
        card_val = "Any"
    else:
        card_val = split_card[1]
    if current_color == "wild":
        for x in range(len(colours)):
            print("{}) {}".format(x+1, colours))
        new_colour = int(input("what colour would you like to chose: "))
        while new_colour < 1 or new_colour > 4:
            new_colour = int(input("invalid option +. what colour would you like to choose"))
        current_color = colours[new_colour-1]
    if card_val == "reverse":
        play_direction = play_direction * -1
    elif card_val == "skip":
        player_turn += play_direction
    elif card_val == "draw two":
        players[player_turn].extend(draw_cards(2))
    elif card_val == "draw four":
        players[player_turn].extend(draw_cards(4))
    player_turn += play_direction
    if player_turn == num_players:
        player_turn = 0
    elif player_turn < 0:
        player_turn = num_players - 1
