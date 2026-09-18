print(' Welcome  to you\'r TODO List')
print('*----menu----*')
print('1. Add Task')
print('2. show Task')
print('3. Mark as Done')
print('4. exit')
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
    if not tasks:
        print('there is no task to mark!')
    else:
        show_task(tasks)
        index = int(input('Enter task index: ')) - 1

        if 0 <= index < len(tasks):
            removed_task  = tasks.pop(index)
            print(f'Task {removed_task} marked as done and removed')
        else:
            print('Invalid task index')

def save(tasks):
    with open('tasks.txt', 'a') as file:
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