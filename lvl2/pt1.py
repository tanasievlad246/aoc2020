valid_counter = 0
invalid_counter = 0

with open('input.txt') as input:
    lines = input.readlines()
    for line in lines:
        password = line.split()
        interval = password[0].split("-")
        target_letter = password[1].split(":")
        letter_count = password[2].count(target_letter[0])

        #print(letter_count)

        if letter_count >= int(interval[0]) and letter_count <= int(interval[1]):
            valid_counter += 1
        else:
            invalid_counter += 1
    
    print(f"Valid passwords -> {valid_counter}")
    print(f"Invalid passwords -> {invalid_counter}")