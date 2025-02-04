# functions go here

def yes_no(question):

    """Checks user response to a question is yes / no / y / n, returns 'yes' or 'no' """

    while True:

        response = input(question).lower()

        # check the user says yes/no/y/n
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter 'yes' or 'no' ")

def instructions():
    """Prints instructions"""

    print("""
*** Instructions ***

Roll the dice and try to win.
    """)


#  Main routine
want_instructions = yes_no("Would you like to view the instructions? ").lower()

# Display the instructions if the user wants to see them.
if want_instructions == "yes":
    instructions()

print()
print("Program continues")