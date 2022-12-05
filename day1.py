from typing import List

class Elf:
    def __init__(self):
        self.foods: List[int] = []
    
    def total_calories(self) -> int:
        return sum(self.foods)

def read_day_one_input() -> List[Elf]:
    with open('day1.txt') as f:
        elves = []
        elf = Elf()
        for line in f.readlines():
            if line != '\n':
                elf.foods.append(int(line))
            else:
                elves.append(elf)
                elf = Elf()
        return elves

def find_elf_with_most_calories(elves: List[Elf]) -> Elf:
    return max(elves, key=lambda elf: elf.total_calories())

def day_one_part_one() -> int:
    elves = read_day_one_input()
    return find_elf_with_most_calories(elves).total_calories()

def day_one_part_two() -> int:
    elves = read_day_one_input()
    return sum([elf.total_calories() for elf in sorted(elves, key=lambda elf: elf.total_calories(), reverse=True)[:3]]) # 🤮

if __name__ == '__main__':
    print(day_one_part_two())