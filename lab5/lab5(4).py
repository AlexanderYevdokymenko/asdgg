import random

class Deck:
    def __init__(self, cards):
        self.cards = cards
 
    def deck_info(self):
        for card in self.cards:
            print(card)
 
    def mix_card(self):
        random.shuffle(self.cards)
 
    def one_card(self):
        if not self.cards:
            return 'no card'
        return random.choice(self.cards)
    
    def six_card(self):
        return [self.one_card() for _ in range(6)]

class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def info_rank(self):
         return self.number
 
    def __str__(self):
        return f'{self.number} {self.suit}'    

number = ['6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король', 'Туз']
suit = ['Чірва', 'Буба', 'Піка', 'Хреста']
cards = [Card(s,r) for s in suit for r in number]

deck = Deck(cards)
print('колода')
deck.deck_info()
deck.mix_card()
print()
print('перемешанная колода')
deck.deck_info()
print()
print('выдача одной карты')
print(deck.one_card())
print()
print('выдача 6 карт')
for card in deck.six_card():
    print(card)