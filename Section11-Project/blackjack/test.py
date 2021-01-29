from functions import take_bet, hit_or_stand
from chips import Chips
from deck import Deck
from hand import Hand

the_deck = Deck()
player_hand = Hand()
player_hand.add_card(the_deck.deal())
player_hand.add_card(the_deck.deal())

hit_or_stand(the_deck, player_hand)

# player_chips = Chips()
# take_bet(player_chips)