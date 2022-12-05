from typing import List

class Assignment:
    def __init__(self, start: int, finish: int):
        self.start = start
        self.finish = finish

class Pair:
    def __init__(self, first: Assignment, second: Assignment):
        self.first = first
        self.second = second

    def overlaps(self) -> bool:
        return self.first.start <= self.second.start and self.first.finish >= self.second.finish or self.second.start <= self.first.start and self.second.finish >= self.first.finish

    def any_overlap(self) -> bool:
        return self.second.start <= self.first.start <= self.second.finish or self.second.start <= self.first.finish <= self.second.finish or self.first.start <= self.second.start <= self.first.finish or self.first.start <= self.second.finish <= self.first.finish

def read_day_four_input() -> List[Pair]:
    with open('day4.txt') as f:
        pairs = []
        for line in f.readlines():
            first, second = line.split(',')
            start, finish = first.split('-')
            assignment = Assignment(int(start), int(finish))

            start, finish = second.split('-')
            assignment_2 = Assignment(int(start), int(finish))
            
            pairs.append(Pair(assignment, assignment_2))
    
    return pairs

def day_four_part_one() -> int:
    pairs = read_day_four_input()
    return sum([pair.overlaps() for pair in pairs])

def day_four_part_two() -> int:
    pairs = read_day_four_input()
    return sum([pair.any_overlap() for pair in pairs])

if __name__ == '__main__':
    print(day_four_part_two())