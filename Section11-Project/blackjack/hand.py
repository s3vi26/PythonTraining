from card import values

class Hand:
  def __init__(self):
    self.cards = []  # start with an empty list as we did in the Deck class
    self.value = 0   # start with zero value
    self.aces = 0    # add an attribute to keep track of aces

  def __str__(self):
    return f"You have {len(self.cards)} cards in your hand"
  
  def add_card(self,card):
    self.cards.append(card)
    self.value += values[card.rank]
    if card.rank == 'Ace':
      self.aces += 1
  
  def adjust_for_ace(self):
    while self.value > 21 and self.aces:
      self.value -= 10