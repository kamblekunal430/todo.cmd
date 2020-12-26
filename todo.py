# Importing the sys package for reading the command line input and datetime package for date
import sys
from datetime import date

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

# Function to write todo in files
def write_todo(todo_list):
    try:
        f = open("todo.txt",'w')
        for task in todo_list:
            f.write(task)

    finally:
        f.close()



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

        # updating the todo.txt file
        write_todo(todo_list)

        # For successfull deletion
        return True

    else:
        # The item number is not valid
        return False
    

# Function to mark todo as done

def done(item_num):
    # Getting all the pending todos
    todo_list = get_todo()
    task_count = len(todo_list)

    # checking if the item number is valid
    if item_num <= task_count and item_num > 0:
        # marking the required todo as done
        done_todo = todo_list.pop(item_num - 1)

        # Adding done todo to done.txt file
        try:
            # Opening the file in append mode to add the item
            f = open("done.txt","a")
            f.write("x {} {}".format(date.today(),done_todo))
            
        finally:
            f.close()

        # updating the todo.txt file
        write_todo(todo_list)

        # For successfull done operation
        return True

    else:
        # The item number is not valid
        return False



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
    item_num = int(sys.argv[2])
    if del_todo(item_num):
        print("Deleted todo #{}".format(item_num))
    else:
        print("Error: todo #{} does not exist. Nothing deleted.".format(item_num))


# Marking todo as done
if arg_len > 2 and sys.argv[1] == "done":
    item_num = int(sys.argv[2])
    if done(item_num):
        print("Marked todo #{} as done".format(item_num))
    else:
        print("Error: todo #{} does not exist.".format(item_num))
    
    

