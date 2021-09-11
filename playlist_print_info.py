from time import sleep

#prints the stores information from a file every 5s

file = open("pl_info2.txt")
lines = file.readlines()

i = 0
while True:
    while (i < 896):
        sleep(5)
        print(lines[i])
        print(lines[i+1])
        i += 2

file.close()
