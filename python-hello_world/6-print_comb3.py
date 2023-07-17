#!/usr/bin/python3
i = 0
j = 1
while i < 9:
    while j < 10:
        print("{:02d}, ".format(i * 10 + j), end="" if i * 10 + j == 89 else " ")
        j += 1
    i += 1
    j = i + 1
print()
