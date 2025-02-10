# set player and bot score to 0

comp_score = 0
user_score = 0

game_goal = int(input("Game Goal: "))

# play multiple rounds until a winner is found
while comp_score < game_goal and user_score < game_goal:
    # start of round loop
    comp_points = int(input("Enter the computer points at the end of the round: "))
    user_points = int(input("Enter the user points at the end of the round"))

    # outside rounds loop - update score with round points - only add points to the score of the
    comp_score += comp_points
    user_score += user_points

    # show overall scores (add this to the rounds loop)
    print("*** Game Update ***")  # replace with statement generator
    print(f"User Score: {user_score}  | Computer Score: {comp_score}")

# end of game
print()
if user_score > comp_score:
    print("The user won")  # replace with statement generator
else:
    print("The computer won")