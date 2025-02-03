from datetime import datetime ;from datetime import date ;import time ;driveselect = "C";t = time.localtime();current_time = time.strftime("%d-%m-%Y %H:%M:%S");cmdrepeat = True ; time = (time);import sys; desktop_repeat = True; search = False; settings = False;
time.sleep(5);print("Starting up System...")
time.sleep(5);print("Checking for Updates...")
time.sleep(10);print("Command Prompt Loaded!")
time.sleep(3)
def process_startOS():
    mode = "startup"
    print()
    print("\033[1;32m  _____                         ___  ____  ")
    print(" |_   _|__  _ __  _ __   ___   / _ \/ ___| ")
    print("   | |/ _ \| '_ \| '_ \ / _ \ | | | \___ \ ")
    print("   | | (_) | |_) | |_) | (_) || |_| |___) |")
    print("   |_|\___/| .__/| .__/ \___/  \___/|____/ ")
    print("           |_|   |_|                        ")
    print()
    time.sleep(2)
    print("Loading...")
    time.sleep(5)
    mode = "login"
    print()
    name_acc = input("\033[1;32mPlease enter your username for sign-in:    \n");login_repeat = "a"
    while login_repeat == "a":
        if name_acc == "":
            name_acc = input("Please try again. \n")
        elif name_acc == "toppo":
            login_repeat = "b"
        else:
            print("The username is toppo.")
            name_acc = input("Please try again. \n")
    print()
    name_pass = input("\033[1;32mPlease enter your password for sign-in:   \n"); login_repeat = "c"
    while login_repeat == "c":
        if name_pass == "":
            name_pass = input("Please try again. \n")
        elif name_pass == "1234":
            login_repeat = "d"
        else:
            print("The password is 1234.")
            name_pass = input("Please try again. \n")
    print()
    print("Welcome!")
    time.sleep(2)
    mode = "desktop"
    while desktop_repeat == True:
         if mode == "desktop":
               print("\033[1;32m")
               print(">My Computer");print(">Settings");print(">iSurf");print(">Recycle Bin \n");print(">Start")
               sel = input()
               if sel == "isurf":
                    search = True
                    mode = "iSurf"
                    print("\033[1;34m")
                    print(" _ ____              __ ")
                    print("(_) ___| _   _ _ __ / _|")
                    print("| \___ \| | | | '__| |_ ")
                    print("| |___) | |_| | |  |  _|")
                    print("|_|____/ \__,_|_|  |_|  ")
                    print()
                    print("Version 0.1"); print("Copyright @ Toppo 2025 - 2025 \n")
                    while search == True:
                         search_ans = input("Search: ")
                         if search_ans == "exit":
                            search = False
                            mode = "desktop"
                         elif search_ans == "toppo":
                             print()
                             print(":~!~~!~^7?????7!~:~~^^^~!7?7!!7??J?:....::.......:");print("~!~::::.:~!??????777!!~^~~~!!!?JYYY7??!!7!^:::::..");print("???7!!7!!!7???JJJ????77!~~~^7JYY555Y555J!!:..^^...");print("??????????JJYJJJJJJJJ??7!!~!YGGB#&&#BBGY7~^^!!~~~~");print("777?????????YJP5JJJJJJJ??7!!5GB#&&&##BG5YJ??JJYYYJ")
                             print("77777777??777???5PYJYYJJJJY5GGB#&&&##BBGP5YYJJJJJ?");print("77777777777!7?77Y55##P5P5PBB#B##&@@&####BGYJJ!~~~!");print("!!!!!!!!777777????JYYP##GG#BB#&&@@@@&&##PYJJJ77777");print("!!!!~~^~?~!777?77????JJ?5##GY555PP#@&&@@&#PYJ?????");print("~~~~~~~~~~YJ!7?7???7???JB#BJ?????Y#@PY5G#@@&GJ7777");print("~~~~~~!!!!775P??J?7???Y###J?????J#@GJ???JG@@@5!!77");print("^^~~~!~~!7!7J?YBBY5P5JG#B5YYYJJJB@BJ????Y&@@G!~~!~");print("^^^^~!!!!!7??77?7P##PB&&PG######@&5YJ??Y#@@B!~^^^~")
                             print("!!!?Y7?????????JJJJYB&&GJJJYY5#@&B###G5B@@#!^^^:^~");print("77777JPJ??????????JP##GJ?????5&&YJJYP#&@@&5???JJ??");print("???????JGPJYYJ????P&&BJ?????5&&5????JG@@@GPPPPPPPP");print("YYJJJJJYYYG#BPGGP5B#BPPPPP55#@P????JP@@@GYYYYYY555");print("5555555555555B#BG#&&G#&&@@@@@@BP5J?5&@@GJJJJJJJJJJ");print("GGGGGGGGPPPPPPPPPGPPPPPPPPGGB#&@@#G&@@BYJJJYYYYYYY");print("BBBGGBGGGGGGGGPPPPPPPPPPPPP555PG#&@@@#PP5PPPPPPPPP");print("GGGPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPGB&&GPPPPPPPGPGGG");print("PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPGGPPPPPPGGGGGGG");print("PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP");print("GGGPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPGGG")
                             print()
                         elif search_ans == "egg":
                             print()
                             print(" . ..  .   ... .");print(". .  ..  . ...  .  .");print(". ........:..... ...");print("  ........::--.  .. ");print(" .......::::--=. . .");print(".......::::--==+... ");print(" ....:::::---=+*-.. ");print(" .:::::::--==+**+.  ");print("..:::::----==+**= ..");print("..::::----==++**-. .");print(". .:::---====++=..  ");print("....::-----====.... ");print(" .. .:-:---=======:.");print("  . ..:-=++++=--:.. ");print(".. . . . ..   .... .");print(".  ..   . ..    ")
                             print()
               elif sel == "start":
                    mode = "start"
                    print("\n>Shutdown");print(">Restart")
                    sel = input()
                    if sel == "shutdown":
                         print("\nAre you sure?")
                         print("[Y]es / [N]o");option1 = input()
                         if option1 == "y":
                             print("\nShutting down...")
                             time.sleep(5)
                             print("It is now safe to turn off your computer.")
                             exit()
                         elif option1 == "n":
                             mode = "desktop"
                         else:
                             print("Invalid option.")
                    elif sel == "restart":
                         print("\nAre you sure?")
                         print("[Y]es / [N]o");option2 = input()
                         if option2 == "y":
                            process_startOS()
               elif sel == "settings":
                    mode = "settings"
                    settings = True
                    print("\033[1;37m")
                    while settings == True:
                        print(">About")
                        print(">Personalization") 
                        sel = input()
                        if sel == "about":
                            print()
                            print("ToppoOS version 0.1")
                            print("Copyright @ Toppo 2025-2025. All rights reserved.")
                            print()
                        elif sel == "exit":
                            mode = "desktop"
                            settings = False
