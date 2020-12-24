import sys


# help function to show what can the TODO do.
def help():
    print("Usage:-")
    print('$ ./todo add "todo item" # Add a new todo')
    print('$ ./todo ls              # Show remaining todos')
    print('$ ./todo del NUMBER      # Delete a todo')
    print('$ ./todo done NUMBER     # Complete a todo')
    print('$ ./todo help            # Show usage')
    print('$ ./todo report          # Statistics')


# Function to list all pending todos
def ls():
    try:
        # Opening the file in read mode
        f = open("todo.txt",'r')
        todo_list = f.readlines()
        task_count = len(todo_list)
        print(todo_list)
        for task in todo_list[::-1]:
            print("[{}] {}".format(task_count,task[:-1]))
            task_count-=1

    finally:
        f.close()

# Function to add new todo item
def add(item):
    try:
        # Opening the file in append mode to add the item
        f = open("todo.txt","a")
        f.write(str(item)+"\n")
        
    finally:
        f.close()


# Calculating the lenght of arguments recieved
arg_len = len(sys.argv)

# If no arguments recieved print the usage
if (arg_len == 1):
    help()

# Display the list of pending todos
if arg_len == 2 and sys.argv[1] == 'ls': 
    ls()


# Adding new task to the todo list
if arg_len > 2 and sys.argv[1] == "add":
    add(sys.argv[2])
    print('Added todo: "{}"'.format(sys.argv[2]))