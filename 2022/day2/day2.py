file = open("input", "r")

# Day 2 #
print("----- Day 2 -----")

### Part 1 ###
print("\n• Part 1 •")

lines = file.read().splitlines()

shapes = ['Rock', 'Paper', 'Scissors']
elf = ['A', 'B', 'C']
me = ['X', 'Y', 'Z']

total = 0
for line in lines:
    line = line.split(' ')
    elf_index = elf.index(line[0])
    me_index = me.index(line[1])
    # print(f"\n{shapes[elf_index]} vs {shapes[me_index]}")
    # print(f"{shapes[me_index]} ({me_index+1})", end=' - ')
    
    total += me_index+1
    
    if elf_index == me_index: # Draw
        total += 3
        # print("Draw (3)")
        continue
    
    if elf_index == (me_index-1)%3: # Win
        # print("Win (6)")
        total += 6
        continue
    
    # print("Lost (0)") # Lost

print(f"My total score is {total}.")



### Part 2 ###
print("\n• Part 2 •")

total = 0
for line in lines:
    line = line.split(' ')
    elf_index = elf.index(line[0])
    me_index = me.index(line[1])
    
    match me[me_index]:
        case 'X': # Lost
            me_index = (elf_index-1)%3
        case 'Y': # Draw
            total += 3
            me_index = elf_index
        case 'Z': # Win
            total += 6
            me_index = (elf_index+1)%3

    total += me_index+1 # points of the object
    
print(f"My total score is {total}.")
    
    
