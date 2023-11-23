import random

class Card:
  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank

  def __str__(self):
    return f"{self.rank['rank']}  of {self.suit}"
    
class Deck:

  def __init__(self):
    self.cards = []
    suits = ["hearts", "clubs", "hearts", "diamonds"]
    suit = suits[2]
    ranks = [{
        "rank": "A",
        "value": 11
    }, {
        "rank": "2",
        "value": 2
    }, {
        "rank": "3",
        "value": 3
    }, {
        "rank": "4",
        "value": 4
    }, {
        "rank": "5",
        "value": 5
    }, {
        "rank": "6",
        "value": 6
    }, {
        "rank": "7",
        "value": 7
    }, {
        "rank": "8",
        "value": 8
    }, {
        "rank": "9",
        "value": 9
    }, {
        "rank": "10",
        "value": 10
    }, {
        "rank": "J",
        "value": 10
    }, {
        "rank": "Q",
        "value": 10
    }, {
        "rank": "K",
        "value": 1
    }]

    value = 10
    for suit in suits:
      for rank in ranks:
        #self.cards.append([suit, rank])
        self.cards.append(Card(suit,rank))

  def shuffle(self):
    if len(self.cards) > 1:
      random.shuffle(self.cards)

  def deal(self, number):
    cards_dealt = []
    for X in range(number):
      if len(self.cards) > 0:
        card = self.cards.pop()
        cards_dealt.append(card)

    return cards_dealt

  #shuffle()
  """
  cards_dealt = deal(2)
  card = cards_dealt[0]
  rank = card[1]
  
  if rank == "A":
    value = 11
  elif rank == "J" or rank == "K" or rank == "Q":
    value = 10
  else:
    value = rank
    
  
  rank_dict = {"rank": rank, "value": value}
  
  print(rank_dict["rank"], rank_dict["value"])
  """


card1 = Card("hearts", {"rank": "j", "value": 10})
#print(card1)

class Hand:
  def __init__(self, dealer=False):
    self.cards = []
    self.value = 0
    self.dealer = dealer
  
  def add_card(self, card_list):
    self.cards.extend(card_list)

  def calculate_value(self):
    self.value = 0
    has_ace = False

    for card in self.cards:
      card_value = card.rank["value"]
      self.value += card_value
      if card.rank["rank"] == "A":
        has_ace = True

    if has_ace and self.value > 21:
      self.value -= 10
      
  def get_value(self):
    self.calculate_value()
    return self.value

  def is_blackjack(self):
    return self.get_value() == 21

  def display(self, show_all_dealer_cards=False):
    print(f''' {"Dealer's" if self.dealer else "Your"} hand: ''')
    for index, card in enumerate(self.cards):
      if index == 0 and self.dealer:
        print("hidden")
      else:
        print(card)

    if not self.dealer \
    and not show_all_dealer_cards and not self.is_blackjack():
      print("Value:", self.get_value())

#deck = Deck()
#deck.shuffle()

#hand = Hand()
#hand.add_card(deck.deal(2))
#hand.display()

class Game:
  def play(self):
    game_number = 0
    games_to_play = 0

    while games_to_play <= 0:
      try:
        games_to_play = int(input("How many games do you want to play?"))
      except:
        print("You must enter a number.")

    while game_number < games_to_play:
      game_number += 1
      print(f"Game {game_number + 1}")
      
      deck = Deck()
      deck.shuffle()
      player_hand = Hand()
      dealer_hand = Hand(dealer=True)

      for i in range(2):
        player_hand.add_card(deck.deal(1))
        dealer_hand.add_card(deck.deal(1))

      print("*" * 30)
      print(f"Game {game_number} of {games_to_play}")
      print("*" * 30)

      player_hand.display()
      dealer_hand.display()

      if self.check_winner(player_hand, dealer_hand):
        continue

      choice = ""
      while player_hand.get_value() < 21 and choice not in ["s", "stand"]:
        choice = input(f"Do you want to hit or stand? ").lower()
        print()
        while choice not in [ "h", "hit", "s", "stand" ]:
          choice = input("Pls enter 'Hit' os 'Stand' (or H/S) ").lower()
          print()
        if choice in ["hit", "h"]:
          player_hand.add_card(deck.deal(1))
          player_hand.display()

      if self.check_winner(player_hand, dealer_hand):
        continue

      player_hand_value = player_hand.get_value()
      dealer_hand_value = dealer_hand.get_value()  

      while dealer_hand_value < 17:
        dealer_hand.add_card(deck.deal(1))
        dealer_hand_value = dealer_hand.get_value()

      dealer_hand.display(show_all_dealer_cards=True)

      if self.check_winner(player_hand, dealer_hand):
        continue

      print("Final Results")
      print("Your hand:", player_hand_value)
      print("Dealer's hand:", dealer_hand_value)

      self.check_winner(player_hand, dealer_hand, True)

    print("\nThank for playing!")

  def check_winner(self, player_hand, dealer_hand, game_over = False):
    if not game_over:
      if player_hand.get_value() > 21:
        print("You busted! Dealer wins!")
        return True
      elif dealer_hand.get_value() > 21:
        print("Dealer busted! You wins!")
        return True
      elif dealer_hand.is_blackjack() and not player_hand.is_blackjack():
        print("Both players are blackjack! Tie!")
        return True
      elif dealer_hand.is_blackjack():
        print("Dealer has blackjack! You lose!")
        return True
      elif player_hand.is_blackjack():
        print("You have blackjack! You Win!")
        return True
      else:
        if player_hand.get_value() > dealer_hand.get_value():
          print("You win!")
        elif dealer_hand.get_value() == player_hand.get_value():
          print("Tie!")
        else:
          print("Dealer wins")
          return True
      return False


g = Game()
g.play()
