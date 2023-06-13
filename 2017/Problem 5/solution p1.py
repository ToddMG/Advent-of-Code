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
            instructions[loc] = instructions[loc] + 1
            loc += jump
            tracker += 1
            print("Step %s, loc is %s" %(tracker, loc))
        except Exception as e:
            print(e)
            return tracker

    return tracker    

instructions = read_input('input.txt')
print(instructions)
jumps = jump(instructions)
print("Total jumps: %s" %jumps) 
