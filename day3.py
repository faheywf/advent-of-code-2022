from typing import Dict, List

def priority_map() -> Dict[str, int]:
    letters = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" # space at the beginning is to make the index line up with the priority
    priorities = { letter: priority for priority, letter in enumerate(letters) }
    return priorities

def read_day_three_input() -> List[str]:
    with open('inputs/day3.txt') as f:
        return [line.replace('\n', '') for line in f.readlines()]

def day_three_part_one() -> int:
    priorities = priority_map()
    rucksacks = read_day_three_input()

    duplicates: List[str] = []

    for rucksack in rucksacks:
        for letter in rucksack[:len(rucksack)//2]:
            if letter in rucksack[len(rucksack)//2:]:
                duplicates.append(letter)
                break
    
    return sum([priorities[letter] for letter in duplicates])

def day_three_part_two() -> int:
    priorities = priority_map()
    rucksacks = read_day_three_input()
    badges: List[str] = []

    for i in range(0, len(rucksacks), 3):
        r0 = set(rucksacks[i])
        r1 = set(rucksacks[i+1])
        r2 = set(rucksacks[i+2])

        for letter in r0:
            if letter in r1 and letter in r2:
                badges.append(letter)
                break
    
    return sum([priorities[letter] for letter in badges])


    

if __name__ == '__main__':
    print(day_three_part_two())