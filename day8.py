from typing import List

class Forest:
    def __init__(self, rows: List[str] = []):
        self.trees = [[int(char) for char in row] for row in rows]

    def count_visible_trees(self) -> int:
        acc = 2 * len(self.trees[0]) + 2 * len(self.trees) - 4
        for row_idx in range(1, len(self.trees) - 1):
            for col_idx in range(1, len(self.trees[row_idx]) - 1):
                tree_height = self.trees[row_idx][col_idx]
                if self.visible_up(row_idx, col_idx, tree_height) or self.visible_down(row_idx, col_idx, tree_height) or self.visible_left(row_idx, col_idx, tree_height) or self.visible_right(row_idx, col_idx, tree_height):
                    acc += 1

        return acc
    
    def visible_up(self, row_idx: int, col_idx: int, tree_height: int) -> bool:
        for row in self.trees[:row_idx]:
            tree = row[col_idx]
            if tree >= tree_height:
                return False
        return True
    
    def visible_down(self, row_idx: int, col_idx: int, tree_height: int) -> bool:
        for row in self.trees[row_idx+1:]:
            tree = row[col_idx]
            if tree >= tree_height:
                return False
        return True

    def visible_left(self, row_idx: int, col_idx: int, tree_height: int) -> bool:
        for tree in self.trees[row_idx][:col_idx]:
            if tree >= tree_height:
                return False
        return True

    def visible_right(self, row_idx: int, col_idx: int, tree_height: int) -> bool:
        for tree in self.trees[row_idx][col_idx+1:]:
            if tree >= tree_height:
                return False
        return True

    def highest_scenic_score(self) -> int:
        _max = 0
        for row_idx in range(len(self.trees)):
            for col_idx in range(len(self.trees[row_idx])):
                score = self.scenic_score(row_idx, col_idx)
                if score > _max:
                    _max = score
        return _max

    def scenic_score(self, row_idx: int, col_idx: int) -> int:
        tree_height = self.trees[row_idx][col_idx]
        score = self.score_up(row_idx, col_idx, tree_height) * self.score_down(row_idx, col_idx, tree_height) * self.score_left(row_idx, col_idx, tree_height) * self.score_right(row_idx, col_idx, tree_height)
        return score

    def score_up(self, row_idx: int, col_idx: int, tree_height: int) -> int:
        score = 0
        for row in reversed(self.trees[:row_idx]):
            tree = row[col_idx]
            if tree >= tree_height:
                return score + 1
            score += 1
        return score

    def score_down(self, row_idx: int, col_idx: int, tree_height: int) -> int:
        score = 0
        for row in self.trees[row_idx+1:]:
            tree = row[col_idx]
            if tree >= tree_height:
                return score + 1
            score += 1
        return score

    def score_left(self, row_idx: int, col_idx: int, tree_height: int) -> int:
        score = 0
        for tree in reversed(self.trees[row_idx][:col_idx]):
            if tree >= tree_height:
                return score + 1
            score += 1
        return score

    def score_right(self, row_idx: int, col_idx: int, tree_height: int) -> int:
        score = 0
        for tree in self.trees[row_idx][col_idx+1:]:
            if tree >= tree_height:
                return score + 1
            score += 1
        return score

def read_day_eight_input() -> Forest:
    with open('inputs/day8.txt') as f:
        lines = [line.replace('\n', '') for line in f.readlines()]
        return Forest(lines)

def day_eight_part_one() -> int:
    forest = read_day_eight_input()
    return forest.count_visible_trees()

def day_eight_part_two() -> int:
    forest = read_day_eight_input()
    return forest.highest_scenic_score()

if __name__ == '__main__':
    print(day_eight_part_two())