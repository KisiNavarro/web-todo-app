
FILEPATH = 'todos.txt'
def get_todos(filepath=FILEPATH):
    """ Read a text file and return list of the to
    do items """
    with open (filepath,'r') as archive:
        todos_local = archive.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the todo items list in text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

text = """triple quotes to multiline string

"""

if __name__ == '__name__':
   print('hello from functions')
