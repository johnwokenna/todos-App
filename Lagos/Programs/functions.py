FILEPATH = 'Data\\todos.txt'

def get_todos(filepath=FILEPATH):
    """ a function that reads opens and read the file"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ a function that opens and writes into the file"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
