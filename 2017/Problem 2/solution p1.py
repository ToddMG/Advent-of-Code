input = []

def read_input(filename: str) -> list[list[int]]:

    input = []
    with open(filename, 'r') as file:
        for line in file:
            input.append([int(word) for word in line.split()])

    return input

def checksum(input):
    sum = 0

    for line in input:
        big = 0
        small = 1000000
        
        for number in line:
            if number > big:
                big = number
            if number < small:
                small = number
        
        sum += big - small 
            
    
    return sum

numbers = read_input('input.txt')
thesum = checksum(numbers)
print(thesum)

# --- Derek Solution ---

# def compute_checksum_1(sheet: List[List[int]]):
#     return sum(max(row) - min(row) for row in sheet)