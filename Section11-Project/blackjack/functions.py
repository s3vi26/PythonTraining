def take_bet(Chips):
  while True:
    try:
      bet = int(input("How much do you want to bet? (1-100): "))
    except ValueError:  
      print('That is not a number')
      continue
    else:
      if bet > Chips.total:
        print("You dont have enough to place that bet")
        continue
      else:
        Chips.total -= bet
        print(f"You have bet {bet} chips")
        break

def hit(Deck,Hand):
  Hand.add_card(Deck.deck.pop(0))
  Hand.adjust_for_ace()

def hit_or_stand(Deck,Hand):
  global playing # to control an upcoming while loop

  while True:
    action = input("Would you like to Hit or Stand?")
    if action == "Hit" or action == "hit":
      hit(Deck,Hand)
      continue
    elif action == "Stand" or action == "stand":
      playing = False
      break
    else:
      print("Please type Hit or Stand")
      continue

def show_some(player,dealer):
  print("\nDealer's Hand:")
  print(" <card hidden>")
  print('',dealer.cards[1])  
  print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
  print("\nDealer's Hand:", *dealer.cards, sep='\n ')
  print("Dealer's Hand =",dealer.value)
  print("\nPlayer's Hand:", *player.cards, sep='\n ')
  print("Player's Hand =",player.value)


def player_busts(player,dealer,chips):
  print("Player busts!")
  chips.lose_bet()

def player_wins(player,dealer,chips):
  print("Player wins!")
  chips.win_bet()

def dealer_busts(player,dealer,chips):
  print("Dealer busts!")
  chips.win_bet()
    
def dealer_wins(player,dealer,chips):
  print("Dealer wins!")
  chips.lose_bet()
    
def push(player,dealer):
  print("Dealer and Player tie! It's a push.")