from char_values import PC


def input_level():
    print("What level is your character?")
    try:
        inp = str.lower(input())
        if inp == "exit":
            quit()
        inp = int(inp)
        if inp >= 1 and inp <= 20:
            PC.lvl = inp
            print(f"Your character is level {PC.lvl}.")
            return
        else:
            print("Please enter a number between 1 and 20.")
            input_level()
    except ValueError:
        print("Please enter a number between 1 and 20.")
        input_level()