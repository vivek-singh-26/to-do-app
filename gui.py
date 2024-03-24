import functions
import PySimpleGUI as sg

label = sg.Text('Type in a to-do: ')
user_input = sg.InputText(tooltip='Enter a to-do')
add_button = sg.Button('Add')

window = sg.Window('My To-Do App', layout=[[label, user_input, add_button]])
window.read()
window.close()


