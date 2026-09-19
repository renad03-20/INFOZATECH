print(' Welcome  to you\'r TODO List')
print('*----menu----*')
print('1. Add Task')
print('2. show Task')
print('3. Mark as Done')
print('4. Remove Task')
print('5. exit')
print('*----****----*')

def main():
    tasks = load()

    while True:
        option = input('Enter you\r choice: ')

        if option == '1':
            add_task(tasks)
        elif option == '2':
            show_task(tasks)
        elif option == '3':
            mark_as_done(tasks)
        elif option == '4':
            remove_task(tasks)
        elif option == '5':
            print("Exiting.")
            save(tasks)
            break
        else:
            print('please slecet a valid option! ')

def add_task(tasks):
    task = input('Ente yor task: ')
    tasks.append(task)
    print('task Addeed')

def show_task(tasks):
    print('\n Tasks: ')
    for i, task in enumerate(tasks, start=1):
        print(i,'*', task)

def mark_as_done(tasks):
    ...

def remove_task(tasks):
    if not tasks:
        print('There are no tasks to remove!')
        return

    show_task(tasks)
    index = input('Enter task index to remove: ')

    if not index.isdigit():
        print('Please enter a valid number: ')
        return

    inde_x = int(index) -1 
    if 0 <= inde_x < len(tasks):
        removed = tasks.pop(inde_x)
        save(tasks)
        print(f'Task "{removed}" removed successfully.')
    else:
        print('Invalid task number.')

def save(tasks):
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def load():
    try:
        with open('tasks.txt', 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

if __name__ == "__main__":
    main()