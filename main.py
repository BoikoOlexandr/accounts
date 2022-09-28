from acc.Command import Command

while True:
    command = input("""
    This is account system
    Enter 1 for add somebody
    Enter 2 for search somebody
    Enter q fo quit
    """)
    if command.lower().strip() in ["q", "й"]:
        print("See you later")
        exit(0)
    try:
        command_code = int(command)
        if not 0 < command_code <= 2: raise ValueError
        Command().set_command(command_code)
    except ValueError:
        print("Enter number dude")


