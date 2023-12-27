word2numdict = {
    'one': 'o1e',
    'two': 't2o',
    'three': 't3e',
    'four': 'f4r',
    'five': 'f5e',
    'six': 's6x',
    'seven': 's7n',
    'eight': 'e8t',
    'nine': 'n9e'
}


def replace_words(text):
    for k, v in word2numdict.items():
        text = text.replace(k, v)
    return text

f = open("day1input.txt", "r") 

digits_list = []

for i in f:
    i = replace_words(i)
    emp_string = "" 
    for e in i: 
        if e.isdigit(): 
            emp_string = emp_string + e
    digits_list.append(int(emp_string[0] + emp_string[-1]))
    emp_string = ""

print(sum(digits_list))