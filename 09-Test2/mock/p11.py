# def order_cards(card_string):
#     ordered_cards = ""

#     for card in card_string:
#         if card.isalpha() and card.isupper():
#             ordered_cards += card

#     return ''.join(sorted(ordered_cards, key=lambda x: "23456789TJQKA".index(x)))


def order_cards(card_string):
    return ''.join(sorted(card_string, key=lambda card: "AKQJT98765432".index(card)))

result = order_cards("T9JK3")
print(result)