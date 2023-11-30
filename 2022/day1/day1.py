file = open("input", "r")

# Day 1 #
print("----- Day 1 -----")
### Part 1 ###
print("\n• Part 1 •")

lines = file.readlines()
somme = []
tmp = 0

for line in lines:
    if line == "\n":
        somme.append(tmp)
        tmp = 0
        continue
    tmp += int(line)

print(f"The Elf carrying the most Calories is the n°{somme.index(max(somme))+1} with {max(somme)} Calories.")



### Part 2 ###
print("\n• Part 2 •")

sommePodium = 0
for i in range(3):
    index = somme.index(max(somme))
    sommePodium += somme.pop(index)
    
print(f"The total Calories of the 3 Elves on the podium is {sommePodium}.")