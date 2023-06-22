while True:
    user_action = (input("Type add, show or exit: "))
    user_action = user_action.strip()
    user_action = user_action.lower()

    match user_action:
        case 'add':
            todo = input("Enter todo: ") + "\n"

            with open('data1.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('data1.txt', 'w') as file:
                file.writelines(todos)
        case 'show':
           # file = open('data1.txt', 'r')
           # todos = file.readlines()
           # file.close()

           with open('data1.txt', 'r') as file:
               todos = file.readlines()

           print (todos)
           # new_todos = []
           #  for todo in todos:
           #      new_todos.append(todo.strip())
           #  print (new_todos)

           new_todos = [todo.strip('\n') for todo in todos]

           for index, item in enumerate (new_todos):
                print(index, item)
        case 'exit':
            break
print ("Bye")