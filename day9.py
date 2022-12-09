from typing import List, Set, Tuple

class Point:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def to_tuple(self) -> Tuple[int, int]:
        return (self.x, self.y)

class Rope:
    def __init__(self, num_tails: int = 1):
        self.head = Point()
        self.tails = [Point() for _ in range(num_tails)]
        self.tail_locations: Set[Tuple[int, int]] = set([(0, 0)])

    def process_motion(self, direction: str, distance: int) -> None:
        for step in range(distance):
            self.move_head(direction)
            for idx, tail in enumerate(self.tails):
                if idx == 0:
                    prev = self.head
                else:
                    prev = self.tails[idx-1]
                if abs(prev.x - tail.x) > 1 or abs(prev.y - tail.y) > 1:
                    self.move_tail(prev, idx)
            self.tail_locations.add(self.tails[-1].to_tuple())
            

    def move_head(self, direction: str) -> None:
        if direction == 'U':
            self.head.y += 1
        elif direction == 'D':
            self.head.y -= 1
        elif direction == 'R':
            self.head.x += 1
        else:
            self.head.x -= 1

    def move_tail(self, prev: Point, tail_idx: int) -> None:
        if prev.x > self.tails[tail_idx].x:
            self.tails[tail_idx].x += 1
        if prev.x < self.tails[tail_idx].x:
            self.tails[tail_idx].x -= 1
        if prev.y > self.tails[tail_idx].y:
            self.tails[tail_idx].y += 1
        if prev.y < self.tails[tail_idx].y:
            self.tails[tail_idx].y -= 1

    def __str__(self) -> str:
        all_points = [self.head] + [tail for tail in self.tails]
        min_x = min([point.x for point in all_points])
        min_y = min([point.y for point in all_points])

        normalized = [(point.x + abs(min_x), point.y + abs(min_y)) for point in all_points]
        max_x = max([x for x, y in normalized])
        max_y = max([y for x, y in normalized])

        matrix = [['.' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
        for idx, (x, y) in enumerate(normalized):
            symbol = 'H' if idx == 0 else str(idx)
            matrix[y][x] = symbol
        return '\n'.join([''.join(row) for row in matrix[::-1]])

    def print_tail_locations(self) -> None:
        min_x = min([x for x, y in self.tail_locations])
        min_y = min([y for x, y in self.tail_locations])

        normalized = [(x + abs(min_x), y + abs(min_y)) for x, y in self.tail_locations]
        max_x = max([x for x, y in normalized])
        max_y = max([y for x, y in normalized])

        matrix = [['.' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
        for x, y in normalized:
            matrix[y][x] = '#'

        print('\n'.join([''.join(row) for row in matrix[::-1]]))

def read_day_nine_input() -> List[Tuple[str, int]]:
    with open('inputs/day9.txt') as f:
        lines = [line.replace('\n', '') for line in f.readlines()]
        commands = []
        for line in lines:
            direction, distance = line.split()
            commands.append((direction, int(distance)))
        return commands


def day_nine_part_one() -> int:
    commands = read_day_nine_input()
    rope = Rope()
    for command in commands:
        rope.process_motion(command[0], command[1])
    return len(rope.tail_locations)

def day_nine_part_two() -> int:
    commands = read_day_nine_input()
    rope = Rope(9)
    for command in commands:
        rope.process_motion(command[0], command[1])
        #print(command)
        #print(rope)
        #print()
    #rope.print_tail_locations()
    return len(rope.tail_locations)

if __name__ == '__main__':
    print(day_nine_part_two())