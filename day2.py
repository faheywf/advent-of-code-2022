from typing import List

class Round:
    def __init__(self, opponents_play: str, your_play: str) -> None:
        self.opponents_play = opponents_play
        self.your_play = your_play

    def your_move_score(self) -> int:
        if self.your_play == 'X': # rock
            return 1
        if self.your_play == 'Y': # paper
            return 2
        else:                     # scissors
            return 3

    def result(self) -> int:
        if self.your_play == 'X': # rock
            if self.opponents_play == 'A': # vs rock
                return 3
            elif self.opponents_play == 'B': # vs paper
                return 0
            else: # vs scissors
                return 6
        elif self.your_play == 'Y': # paper
            if self.opponents_play == 'A': # vs rock
                return 6
            elif self.opponents_play == 'B': # vs paper
                return 3
            else: # vs scissors
                return 0
        else: # scissors
            if self.opponents_play == 'A': # vs rock
                return 0
            elif self.opponents_play == 'B': # vs paper
                return 6
            else: # vs scissors
                return 3

    def choose_move(self) -> None:
        if self.your_play == 'X': # need to lose
            if self.opponents_play == 'A': # vs rock
                self.your_play = 'Z'
            elif self.opponents_play == 'B': # vs paper
                self.your_play = 'X'
            else: # vs scissors
                self.your_play = 'Y'
        elif self.your_play == 'Y': # need to draw:
            if self.opponents_play == 'A': # vs rock
                self.your_play = 'X'
            elif self.opponents_play == 'B': # vs paper
                self.your_play = 'Y'
            else: # vs scissors
                self.your_play = 'Z'
        else: # need to win
            if self.opponents_play == 'A': # vs rock
                self.your_play = 'Y'
            elif self.opponents_play == 'B': # vs paper
                self.your_play = 'Z'
            else: # vs scissors
                self.your_play = 'X'


    def score(self) -> int:
        return self.result() + self.your_move_score()

def read_day_two_input() -> List[Round]:
    with open('inputs/day2.txt') as f:
        rounds = []
        for line in f.readlines():
            line = line.split()
            rounds.append(Round(line[0], line[1]))
        return rounds

def day_two_part_one() -> int:
    rounds = read_day_two_input()
    return sum([round.score() for round in rounds])

def day_two_part_two() -> int:
    rounds = read_day_two_input()
    for round in rounds:
        round.choose_move()
    return sum([round.score() for round in rounds])

if __name__ == '__main__':
    print(day_two_part_two())