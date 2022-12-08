from typing import List, Optional, Union

class VFile:
    def __init__(self, name: str, size: int, depth: int) -> None:
        self.name = name
        self._size = size
        self.depth = depth

    def size(self) -> int:
        return self._size

    def __str__(self) -> str:
        return "  " * self.depth + f'{self.name}, {self.size}'

class VDirectory:
    def __init__(self, name: str, parent: Optional['VDirectory'] = None) -> None:
        self.name = name
        self.parent = parent
        self.depth = 0 if parent is None else parent.depth + 1
        self.contents: List[Union['VDirectory', VFile]] = []

    def add_child(self, child: Union['VDirectory', VFile]) -> None:
        self.contents.append(child)

    def size(self) -> int:
        return sum([child.size() for child in self.contents])

    def __str__(self) -> str:
        output = "  " * self.depth + f'{self.name}\n'
        for child in self.contents:
            output += str(child) + '\n'
        return output


def read_day_seven_input() -> VDirectory:
    with open('inputs/day7.txt') as f:
        root = VDirectory('/')
        current_dir = root
        for idx, line in enumerate([line.replace('\n', '') for line in f.readlines()][1:]):
            try:
                if line.startswith('$ cd'): # command
                    _, _, dir_name = line.split(' ')
                    if dir_name == '..':
                        current_dir = current_dir.parent
                    else:
                        new_dir = None
                        for child in current_dir.contents:
                            if child.name == dir_name:
                                new_dir = child
                                break
                        if new_dir is None:
                            raise Exception(f'Could not find directory {dir_name}')
                        current_dir = new_dir
                elif line == '$ ls':
                    pass
                else: # ls output
                    if line.startswith('dir'):
                        _, dir_name = line.split(' ')
                        new_dir = VDirectory(dir_name, current_dir)
                        current_dir.add_child(new_dir)
                    else:
                        file_size, file_name = line.split(' ')
                        current_dir.add_child(VFile(file_name, int(file_size), current_dir.depth + 1))
            except Exception as e:
                print(idx, line)
                raise e
        return root
    
def day_seven_part_one() -> int:
    root = read_day_seven_input()

    directories_total_lt_100k = []
    to_search = [root]
    while to_search:
        curr_node = to_search.pop()
        if curr_node.size() < 100000:
            directories_total_lt_100k.append(curr_node)
        for child in curr_node.contents:
            if isinstance(child, VDirectory):
                to_search.append(child)
        
    return sum([dir.size() for dir in directories_total_lt_100k])

def day_seven_part_two() -> int:
    root = read_day_seven_input()
    
    total_space = 70000000
    free_space = total_space - root.size()
    update_space = 30000000
    space_needed = update_space - free_space

    nodes_that_free_enough_space = []
    to_search = [root]
    while to_search:
        curr_node = to_search.pop()
        if curr_node.size() > space_needed:
            nodes_that_free_enough_space.append(curr_node)
        for child in curr_node.contents:
            if isinstance(child, VDirectory):
                to_search.append(child)

    return min([node.size() for node in nodes_that_free_enough_space])

if __name__ == '__main__':
    print(day_seven_part_two())