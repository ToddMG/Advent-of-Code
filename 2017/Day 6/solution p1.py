# find i bank with most blocks (take first if tied)
# take i value as x, change to i(x) = 0 
# iterate x times over banks after i in succession and add 1 until cycle is done
# store new iteration list in list of lists for future matching
# keep track of cycles

def distribution(banks: list[int]) -> int:

    cycle = 0
    previous = []
    previous.append(banks[:])

    while True:
        cycle += 1
        i = banks.index(max(banks))
        x  = banks[i]
        banks[i] = 0
        i += 1

        while x > 0:
            if i < len(banks):
                banks[i] += 1
                i += 1
                x -= 1
            elif i == len(banks):
                i = 0
                banks[i] += 1
                i += 1
                x -= 1
                
        if banks in previous:
            return cycle
        
        else:
            previous.append(banks[:])


input = [4,	1,	15,	12,	0,	9,	9,	5,	5,	8,	7,	3,	14,	5,	12,	3]
answer = distribution(input)
print("The answer is %s" %answer)

