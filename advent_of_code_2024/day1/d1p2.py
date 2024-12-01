import itertools


with open('day1input.txt', 'r') as file:
    counter = 0
    first_list = []
    second_list = []
    for line in file:
        obj = line.strip().split('  ')
        first_list.append(int(obj[0]))
        second_list.append(int(obj[1]))
    for i in first_list:
        counter = counter + (i * second_list.count(i))
    print(counter)