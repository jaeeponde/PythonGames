suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
playing = True

class Card:
  #should be able to understand suit and rank of the card
  def __init__(self,suit,rank):
    self.suit = suit
    self.rank = rank
    self.value = values[rank]

  def __str__ (self):
    return self.rank + " of " + self.suit

class Deck:
   #hold all 52 card objects
   #shuffle cards
   #pop used cards

   def __init__(self):
     self.testdeck = []

     for suit in suits:
       for rank in ranks:
         created_card = Card(suit,rank)
         self.testdeck.append(created_card)

   def shuffle(self):

     from random import shuffle
     shuffle(self.testdeck)

   def deal_one(self):
     single_card = self.testdeck.pop()
     return single_card

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces

    def add_card(self,card,aces=0):

      self.cards.append(card)
      self.value += values[card.rank]
      if card.rank == "Ace":
        self.aces +=1
        pass

    def adjust_for_ace(self):
      while self.value >21 and self.aces>0:
        self.value -=10
        self.aces -=1

class Chips:

    def __init__(self):
        self.total = 1000  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += (self.bet + self.bet)

    def lose_bet(self):
        self.total -= self.bet

def take_bet(Chips):

  while True :
    try:
      Chips.bet = int(input("Please place your bet :  "))
    except :
      print ("Please bet an integer")
    else:
        if Chips.bet > Chips.total:
           print("Sorry, your bet can't exceed",Chips.total)
        else:
            break

def hit(Deck,Hand):

  Hand.add_card(Deck.deal_one())
  Hand.adjust_for_ace

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop

    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")

        if x[0].lower() == 'h':
            hit(deck,hand)
            show_some(player_hand,dealer_hand) # hit() function defined above

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again.")
            continue
        break

def show_some(player,dealer):
  print("\nDealer's Hand :")
  sleep(1)
  print("First Card : HIDDEN \n")
  sleep(1)
  print(dealer.cards[1])
  print("\nPlayer's Hand :")
  sleep(1)
  for item in player.cards:
    print(item)
    sleep(1)
    print("\n")

  pass

from time import sleep

def show_all(player,dealer):

  print("\nPlayer's Hand :")
  sleep(1)
  for item in player.cards:
    print(item)
    sleep(1)
    print("\n")
  print(f"Value of players hand is : {player.value}")
  sleep(1)
  

  print("\nDealers's Hand :")
  sleep(1)
  for item in dealer.cards:
    print(item)
    sleep(1)
    print("\n")
  print(f"Value of dealers hand is : {dealer.value}")

def player_busts(player,dealer,Chips):
  print ("PLAYER BUSTS!")
  Chips.lose_bet()
  pass

def player_wins(player,dealer,Chips):
  print ("PLAYER WINS!")
  Chips.win_bet()
  pass

def dealer_busts(player,dealer,Chips):
  print ("DEALER BUSTS! PLAYER WINS!")
  Chips.win_bet()
  pass

def dealer_wins(player,dealer,Chips):
  print ("DEALER WINS!")
  Chips.lose_bet()
  pass

def push(player,dealer,Chips):
  print ("Dealer and Player TIE. PUSH.")
  pass

playerchips = Chips()
while True:
    # Print an opening statement
    print("Welcome to BlackJack!")


    # Create & shuffle the deck, deal two cards to each player
    mydeck = Deck()
    mydeck.shuffle()
    player_hand = Hand()
    dealer_hand=Hand()

    player_hand.add_card(mydeck.deal_one())
    player_hand.add_card(mydeck.deal_one())
    dealer_hand.add_card(mydeck.deal_one())
    dealer_hand.add_card(mydeck.deal_one())

    # Set up the Player's chips



    # Prompt the Player for their bet
    take_bet(playerchips)



    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)




    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(mydeck,player_hand)


        if player_hand.value > 21 :
          player_busts(player_hand,dealer_hand,playerchips)
          playing = False


    # If Player hasn't busted, play dealer's hand until Dealer reaches 17
    if player_hand.value <= 21 :
       while dealer_hand.value  <= 17:
          hit(mydeck,dealer_hand)



    # Show all cards
    show_all(player_hand,dealer_hand)


    # Run different winning scenarios
    if dealer_hand.value>21:
      dealer_busts(player_hand,dealer_hand,playerchips)

    elif player_hand.value<=21 and player_hand.value > dealer_hand.value:
      player_wins(player_hand,dealer_hand,playerchips)

    elif player_hand.value < dealer_hand.value:
      dealer_wins(player_hand,dealer_hand,playerchips)

    elif player_hand.value == dealer_hand.value:
      push(player_hand,dealer_hand,playerchips)

    # Ask to play again
    answer = input("Would you ike to play again? Y or N :  ")
    if answer == "Y":
      playing = True
      pass
    else :
      print("Thank you for playing")
      break
