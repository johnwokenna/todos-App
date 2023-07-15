import functions
import PySimpleGUI as Sg
import time

Sg.theme("black")

label_clock = Sg.Text('', key='clock')
label = Sg.Text("Type in a to-do")
input_box = Sg.InputText(tooltip="Enter todo", key='add_todo')
add_button = Sg.Button("Add")

list_box = Sg.Listbox(values=functions.get_todos(), key='edit_todo',
                    enable_events=True, size=[45, 10])
edit_button = Sg.Button("Edit")

delete_button = Sg.Button("Delete")

exit_button = Sg.Button("Exit")

window = Sg.Window("My To-Do App",
                   layout=[[label_clock],
                           [label], [input_box, add_button], [list_box, edit_button, delete_button],
                           [exit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=200)

    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(1, event)
    print(2, values)
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['add_todo'] + '\n'
            if values['add_todo'] != "":
                todos.append(new_todo)
                functions.write_todos(todos)
                window['edit_todo'].update(values=todos)
        case 'Edit':
            try:
                todo_to_edit = values['edit_todo'][0]
                new_todo = values['add_todo'] + '\n'

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)

                window['edit_todo'].update(values=todos)
            except IndexError:
                Sg.popup("Please select an item", font=('Helvetica', 20))
        case 'edit_todo':
            window['add_todo'].update(value=values['edit_todo'][0])

        case 'Delete':
            todos = functions.get_todos()
            todo_to_remove = values['edit_todo'][0]
            # new_todo = values['add_todo'] + '\n'

            todos.remove(todo_to_remove)

            # index = todos.index(todo_to_remove)
            # removed_item = todos.pop(index)
            functions.write_todos(todos)

            window['edit_todo'].update(values=todos)
            window['add_todo'].update(value='')
        case 'Exit':
            break
        case Sg.WIN_CLOSED:
            break

window.close()
