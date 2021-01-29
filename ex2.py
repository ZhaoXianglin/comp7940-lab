import json
import requests

site="https://api.npoint.io/2b57052af2060e84dc86"

# Your code goes here
def convert_number(str):
    temp = []
    for i in str[1:]:
        try:
             num = int(i)
             temp.append(num)
        except:
            continue
    return temp

def replace_number(number_list, being_replace,to_replace):
    if being_replace < to_replace:
        if to_replace > len(number_list)+1:
            to_replace = len(number_list)+1
        
        for i in range(being_replace-1,to_replace - 1):
            # print(number_list[i])
            if number_list[i] == 1:
                number_list[i] = 10
    return number_list

# Trying to load JSON into text
r = requests.get(site)
print(r.json())
text = r.json()['users']

# Debug
for i in text:
    print("parse " + str(i))



# call the function convert_number
# convert all elements (except the first one) into number and return it as a list
y = convert_number(text[0]) 

print("y")
print(y)

# call the function replace_number
# replace all number 1 by the number 10 in the function
z = replace_number(number_list = y, being_replace = 1, to_replace = 10)

print("z")
print(z)

sum = 0
for i in z:
    sum = sum + i
    print("sum = " + str(sum) + "; i =" + str(i))
print ("Total = " + str(sum))
