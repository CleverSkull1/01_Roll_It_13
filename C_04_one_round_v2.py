import random


# functions

def initial_points(which_player):
    """Roll dice twice and return total / if double points apply"""

    double = "no"

    # roll the dice for the user and note if they got double
    roll_one = random.randint(1, 6)
    roll_two = random.randint(1, 6)

    if roll_one == roll_two:
        double = "yes"

    total = roll_one + roll_two
    print(f"{which_player}   - Roll 1: {roll_one} \t| Roll 2: {roll_two} \t| Total: {total}")

    return total, double


def make_statement(statement, decoration):
    """Adds additional characters to the start and end of headings as decoration"""

    ends = decoration * 3
    print(f"\n{ends} {statement} {ends}")


# main starts here..


# Roll the dice for the user and note if they got a double
initial_user = initial_points("User")
initial_comp = initial_points("Computer")

# retrieve user points (first item returned from function)
user_points = initial_user[0]
comp_points = initial_comp[0]

double_user = initial_user[1]

# let the user know if they qualify for double points
if double_user == "yes":
    print("You are eligible for double points if you win")

# assume user goes first
first = "User"
second = "Computer"
player_1_points: int = user_points
player_2_points = comp_points

# if the user has fewer points they start
if user_points < comp_points:
    print("You start because your initial roll was less than the computer\n")

# if the user and computer roll equal points, the user is player 1
elif user_points == comp_points:
    print("The initial rolls were the same, the user starts")

# if the computer has fewer points switch the computer to player 1
else:
    player_1_points, player_2_points = player_2_points, player_1_points
    first, second = second, first

# Loop until there's a winner
while player_1_points < 13 and player_2_points < 13:
    print()
    input("Press <enter> to continue this round\n")

    # first person rolls the die and score is updated
    player_1_roll = random.randint(1, 6)
    player_1_points += player_1_roll

    print(f"{first}: Rolled a {player_1_roll} - has {player_1_points} points")

    # if the first person's score is > 13, end the round
    if player_1_points >= 13:
        break

    # second person rolls the die and score is updated
    player_2_roll = random.randint(1, 6)
    player_2_points += player_2_roll

    print(f"{second}: Rolled a {player_2_roll} - has {player_2_points} points")

    print(f"{first}: {player_1_points}   |  {second}: {player_2_points}")

print()

# end of round

# associate player points with either the user or computer
user_points = player_1_points
comp_points = player_2_points

# switch the user and computer points if the computer went first

# decide winner
if user_points > comp_points:
    winner = "user"
else:
    winner = "computer"

round_feedback = f"The {winner} won."

# double user points if eligible
if winner == "user" and double_user == "yes":
    user_points = user_points * 2

# output round results
make_statement("Round Results", "=")
print(f"User Points: {user_points}  |   Computer Points: {comp_points}")
print(round_feedback)
print()
