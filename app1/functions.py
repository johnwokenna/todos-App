FILEPATH = "data\\todo.txt"


def get_todos(filepath):
    """ Reads the items in the todo text file and returns a list."""
    with open(filepath, 'r') as local_file:
        todos_local = local_file.readlines()
    return todos_local


def write_todos(todos_arg, filepath):
    """ Writes a todo item into the text file todos.txt """
    with open(filepath, 'w') as local_file:
        local_file.writelines(todos_arg)
