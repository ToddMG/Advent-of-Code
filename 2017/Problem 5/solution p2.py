def read_input(filename: str) -> list[int]:
    
    input = []
    with open(filename, 'r') as file:
        for number in file:
            input.append(int(number))
        
    return input

def jump(instructions: list[int]) -> int:

    loc = 0
    tracker = 0
    
    while True:
        
        try:
            jump = instructions[loc]
            if jump >= 3:
                instructions[loc] = instructions[loc] - 1
            else:
                instructions[loc] = instructions[loc] + 1
            loc += jump
            tracker += 1
        except Exception as e:
            print(e)
            return tracker

    return tracker    

instructions = read_input('input.txt')
print(instructions)
jumps = jump(instructions)
print("Total jumps: %s" %jumps) 
