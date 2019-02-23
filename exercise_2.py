'''
Agenda:
1) Releasing resources and "with" statements
2) Context managers, enter and exit methods
3) Contextlib (decorator style context managers)
** Using git throughout!!
'''

#Exercise 2
#How can I change this to use the context manager "ManagedFile"?

class ManagedFile(object):
    """Starter context manager
    """
    def __init__(self, file_name, method):
        print("initializing")
        self.file_obj = open(file_name, method)

    def __enter__(self):
        print("entering")
        return self.file_obj

    def __exit__(self, type, value, traceback):
        print("exiting")
        self.file_obj.close()

def write_value_to_file():
    with open('output_2.txt', 'w') as f:
        msg = "Hello World"
        print(msg)
        f.write(msg)

write_value_to_file()    
