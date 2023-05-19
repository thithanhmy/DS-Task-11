# DS-Task-11 - String Handling

#alter every second letter of the string
print('Example 1: ')
string = 'Hello World, Hello World'
new_string = ''     #create a placeholder for new string


for i in range(len(string)):        #learned from task 11 video on HyperionDev Dashboard --> Need index values of the string
    if i % 2 == 1:      #choose every second letter with modulos.
        new_string += string[i].lower()
    
    else:
        new_string += string[i].upper()

print(new_string)

print(' ')      #extra line

#alter every second word of the string and use string from above
print('Example 2: ')
string_list = string.split()       #create a list of separate items

new_string_2 = ''

for i in range(len(string_list)):         
    if i % 2 == 1:     
        new_string_2 += string_list[i].lower() + ' '

    else:
        new_string_2 += string_list[i].upper() + ' '


print(new_string_2)


