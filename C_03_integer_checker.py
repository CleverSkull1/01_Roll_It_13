# Choose the game goal as a value that's > 13

error = "Please enter an integer more than or equal to 13. "

while True:
    try:
        game_goal = int(input("Choose a game goal "))

        if game_goal < 13:
            print(error)
        else:
            print(f"Game goal: {game_goal} ")
            break
    except ValueError:
        print(error)


