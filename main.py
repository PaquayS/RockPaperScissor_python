import random


class Game:
    ai = ["rock", "paper", "scissors"]
    win = False
    lose = False
    ties = 0
    wins = 0
    losses = 0
    games_needed = 0

    def __init__(self, amount_of_games):
        self.games_needed = (amount_of_games + 1) / 2

    def game_end(self):
        if self.win or self.lose:
            return
        else:
            self.player_hand()

    def game_won(self):
        if self.wins == self.games_needed:
            self.win = True
            print("YOU WIN!")
            return
        else:
            self.win = False

    def game_lose(self):
        if self.losses == self.games_needed:
            self.lose = True
            print("YOU LOSE!")
            return
        else:
            self.lose = False

    def ai_hand(self):
        _ai_hand = random.choice(self.ai)
        print("The AI played " + _ai_hand)
        return _ai_hand

    def display_score(self):
        return "The current score is " + str(self.wins) + " for you and " + str(self.losses) + " for the AI.\nThere have been a total of " + str(self.ties) + " ties so far.\n"

    def play_round(self, player):
        _ai = self.ai_hand()
        if player == 'rock' or player == 'r':
            if _ai == 'rock':
                self.ties += 1
                print('It\'s a tie')
            elif _ai == 'scissors':
                self.wins += 1
                print('you won')
            elif _ai == 'paper':
                self.losses += 1
                print('you lose')
        elif player == 'scissors' or player == 's':
            if _ai == 'rock':
                self.losses += 1
                print('you lose')
            elif _ai == 'scissors':
                self.ties += 1
                print('It\'s a tie')
            elif _ai == 'paper':
                self.wins += 1
                print('you won')
        elif player == 'paper' or player == 'p':
            if _ai == 'rock':
                self.wins += 1
                print('you won')
            elif _ai == 'scissors':
                self.losses += 1
                print('you lose')
            elif _ai == 'paper':
                self.ties += 1
                print('It\'s a tie')

        print(self.display_score())
        self.game_won()
        self.game_lose()
        self.game_end()

    def player_hand(self):
        hand = input('Do you play hand(h)/scissors(s)/rock(r): \t')
        if hand == 'rock' or hand == 'r' or hand == 'scissors' or hand == 's' or hand == 'paper' or hand == 'p':
            self.play_round(hand)
        else:
            print('Wrong answer, please try again.\n')
            self.player_hand()


def uneven():
    try:
        val = int(input('please give an uneven int in for the Best of games you want to play:\t'))
    except:
        print('not an int, please try again.\n')
        uneven()
    if val % 2 == 0:
        print('The entered number was even, a BO series requires an odd value. fe 1-3-5-7.\nPlease try again.\n')
        uneven()
    else:
        rps_game = Game(val)
        rps_game.player_hand()


def quit_game():
    reply = input("\nDo you want to quit? y/n\n")
    if reply.lower() == 'y':
        quit();
    elif reply.lower() == 'n':
        uneven()
    else:
        print("Please enter y or n.\n")
        quit_game()


print("Welcome to Rock, Paper, Scissors!\n")
uneven()
quit_game()
