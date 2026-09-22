import easygui
#9/9/26 Full preset monsters list
monsters = {"Stoneling":{"Strength": 7,
                         "Speed": 1,
                         "Stealth": 25,
                         "Cunning": 15,},
            "Vexscream":{"Strength": 1,
                         "Speed": 6,
                         "Stealth": 21,
                         "Cunning": 19,},  
            "Dawnmirage":{"Strength": 5,
                         "Speed": 15,
                         "Stealth": 18,
                         "Cunning": 22,},
            "Blazegolem":{"Strength": 15,
                         "Speed": 20,
                         "Stealth": 23,
                         "Cunning": 6,},
            "Websnake":{"Strength": 7,
                         "Speed": 15,
                         "Stealth": 10,
                         "Cunning": 5,},  
            "Moldvine":{"Strength": 21,
                         "Speed": 18,
                         "Stealth": 14,
                         "Cunning": 5,},
            "Vortexwing":{"Strength": 19,
                         "Speed": 13,
                         "Stealth": 19,
                         "Cunning": 2,},
            "Rotthing":{"Strength":16,
                         "Speed": 7,
                         "Stealth": 4,
                         "Cunning": 12,},  
            "Froststep":{"Strength": 14,
                         "Speed": 14,
                         "Stealth": 17,
                         "Cunning": 4,},
            "Wispghoul":{"Strength": 17,
                         "Speed": 19,
                         "Stealth": 3,
                         "Cunning": 2,}
                         }

def main_menu():
    action = easygui.buttonbox("What Would you like to do?", choices=['Add Monsters','Delete Monsters','Print Monsters','Quit'], title="Main Menu")
    if action == "Add Monsters":
        add_this()
    elif action == "Delete Monsters":
        delete()
    elif action == "Print Monsters":
        print_menu()
    else:
        easygui.msgbox("Thank you for playing. See you next time!!!")
        quit()

#working add menu. Thinking of adding a forced capital to the monsters name
def add_this():
    ID = easygui.enterbox("\n\nEnter Monster name: ")
    monsters[ID] = {}

    mstrength = easygui.integerbox("Enter Monsters strength: ")
    monsters[ID]["strength"] = mstrength

    mspeed = easygui.integerbox("Enter Monsters speed: ")
    monsters[ID]["speed"] = mspeed

    mstealth = easygui.integerbox("Enter Monsters stealth: ")
    monsters[ID]["stealth"] = mstealth

    mcunning = easygui.integerbox("Enter Monsters cunning: ")
    monsters[ID]["cunning"] = mcunning

    easygui.msgbox(monsters)
# need to fix unexpected output issue
    while True:
        add = easygui.enterbox("Would you like to add another Monster? (Y/N):")
        if add.capitalize() == "Y":
            print("Let's add another Monster!")
            add_this()
        elif add.capitalize() == "N":
            print("Thank you for adding another Monster!")
        main_menu()

def print_menu():
    try:
        for monsters_id, monsters_info in monsters.items():
            print("\nMonster ID:", monsters_id)

            for key in monsters_info:
                print (key + ":", monsters_info[key])
    except:
        print("There are no Monsters Left!")
    main_menu()




main_menu()