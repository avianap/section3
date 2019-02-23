'''
Agenda:
1) Releasing resources and "with" statements
2) Context managers, enter and exit methods
3) Contextlib (decorator style context managers)
** Using git throughout!
'''

#Exercise 1

#What is wrong here? 
#How can we fix it without using "with"? How do we fix it using "with"

def write_value_to_file():
    f = open('output.txt', 'w')
    msg = 'Hello World'
    print(msg)
    f.write(msg)

write_value_to_file()    
