with open('input.txt') as input:
    lines = input.readlines()
    for line in lines:
        for i in range(len(lines)):
            answer = int(line) + int(lines[i])
            if answer == 2020:
                print(int(line) * int(lines[i]))
                