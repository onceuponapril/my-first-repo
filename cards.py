import random
import unittest

# SI 507 Winter 2018
# Homework 2 - Code

##COMMENT YOUR CODE WITH:
# Section Day/Time:
# People you worked with:

######### DO NOT CHANGE PROVIDED CODE #########
### Below is the same cards.py code you saw in lecture.
### Scroll down for assignment instructions.
#########

class Card(object):
	suit_names =  ["Diamonds","Clubs","Hearts","Spades"]
	rank_levels = [1,2,3,4,5,6,7,8,9,10,11,12,13]
	faces = {1:"Ace",11:"Jack",12:"Queen",13:"King"}

	def __init__(self, suit=0,rank=2):
		self.suit = self.suit_names[suit]
		if rank in self.faces: # self.rank handles printed representation
			self.rank = self.faces[rank]
		else:
			self.rank = rank
		self.rank_num = rank # To handle winning comparison

	def __str__(self):
		return "{} of {}".format(self.rank,self.suit)

class Deck(object):
	def __init__(self): # Don't need any input to create a deck of cards
		# This working depends on Card class existing above
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card) # appends in a sorted order

	def __str__(self):
		total = []
		for card in self.cards:
			total.append(card.__str__())
		# shows up in whatever order the cards are in
		return "\n".join(total) # returns a multi-line string listing each card

	def pop_card(self, i=-1):
		# removes and returns a card from the Deck
		# default is the last card in the Deck
		return self.cards.pop(i) # this card is no longer in the deck -- taken off

	def shuffle(self):
		random.shuffle(self.cards)

	def replace_card(self, card):
		card_strs = [] # forming an empty list
		for c in self.cards: # each card in self.cards (the initial list)
			card_strs.append(c.__str__()) # appends the string that represents that card to the empty list
		if card.__str__() not in card_strs: # if the string representing this card is not in the list already
			self.cards.append(card) # append it to the list

	def sort_cards(self):
		# Basically, remake the deck in a sorted way
		# This is assuming you cannot have more than the normal 52 cars in a deck
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card)


def play_war_game(testing=False):
	# Call this with testing = True and it won't print out all the game stuff -- makes it hard to see test results
	player1 = Deck()
	player2 = Deck()

	p1_score = 0
	p2_score = 0

	player1.shuffle()
	player2.shuffle()
	if not testing:
		print("\n*** BEGIN THE GAME ***\n")
	for i in range(52):
		p1_card = player1.pop_card()
		p2_card = player2.pop_card()
		print('p1 rank_num=', p1_card.rank_num, 'p1 rank_num=', p2_card.rank_num)
		if not testing:
			print("Player 1 plays", p1_card,"& Player 2 plays", p2_card)

		if p1_card.rank_num > p2_card.rank_num:

			if not testing:
				print("Player 1 wins a point!")
			p1_score += 1
		elif p1_card.rank_num < p2_card.rank_num:
			if not testing:
				print("Player 2 wins a point!")
			p2_score += 1
		else:
			if not testing:
				print("Tie. Next turn.")

	if p1_score > p2_score:
		return "Player1", p1_score, p2_score
	elif p2_score > p1_score:
		return "Player2", p1_score, p2_score
	else:
		return "Tie", p1_score, p2_score

if __name__ == "__main__":
	result = play_war_game()
	print("""\n\n******\nTOTAL SCORES:\nPlayer 1: {}\nPlayer 2: {}\n\n""".format(result[1],result[2]))
	if result[0] != "Tie":
		print(result[0], "wins")
	else:
		print("TIE!")


######### DO NOT CHANGE CODE ABOVE THIS LINE #########

## You can write any additional debugging/trying stuff out code here...
## OK to add debugging print statements, but do NOT change functionality of existing code.
## Also OK to add comments!

#########







##**##**##**##@##**##**##**## # DO NOT CHANGE OR DELETE THIS COMMENT LINE -- we use it for grading your file
###############################################

### Write unit tests below this line for the cards code above.

class TestCard(unittest.TestCase):


	# this is a "test"
	def test_create(self):
		card = Card()
		self.assertEqual(card.suit, "Diamonds")
		self.assertEqual(card.rank, 3)
		self.assertEqual(Card(0,12).rank,'Queen')
		self.assertEqual(Card(0,1).rank,'Ace')
		self.assertEqual(Card(0,3).rank,3)
		self.assertEqual(Card(1).suit,'Clubs')
		self.assertEqual(Card(2).suit,'Hearts')
		self.assertEqual(card.suit_names,["Diamonds","Clubs","Hearts","Spades"])
	def test_str(self):
	    self.assertEqual(Card(2,7).__str__(),'7 of Hearts')
	    self.assertEqual(Card(3,13).__str__(),'King of Spades')
	def test_deck(self):
	    deck=Deck()
	    self.assertEqual(len(deck.cards),52)
	    a=deck.pop_card()
	    self.assertEqual(type(a),type(Card()))
	    self.assertEqual(len(deck.cards),51)
	
	def test_game(self):
	    game=play_war_game()
	    self.assertIs(type(game),tuple)
	    self.assertEqual(len(game),3)
	    self.assertIs(type(game[0]),str)        

#Test if invoke Deck's methods of shuffle, the new cards will change its order.	
	def test_shuffle(self):
	    deck=Deck()
	    deck.shuffle()
	    self.assertNotEqual(deck.cards[0],Deck().cards[0])

# Test if invoke sort_cards, the deck still contains 52 cards.
	def test_sort(self):
	    deck=Deck()
	    deck.sort_cards()
	    self.assertEqual(len(deck.cards),52)
	    

class Hand():
      def __init__(self):
          self.cards=[Card(0,1),Card(1,1),Card(2,2)]
      
      def __str__(self):
          lis=[]
          for i in self.cards:
              lis.append(i.__str__())
          return lis
          
      
      
      def add_card(self,newcard):
          newstr=newcard.__str__() 
          tlst=self.__str__()
          if newstr not in tlst:
                       self.cards.append(newcard)
    
      def remove_card(self, rmcard):
          for i in self.cards:
              if i.suit==rmcard.suit and i.rank==rmcard.rank:
                                         self.cards.remove(i)
                                         return i
 
              else:
                   return None
      
      def draw(self,deck,num=-1):
          cd=deck.pop_card(num)
          self.drawc=cd
          self.cards.append(cd)

 


# Test that a hand is initialized properly.
# Test that add_card( ) and remove_card( ) behave as specified (you can write one test for this, called testAddAndRemove.
# Test that draw( ) works as specified. Be sure to test side effects as well.

class Testhand(unittest.TestCase):  
      def test_init(self):
          self.assertEqual(len(Hand().cards),3)
      
      def testAddAndRemove(self):
          thand=Hand()
          thand.add_card(Card(1,1))
          self.assertEqual(len(thand.cards),len(Hand().cards))
          thand.add_card(Card(1,2))
          self.assertIn(Card(1,2).__str__(),thand.__str__())
          self.assertEqual(thand.remove_card(Card(3,2)),None)
          self.assertEqual(thand.remove_card(Card(0,1)).rank,'Ace')

      
      def testdraw(self):
          ddeck=Deck()
          hhand=Hand()
          hhand.draw(ddeck,1)
          self.assertIn(hhand.drawc.__str__(),hhand.__str__())
          self.assertGreater(len(Deck().cards),len(ddeck.cards))
          
          
          
          
             
# #############
## The following is a line to run all of the tests you include:
if __name__ == "__main__":
	unittest.main(verbosity=2)
## verbosity 2 to see detail about the tests the code fails/passes/etc.
