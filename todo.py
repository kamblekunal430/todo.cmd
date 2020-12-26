# Importing the sys package for reading the command line input
import sys


# help function to show what can the TODO do.
def help():
    print("Usage :-")
    print('$ ./todo add "todo item"  # Add a new todo')
    print('$ ./todo ls               # Show remaining todos')
    print('$ ./todo del NUMBER       # Delete a todo')
    print('$ ./todo done NUMBER      # Complete a todo')
    print('$ ./todo help             # Show usage')
    print('$ ./todo report           # Statistics')


# Function to get all todos
def get_todo():
    try:
        # Opening the file in read mode
        f = open("todo.txt",'r')
        todo_list = f.readlines()    
    finally:
        f.close()

    return todo_list


# Function to list all pending todos
def ls():
    # Getting the all pending todos
    todo_list = get_todo()
    task_count = len(todo_list)
    
    # Printing all the pending todos
    for task in todo_list[::-1]:
        print("[{}] {}".format(task_count,task[:-1]))
        task_count-=1


# Function to add new todo item
def add(item):
    try:
        # Opening the file in append mode to add the item
        f = open("todo.txt","a")
        f.write(str(item)+"\n")
        
    finally:
        f.close()

# Function to delete a todo item
def del_todo(item_num):
    # Getting all the pending todos
    todo_list = get_todo()
    task_count = len(todo_list)

    # checking if the item number is valid
    if item_num <= task_count and item_num > 0:
        # deleting the required todo
        todo_list.pop(item_num - 1)
        print("Deleted todo #{}".format(item_num))
        # updating the todo.txt file
        try:
            f = open("todo.txt",'w')
            for task in todo_list:
                f.write(task)

        finally:
            f.close()

    else:
        # The item number is not valid
        print("Error: todo #{} does not exist. Nothing deleted.".format(item_num))



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

# Deleting a todo from the list
if arg_len > 2 and sys.argv[1] == "del":
    del_todo(int(sys.argv[2]))
    
