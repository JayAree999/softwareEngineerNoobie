# This is a sample Python script.
from statistics import stdev

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

with open("filename.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append(int(line))
    # printing the data
        mean = sum(lines)/len(lines)
        variance = sum([((x - mean) ** 2) for x in lines]) / len(lines)
        res = variance ** 0.5

    print(mean)
    print(res)
    print(min(lines))
    print(max(lines))








    # See PyCharm help at https://www.jetbrains.com/help/pycharm/



