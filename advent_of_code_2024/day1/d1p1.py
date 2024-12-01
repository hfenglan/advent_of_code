# sort both lists from smallest to largest
# gather differences from both list 
# sum up the differences

with open('day1input.txt', 'r') as file:
    counter = 0
    first_list = []
    second_list = []
    for line in file:
        obj = line.strip().split('  ')
        first_list.append(obj[0])
        second_list.append(obj[1])
    first_list.sort()
    second_list.sort()
    for i in range(len(first_list)):
        counter = counter + abs(int(first_list[i]) - int(second_list[i]))
    print(counter)
    
    #content = file.read()
    #print(content)

