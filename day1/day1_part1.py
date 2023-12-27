f = open("day1input.txt", "r") 
#open file

digits_list = [] 
 #initiate an empty list to add digits to

for i in f: 
    emp_string = "" 
    for e in i: 
        if e.isdigit(): 
            emp_string = emp_string + e
    digits_list.append(int(emp_string[0] + emp_string[-1]))
    emp_string = ""
""" for every character of every line in the input text file, if the character is a digit
    add the digit to an empty string. however, we only want the first and the last digit 
    of every line in the file, so combine only the first and last digit, before adding to 
    digits_list.
"""

print(sum(digits_list)) 
#return the sum of all the numbers in the list.