want_instructions = input("Would you like to view the instructions? ").lower()

# check the user says yes/no
if want_instructions == "yes" or want_instructions == "y":
    print("[instructions]")
elif want_instructions == "no" or want_instructions == "n":
    print("nu uh")
else:
    print("Please enter 'yes' or 'no' ")
