import easygui
#9/9/26 Full preset monsters list.
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

# 15/9/26 This is my main menu code.
def main_menu():
    action = easygui.buttonbox("What Would you like to do?", choices=['Add Monsters','Delete Monsters','Print Monsters','Quit'], title="Main Menu")
    if action == "Add Monsters":
        add_this()
    elif action == "Delete Monsters":
        delete()
    elif action == "Print Monsters":
        print_menu()
    else:
        easygui.msgbox("Thank you for playing. See you next time!!!", title="Goodbye")
        quit()

# 24/9/26 This is my add code. The monsters name has a forced capital at the start.
def add_this():
    mname = easygui.enterbox("\n\nEnter Monster name: ", title="Monster name")
    ID = mname.capitalize()
    easygui.msgbox(f"Added a capital letter. Result: {ID}", title="Added a capital")
    monsters[ID] = {}
    #29/9/26 User can only enter a number inbetween 1 and 25. No more, no less.
    mstrength = easygui.integerbox("Enter Monsters strength: (1 - 25)", title="Monster strength", lowerbound=1, upperbound=25)
    monsters[ID]["strength"] = mstrength

    mspeed = easygui.integerbox("Enter Monsters speed: (1 - 25)", title="Monster speed", lowerbound=1, upperbound=25)
    monsters[ID]["speed"] = mspeed

    mstealth = easygui.integerbox("Enter Monsters stealth: (1 - 25)", title="Monster stealth", lowerbound=1, upperbound=25)
    monsters[ID]["stealth"] = mstealth

    mcunning = easygui.integerbox("Enter Monsters cunning: (1 - 25)", title="Monster cunning", lowerbound=1, upperbound=25)
    monsters[ID]["cunning"] = mcunning

    easygui.msgbox(monsters)

 # 24/9/26 This code asks if you would like to add a new monster.
    add = easygui.buttonbox("Would you like to add another Monster?", choices=("Yes", "No"), title="Add Another")
    if add == "Yes":
        easygui.msgbox("Let's add another Monster!", title="Add another monster")
        add_this()
    else:
        easygui.msgbox("Thank you for adding another Monster!", title="Thank you")
        main_menu()

# 29/9/26 This is the code to delete a monster. You can now delete all monsters or just one
def delete():
    choose = easygui.buttonbox("What would you like to delete?", choices=("One monster", "All monsters"), title="Choose an option")
    if choose == "One Monster":
        kill = easygui.enterbox("Enter the name of the monster you want to delete:", title="Delete monster")
        if kill.capitalize() in monsters:
            corrected_input = kill.capitalize()
            easygui.msgbox(f"You might of forgot a capital letter, so I added it for you. Result: {corrected_input}", title="Added a capital")

            monsters.pop(corrected_input)
            print(monsters)
            main_menu()
        else:
            easygui.msgbox("That monster does not exist!!", title="Unknown monster")
            main_menu()
    else:
        monsters.clear()
        print(monsters)
        easygui.msgbox("All monsters have been deleted", title="Clean plate")
        main_menu()
# 28/9/26 This is the code to print all monsters.
def print_menu():
    if not monsters:
        easygui.msgbox("There are no Monsters Left!", title="Clean plate")
        main_menu()
    else:
        for monsters_id, monsters_info in monsters.items():
            print("\nMonster ID:", monsters_id)

            for key in monsters_info:
                print(key + ":", monsters_info[key])
    main_menu()


main_menu()