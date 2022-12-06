def read_day_six_input() -> str:
    with open('inputs/day6.txt') as f:
        return f.read().replace('\n', '')

def day_six_part_one() -> int:
    signal = read_day_six_input()
    for i in range(0, len(signal) - 4):
        if len(set(signal[i:i+4])) == 4:
            return i + 4

def day_six_part_two() -> int:
    signal = read_day_six_input()
    for i in range(0, len(signal) - 14):
        if len(set(signal[i:i+14])) == 14:
            return i + 14

if __name__ == '__main__':
    print(day_six_part_two())