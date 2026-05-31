deck_cards = input().split()
number_shuffles = int(input())

for current_shuffle in range(number_shuffles):
    middle_deck = len(deck_cards)//2
    left_deck = deck_cards[:middle_deck]
    right_deck = deck_cards[middle_deck:]

    shuffle_desk = []

    for index in range(len(left_deck)):
        shuffle_desk.append(left_deck[index])
        shuffle_desk.append(right_deck[index])
    deck_cards = shuffle_desk.copy()

print(deck_cards)