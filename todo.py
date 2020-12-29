# Importing the sys package for reading the command line input and datetime package for date
import sys
from datetime import date

# help function to show what can the TODO do.
def help():
    print('''Usage :-\n$ ./todo add \"todo item\"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics''')


# Function to get all todos
def get_todo(file_name):
    try:
        # Opening the file in read mode
        f = open(file_name,'r')
        try:
            todo_list = f.readlines()    
        finally:
            f.close()
    except:
        return []

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
    todo_list = get_todo("todo.txt")
    task_count = len(todo_list)
    
    if todo_list == []:
        print("There are no pending todos!")
    else:
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
    todo_list = get_todo("todo.txt")
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
    todo_list = get_todo("todo.txt")
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


# Function to get the statistics of pending and completed task
def report():
    # Getting all the pending todos
    todo_list = get_todo("todo.txt")
    todo_count = len(todo_list)

    # Getting all the done todos
    done_list = get_todo("done.txt")
    done_count = len(done_list)

    print("{} Pending : {} Completed : {}".format(date.today(),todo_count,done_count))



# Calculating the lenght of arguments recieved
arg_len = len(sys.argv)

# If no arguments recieved print the usage
if (arg_len == 1):
    help()

# Display the list of pending todos
elif arg_len == 2 and sys.argv[1] == 'ls': 
    ls()

# Display the help menu
elif arg_len == 2 and sys.argv[1] == 'help': 
    help()


# Adding new task to the todo list
elif sys.argv[1] == "add":
    if arg_len > 2:
        add(sys.argv[2])
        print('Added todo: "{}"'.format(sys.argv[2]))
    else:
        print("Error: Missing todo string. Nothing added!")

# Deleting a todo from the list
elif sys.argv[1] == "del":
    if arg_len > 2:
        item_num = int(sys.argv[2])
        if del_todo(item_num):
            print("Deleted todo #{}".format(item_num))
        else:
            print("Error: todo #{} does not exist. Nothing deleted.".format(item_num))
    else:
        print("Error: Missing NUMBER for deleting todo.")


# Marking todo as done
elif sys.argv[1] == "done":
    if arg_len >2:
        item_num = int(sys.argv[2])
        if done(item_num):
            print("Marked todo #{} as done.".format(item_num))
        else:
            print("Error: todo #{} does not exist.".format(item_num))
    else:
        print("Error: Missing NUMBER for marking todo as done.")
    
  
# Displaying the statistics of done and pending todos
if arg_len == 2 and sys.argv[1] == 'report': 
    report()
    

