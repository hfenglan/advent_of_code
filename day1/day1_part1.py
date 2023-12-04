f = open("day1input.txt", "r") 

digits_list = [] 
 
for i in f:
    emp_string = "" 
    for e in i: 
        if e.isdigit(): 
            emp_string = emp_string + e # 
    digits_list.append(int(emp_string[0] + emp_string[-1]))
    emp_string = ""

print(sum(digits_list))