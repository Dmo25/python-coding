#!/usr/bin/python3
i = 0
j = 1
last_combination = 89

while i < 9:
    while j < 10:
        if i * 10 + j == last_combination:
            print("{:02d}".format(i * 10 + j))
        else:
            print("{:02d}, ".format(i * 10 + j), end="")
        j += 1
    i += 1
    j = i + 1
