"""
--s (Spades) Пики
--h (Hearts) Черви
--d (Diamonds) Бубны
--c (Clovers) Трефы
"""

from random import randrange

from matplotlib.pyplot import table

def create_desk() -> list:
    suits = ['s', 'h', 'd', 'c']
    values =['2','3','4','5','6','7','8', '9', 'T','Q', 'K', 'A']
    deck = []
    for suit in suits:
        for value in values:
            deck.append(f'{value}{suit}')
    return deck


def shuffle_deck(deck:list) -> list:
    new_deck = deck.copy()
    for _ in range(0, len(new_deck)):
        random_index = randrange(0, len(new_deck))
        new_deck[_], new_deck[random_index] = new_deck[random_index], new_deck[_]
    return new_deck


def deal(players:int, number_cards_of_players:int, deck:list) -> list[list]:
    if players * number_cards_of_players > len(deck):
        print('Игра невозможна не хвататет карт в колоде')
        return None
    table = []
    for player in range(0,players):
        table.append([])
    for _ in range(0, number_cards_of_players):
        for player in range(0,players):
            table[player].append(deck.pop())
    return table


def main():
    init_deck = create_desk()
    print(f'Открываем новую колоду: {init_deck}')
    deck = shuffle_deck(init_deck)
    print(f'Тасуем колоду: {deck}')
    players = 7
    number_cards_of_players = 5
    table_deal = deal(players, number_cards_of_players, deck)
    for i in range(players):
        print(f'Карты игрока {i + 1}: {table_deal[i]}')
    print(f'Колода после раздачи: {deck}')

if __name__ == '__main__':
    main()