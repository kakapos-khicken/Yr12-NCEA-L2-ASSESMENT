import easygui

combos = {"Value":
    {"Beef burger": "5.69",
    "Fries": "$1.00",
    "Fizzy drink": "$1.00",},
    "Cheezy":
    {"Cheeseburger": "$6.69",
    "Fries": "$1.00",
    "Fizzy drink": "$1.00",},
    "Super":
    {"Cheeseburger": "$6.69",
     "Large fries": "$2.00",
     "Smoothie": "$2.00",}}

def main_menu():
    action = easygui.buttonbox("what do you want?", choices=['add','del','print','exit'])
    if action == "add":
        add_this()
    elif action == "del":
        delete()
    elif action == "print":
        print_menu()
    else:
        quit()

def add_this():
    ID = easygui.enterbox("\n\nEnter combo ID:")
    combos[ID] = {}

    burger = easygui.enterbox("Enter burger name:")
    bprice = easygui.integerbox("Enter burger price: $")
    combos[ID]["burger"] = burger, bprice

    fries = easygui.buttonbox("Choose fries size:", choices= ["Small", "Medium", "Large", "Extra Large" ] )
    fprice = easygui.integerbox("Enter fries price: $")
    combos[ID]["fries"] = fries, fprice

    drink = easygui.enterbox("Enter drink type:")
    dprice = easygui.integerbox("Enter drink price: $")
    combos[ID]["drink"] = drink, dprice

    easygui.msgbox(combos)

    while True:
        add = easygui.enterbox("Would you like to add another combo? (Y/N):")
        if add.capitalize() == "Y":
            print("Let's add another combo!")
            add_this()
        elif add.capitalize() == "N":
            print("Thank you for your order!")
            main_menu()

def delete():
    kill = easygui.enterbox("this is my delete code. what do you want to delete?")
    if kill.capitalize() in combos:
        # need to figure out how to stop kill from crashing code
        formatted_input = kill.capitalize()
        easygui.msgbox(f"Result: {formatted_input}")

        combos.pop(formatted_input)
        print(combos)
        main_menu()
    else:
        easygui.msgbox("ID doesn't exist")
        main_menu()

def print_menu():
    try:
        for combos_id, combos_info in combos.items():
            print("\nCombo ID:", combos_id)

            for key in combos_info:
                print (key + ":", combos_info[key])
    except:
        print("There are no combos in the menu")
    main_menu()
# mainmenu() line 75 causes issues on line 21 delete() & combos.pop(kill)
# keyerror pops up on any text entered that is not on the combos list.
main_menu()
# ask the notorious kp to help fix my issue