while cmdrepeat == True:
    if driveselect == "C":
        print()
        command = input("C:/")
        if command == "toppo":
            process_startOS()
        if command == "about":
            print()
            print("\033[1;33mToppo's CMD Prompt Version 0.2")
        elif command == "time":
            print()
            print(current_time)
        elif command == "help":
            print()
            print("about = Shows the version you're currently using.")
            print("time = Shows the current time. (doesn't update though!)")
            print("exit = Exits the program.")
            print("list par = Lists the partitons currently on the disk.")
            print("info = Shows the name and size of the drive.")
            print("cd [drive]:/ = Changes the current drive to another drive.")
            print("os = Shows information of the operating system you're currently using.")
            print("list dir = Lists the files currently in the drive.")
        elif command == "exit":
            exit()
        elif command == "cd d:/":
            driveselect = "D"
        elif command == "list par":
            print()
            print(" Name      Size    Type")
            print("--------------------------")
            print("Par 1    511000MB  GPT")
            print("Par 2     1000MB  System")
        elif command == "info":
            print()
            print("Western Digital Teal SSD 512GB")
        elif command == "cd a:/":
            print()
            print("Floppy disk not found.")
        elif command == "":
            pass
        elif command == "os":
            print()
            print("\033[1;33mWindows 11 Home Singe Language 24H2 (26100.2605)")
        elif command == "list dir":
            print()
            print( " Name       Modified Date")
            print("----------------------------")
            print("system32      12-09-1997")
            driveselect = "DirSel"
        else:
            print()
            print("Unknown command.")
    elif driveselect == "D":
        print()
        command2 = input("D:/")
        if command2 == "cd c:/":
            driveselect = "C"
        elif command2 == "list par":
            print()
            print(" Par      Size     Type")
            print("--------------------------")
            print("Par 1    16000MB   NTFS")
        elif command2 == "info":
            print()
            print("Name: SanDisk E45 16GB")
        elif command2 == "help":
            print()
            print("list par = Lists the partitons currently on the disk.")
            print("info = Shows the name and size of the drive.")
            print("cd [drive]:/ = Changes the current drive to another drive.")
            print("os = Shows information of the operating system you're currently using. (Only works if C:/ is selected!)")
        elif command2 == "":
            pass
        elif command2 == "cd a:/":
            print()
            print("Floppy disk not found.")
        else: 
            print()
            print("Unknown command.")
    elif driveselect == "DirSel":
        print()
        filesel = input("C:/")
        if filesel == "system32":
            print()
            print("System32 has been successfully selected.");time.sleep(2)
            print()
            print("What do you want to do with it?")
            print()
            print("[D]elete");option = input()
            if option == "D" or "d":
                print()
                print("Are you sure?")
                print("")
                print("[Y]es / [N]o");option2 = input()
                if option2 == "Y" or "y":
                 print()
                 print("Deleting files..."); time.sleep(10)
                 print()
                 print("Done!")
                 filesel = ""
                 driveselect = "C"
                elif option2 == "N" or "n":
                 driveselect = "C"
            


