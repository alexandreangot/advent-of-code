file = open("input", "r")

# Day 1 #
print("----- Day 1 -----")

### Part 1 ###
print("\n• Part 1 •")

lines = file.read().splitlines()
total = 0
for line in lines:
    calibration_value = ''
    for i in range(0, len(line)):
        if line[i].isdigit():
            calibration_value += line[i]
            break
    
    for i in range(len(line)-1, -1, -1):
        if line[i].isdigit():
            calibration_value += line[i]
            break

    total += int(calibration_value)
    
print(f"The total calibration value is {total}.")



### Part 2 ###
print("\n• Part 2 •")

digit_in_letter = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
total = 0
for line in lines:
    find_digits = []
    for i,c in enumerate(line):
        if c.isdigit():
            find_digits.append(c)
        for j,digit in enumerate(digit_in_letter):
            if line[i:].startswith(digit):
                find_digits.append(str(j+1))
                break
    
    calibration_value = int(find_digits[0] + find_digits[-1])
    # print(f"{line} - {calibration_value}")
    total += calibration_value
    
print(f"The total calibration value is {total}.")
