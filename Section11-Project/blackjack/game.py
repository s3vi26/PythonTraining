# game code
from chips import Chips
from deck import Deck
from hand import Hand
from functions import take_bet, hit, hit_or_stand, show_some, show_all, player_busts, player_wins, dealer_busts, dealer_wins, push

playing = True

while True:
  print("Welcome to the game of Blackjack!")

  the_deck = Deck()
  the_deck.shuffle()

  player = Hand()
  dealer = Hand()

  player.add_card(the_deck.deal())
  dealer.add_card(the_deck.deal())
  player.add_card(the_deck.deal())
  dealer.add_card(the_deck.deal())

  player_chips = Chips()
  take_bet(player_chips)
  show_some(player, dealer)
  
  while playing:
    hit_or_stand(the_deck, player)
    show_some(player, dealer)

    if player.value > 21:
      player_busts(player, dealer, player_chips)
      break
  
  if player.value <= 21:
    while dealer.value >= 17:
      hit(the_deck, dealer)
      show_all(player, dealer)
    if dealer.value > 21:
      dealer_busts(player, dealer, player_chips)
    elif dealer.value > player.value:
      dealer_wins(player, dealer, player_chips)
    elif dealer.value < player.value:
      player_wins(player, dealer, player_chips)
    else:
      push(player, dealer)

  new_game = input("Would you like to play another hand? Enter Y or N")
  
  if new_game[0].lower()=='y':
    playing=True
    continue
  else:
    print("Thanks for playing!")
    break




