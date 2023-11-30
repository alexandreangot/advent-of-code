file = open("input", "r")

# Day 2 #
print("----- Day 2 -----")

### Part 1 ###
print("\n• Part 1 •")

def get_priority(item):
    if item >= 'a' and item <= 'z':
        priority = ord(item) - 96
    elif item >= 'A' and item <= 'Z':
        priority = ord(item) - 64 + 26
    else:
        print("Invalid item.")
        return 0
    
    return priority

rucksacks = file.read().splitlines()
total = 0

for rucksack in rucksacks:
    for e1 in rucksack[0:len(rucksack)//2]:
        for e2 in rucksack[len(rucksack)//2:len(rucksack)]:
            if e1 == e2:
                item = e1
                break
    
    # print(f"{rucksack} -> {item}")
    total += get_priority(item)

print(f"The sum of the priorities is {total}.")



### Part 2 ###
print("\n• Part 2 •")

total = 0
for i in range(0, len(rucksacks), 3):
    for e1 in rucksacks[i]:
        for e2 in rucksacks[i+1]:
            for e3 in rucksacks[i+2]:
                if e1 == e2 == e3:
                    item = e1
                    break
    
    # print(f"\n{rucksacks[i]}\n{rucksacks[i+1]}\n{rucksacks[i+2]}\nitem: {item}")
    total += get_priority(item)
    
print(f"The sum of the priorities is {total}.")
