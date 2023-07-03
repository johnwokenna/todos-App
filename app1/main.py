import functions
import time


now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    user_action = input("Enter Add, Edit, Show, Complete or Exit: ")

    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()

        # new_todos = [item.strip('\n') for item in todos] list comprehension

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"

            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not value")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            number = number - 1

            todos = functions.get_todos()

            todo_to_be_removed = todos.pop(number).strip('\n')

            functions.write_todos(todos)

            message = f"{todo_to_be_removed} is removed from the file"
            print(message)
        except IndexError:
            print("Index is out of range")

    elif user_action.startswith('exit'):
        break
    else:
        print("Command isn't valid")

print("Bye!")
