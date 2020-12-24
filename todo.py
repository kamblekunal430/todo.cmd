import sys


# help/Usage function to show what can the TODO do.
def usage():
    print("Usage:-")
    print('$ ./todo add "todo item" # Add a new todo')
    print('$ ./todo ls              # Show remaining todos')
    print('$ ./todo del NUMBER      # Delete a todo')
    print('$ ./todo done NUMBER     # Complete a todo')
    print('$ ./todo help            # Show usage')
    print('$ ./todo report          # Statistics')
    
usage()
