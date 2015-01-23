class User:
    """User bets, hand actions, and chip count.

    Responsibilities:
    * Gives initial chip count:
        500
    * Chooses game settings:
        Change bet?
        Deal Hand

    Collaborators:
    * Chooses possible actions passed from Hand
    * Chooses how much to bet.
    * Game_manager class sends user double bet if wins. """


    def __init__(self):
        self.chip_count = 500

    def bet_chips(self, bet):
        self.chip_count = self.chip_count - bet
        return self.chip_count

    def user_pregame_input(self):
        user_request = input("Type 'bet' if you'd like to place a bet and"
                             " start a new hand.\n")

        if user_request in ['quit', 'help', 'chips']:
            return user_request
        elif user_request == 'bet':
            try:
                bet_amount = int(input("How much would you like to wager?\n"))
                if bet_amount <= self.chip_count:
                    return bet_amount
                else:
                    print("You don't have that many chips!")
                    return self.user_pregame_input()
                return bet_amount
            except:
                print("That is not a number.")
                return self.user_pregame_input()
        else:
            print('That is not a valid response.')
            return self.user_pregame_input()

    def user_in_game_input(self):
        user_request = input("What would you like to do? You can either:\n"
                             "Type 'hit' to receive another card.\n"
                             "Type 'stay' to hold your position.\n"
                             "Type 'double' to double down your bet\n")

        if user_request not in ['hit', 'stay', 'double', 'help','quit']:
            print("That is not a valid response.")
            return self.user_in_game_input()
        return user_request
