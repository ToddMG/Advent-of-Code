def read_input(filename: str) -> list[str]:

    input = []
    with open(filename, 'r') as file:
        for line in file:
            input.append(line)

    return input

def sift(stream: list[str]):

    score = 0
    depth = 0
    skip = False
    garbage = False
    count = 0

    for item in stream:
        for i, c in enumerate(item):
            if skip:
                skip = False 
                continue
            if c == '!': 
                skip = True
                continue
            elif garbage and c != '>': count += 1
            elif c == '<': garbage = True
            elif c == '>': garbage = False
            elif c == '{':
                 depth += 1
                 score += depth
            elif c == '}': depth -= 1

    return score, count


file = read_input('input.txt')
do = sift(file)
print(do)

