import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

windows = sg.Window("My first Windows - To do App", layout=[[label], [input_box, add_button]])
windows.read()
windows.close()