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
        for task in todo_list[::-1]:
            print("[{}] {}".format(task_count,task))
            task_count-=1

    finally:
        f.close()




# Calculating the lenght of arguments recieved
arg_len = len(sys.argv)

# If no arguments recieved print the usage
if (arg_len == 1):
    help()

# Display the list of pending todos
if sys.argv[1] == 'ls': 
    ls()
