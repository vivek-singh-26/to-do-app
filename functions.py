FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """ Reads a text file and returns the to-do items in a list."""
    with open(filepath, 'r') as get_file:
        todos_local = get_file.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Writes the to-do items in the test file."""
    with open(filepath, 'w') as write_file:
        write_file.writelines(todos_arg)
