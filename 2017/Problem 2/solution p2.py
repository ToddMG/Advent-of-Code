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
        line.sort(reverse=True) 
        for number in line[:]:

            line.remove(number)

            for divisor in line:
                if number % divisor == 0:
                    sum += number // divisor
                    break
    
    return sum

numbers = read_input('input.txt')
thesum = checksum(numbers)
print(thesum)

# ---Derek Solution---

# def row_processor_2(sorted_row: List[int]) -> int:
#     for i in range(len(sorted_row)-1):
#         for j in range(i+1,len(sorted_row)):
#             if sorted_row[j] % sorted_row[i] == 0:
#                 return sorted_row[j] // sorted_row[i]
#     return 0

# # same as row_processor_2 but no indices
# import itertools
# def row_processor_2_alternate(sorted_row: List) -> int:
#     for left, right in itertools.combinations(sorted_row,r=2):
#         if right % left == 0:
#             return right // left
#     return 0


# def compute_checksum_2(sheet: List[List[int]]) -> int:
#     for row in sheet:
#         row.sort()
#     return sum(row_processor_2_alternate(row) for row in sheet)