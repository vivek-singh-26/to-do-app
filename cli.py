# from functions import get_todos, write_todos
import functions
import time

now = time.strftime('%b %d, %Y %H:%M:%S')
print("It is", now)
user_prompt = 'Please type add, show, edit, complete or exit: '

while True:
    user_action = input(user_prompt)

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()

        for index, items in enumerate(todos):
            items = items.strip('\n')
            print(f'{index + 1}. {items}')
    elif user_action.startswith('edit'):
        try:
            todos = functions.get_todos()
            if len(todos) == 0:
                print('No item in Todo to edit, please enter an item first!')
            else:
                # for index, items in enumerate(todos):
                #     items = items.strip('\n')
                #     print(f'{index + 1}. {items}')
                number = int(user_action[5:])
                new_input = input('Please edit the Todo: ')
                todos[number - 1] = new_input + '\n'

                functions.write_todos(todos)
        except ValueError:
            print('Please enter a number after edit command!')
            continue
        # except IndexError:
        #     print('Please enter a number within todo list limit!')
    elif user_action.startswith('complete'):
        try:
            todos = functions.get_todos()
            # for index, items in enumerate(todos):
            #     print(f'{index + 1}. {items}')
            number = int(user_action[9:])
            complete_todo = todos[number - 1].strip('\n')
            todos.pop(number - 1)

            functions.write_todos(todos)
            print(f"Marking the to-do {complete_todo} as complete.")
        except IndexError:
            print('Please enter a number within todo list limit!')
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print('Please enter a valid command!')

print('Bye!')
