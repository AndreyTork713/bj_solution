import random

# Задаем глобальные переменные:
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')  # Масть - Кортеж
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')  # ранг карт - Кортеж
values = {'Two': 2, 'Three': 3, 'Four': 4,
          'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}  # Стоимость карты в зависимости от её ранга

playing = True  # Переменная разрешающая или запрещающая игру


class Card():  # класс репрезентующий одну карту по масти и рангу
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):  # Специальный метод выводящий на экран
        return self.rank + " of " + self.suit


class Deck():  # Класс Колода 
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The deck has: " + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


# Создаём класс Hand который будет отвечать за карты на руках у игрока
class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

    def adjust_for_ace(self):
        pass


test_deck = Deck()
test_deck.shuffle()

# PLAYER
test_player = Hand()

pulled_card = test_deck.deal()
print(pulled_card)
test_player.add_card(pulled_card)
print(test_player.value)