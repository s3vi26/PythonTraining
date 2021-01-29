import random
from card import Card, ranks, suits, values

class Deck:
  def __init__(self):
      
    self.deck = []

    for suit in suits:
      for rank in ranks:

        created_card = Card(suit,rank)
        print(created_card)

        self.deck.append(created_card)

  def __str__(self):
    return f'{len(self.deck)} cards in Deck'

  def shuffle(self):
    random.shuffle(self.deck)

  def deal(self):
    dealt = self.deck.pop(0)
    return dealt

