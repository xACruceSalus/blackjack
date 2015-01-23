from blackjack.card import Card


class PlayerHand:
    """current card count.

    Responsibilites:
        *sum cards in hand
        *holds the possibilites of action
            hit
            stay
            double down
            split
            if >= 22 == bust

    Collaboraters:
        *Recieves card from deck
        *Gives actionable choices to player"""

    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return "{}".format(self.cards)

    def player_card_count(self, cards):
        count = 0
        for card in cards:
            if card.rank in (2, 3, 4, 5, 6, 7, 8, 9, 10):
                count += card.rank
            elif card.rank in ('King', 'Queen', 'Jack'):
                count += 10
        for left_card in cards:
            if left_card.rank == 'Ace':
                if count >= 11:
                    count += 1
                else:
                    count += 11
        return count

    def player_actions(self, count):
        if count >= 22:
            return 'bust'
        elif count == 21:
            return '21'
        else:
            return 'choice'
        # double down
        # split
