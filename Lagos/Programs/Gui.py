import functions
import PySimpleGUI as Sg

label = Sg.Text("Type in a to-do")
input_box = Sg.InputText(tooltip="Enter todo")
add_button = Sg.Button("Add")

windows = Sg.Window("My first Windows - To do App", layout=[[label], [input_box, add_button]])
windows.read()
windows.close()