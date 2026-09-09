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
        quit()

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