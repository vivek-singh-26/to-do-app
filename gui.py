import functions
import PySimpleGUI as sg
import time

time_label = sg.Text(time.strftime('%b %d, %Y %H:%M:%S'))

label = sg.Text('Type in a to-do: ')
user_input = sg.InputText(tooltip='Enter a to-do', key='todo')
todo_list = sg.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=[45, 10])
add_button = sg.Button('Add')
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')
exit_button = sg.Button('Exit')
compete_output = sg.Text(key='output')

window = sg.Window('My To-Do App',
                   layout=[[time_label], [label], [user_input, add_button], [todo_list, edit_button, complete_button],
                           [exit_button, compete_output]],
                   font=('Helvetica', 12))
while True:
    event, value = window.read()
    print(event)
    print(value)
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = value['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            todo_to_edit = value['todos'][0]
            new_todo = value['todo'] + '\n'

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=value['todos'][0])
        case 'Complete':
            todo_to_complete = value['todos'][0]
            completed_todo = todo_to_complete.strip('\n')
            todos = functions.get_todos()
            index = todos.index(todo_to_complete)
            todos.pop(index)
            functions.write_todos(todos)
            window['output'].update(value=f'{completed_todo} is completed')
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case 'Exit':
            break
        case sg.WINDOW_CLOSED:
            break

window.close()
