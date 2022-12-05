from typing import List, Tuple

class Instruction:
    def __init__(self, instruction: str):
        instruction = instruction.split(' ')
        self.quantity = int(instruction[1])
        self.from_stack = int(instruction[3])
        self.to_stack = int(instruction[5])

    def __str__(self) -> str:
        return f"Move {self.quantity} from stack {self.from_stack} to stack {self.to_stack}"


class Ship:
    def __init__(self, num_stacks: int, crate_mover_9001: bool = False):
        self.stacks: List[List[str]] = [[] for _ in range(num_stacks)]
        self.crate_mover_9001 = crate_mover_9001

    def add_cargo(self, cargo: str, stack: int) -> None:
        self.stacks[stack].append(cargo)

    def process_instruction(self, instruction: Instruction) -> None:
        if not self.crate_mover_9001:
            for _ in range(instruction.quantity):
                self.stacks[instruction.to_stack-1].append(self.stacks[instruction.from_stack-1].pop())
        else:
            self.stacks[instruction.to_stack-1].extend(self.stacks[instruction.from_stack-1][-instruction.quantity:])
            self.stacks[instruction.from_stack-1] = self.stacks[instruction.from_stack-1][:-instruction.quantity]
            

    def top_of_stacks(self) -> str:
        return ''.join([stack[-1] if len(stack) > 0 else '' for stack in self.stacks])

    def __str__(self) -> str:
        return '\n'.join([str(stack) for stack in self.stacks])


def read_day_five_input(part_two: bool = False) -> Tuple[Ship, List[Instruction]]:
    with open('inputs/day5.txt') as f:
        lines = [line.replace('\n', '') for line in f.readlines()]
        separator_idx = None
        for idx, line in enumerate(lines):
            if line == '':
                separator_idx = idx
                break

        stack_info = lines[:separator_idx]
        num_stacks = len(stack_info[-1].split())
        ship = Ship(num_stacks, part_two)

        for line in reversed(stack_info[:-1]):
            for start_idx in range(0, len(line), 4):
                cargo = line[start_idx+1]
                stack = start_idx // 4
                if cargo != ' ':
                    ship.add_cargo(cargo, stack)

        instructions = [Instruction(line) for line in lines[separator_idx+1:]]

        return ship, instructions

def day_five_part_one() -> str:
    ship, instructions = read_day_five_input()

    for instruction in instructions:
        ship.process_instruction(instruction)

    return ship.top_of_stacks()

def day_five_part_two() -> str:
    ship, instructions = read_day_five_input(True)

    for instruction in instructions:
        ship.process_instruction(instruction)

    return ship.top_of_stacks()

if __name__ == '__main__':
    print(day_five_part_two())
    