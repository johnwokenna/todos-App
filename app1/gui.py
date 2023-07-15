import functions
import PySimpleGUI as Sg

label = Sg.Text("Type in a to-do")
input_box = Sg.InputText(tooltip="Enter todo", key='add_todo')
add_button = Sg.Button("Add")

list_box = Sg.Listbox(values=functions.get_todos(), key='edit_todo',
                    enable_events=True, size=[45, 10])
edit_button = Sg.Button("Edit")

window = Sg.Window("My To-Do App",
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()

    print(1, event)
    print(2, values)
    print(3, values['edit_todo'])
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['add_todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['edit_todo'].update(values=todos)
        case 'Edit':
            todo_to_edit = values['edit_todo'][0]
            new_todo = values['add_todo'] + '\n'

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)

            window['edit_todo'].update(values=todos)
        case 'edit_todo':
            window['add_todo'].update(value=values['edit_todo'][0])
        case Sg.WIN_CLOSED:
            break


window.close()
