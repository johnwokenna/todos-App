import functions
import time

mytime = time.strftime("%d - %b - %Y %H:%M:%S")
print("My date/time stamp is",mytime)

while True:
    user_action = input("Type Add, Show, edit, complete or Exit ")
    user_action = user_action.strip()
#    match user_action:
    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'

        """file = open("Data\\todos.txt", 'r')
        todos = file.readlines()
        file.close()"""

    # with content manager to improve our (open, read and close file)
        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)
    #case 'show':
    elif user_action.startswith('show'):

        todos = functions.get_todos()

        """ new_todos = []
        for item in todos:
            new_item = item.strip('\n')
            new_todos.append(new_item) 
            we used list comprehension below to do this """

        #new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n') # used to remove extra '\n
            row = f"{index +1}-{item}"
            print(row)
    #case 'edit':
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)
        except ValueError:
            print('Invalid command')
            continue

    #case 'complete':
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"{todo_to_remove} was removed from the file"
            print(message)
        except IndexError:
            print('Item not available')
    #case 'exit':
    elif user_action.startswith('exit'):
        break
    else:
        print("Invalid command")
print('Bye')
