from collections import Counter

def is_valid_phrase(phrase: list[str]) -> bool:
    check = []
    for item in phrase.split():
        if sorted(item) in check:
            return False
        else:
            check.append(sorted(item))
    return True


def check_phrases(input: list[list[str]]) -> int:
    valid_phrases = 0
    for phrase in input:
        if is_valid_phrase(phrase):
            valid_phrases += 1
    
    return valid_phrases


def read_input(filename: str) -> list[list[str]]:

    input = []
    with open(filename, 'r') as file:
        for line in file:
            input.append(line)

    file.close()

    return input
    
input = read_input('input.txt')
number_of_valid = check_phrases(input)
print("Number of valid phrases: %s" % number_of_valid)
