import os
import sys
import re
import shutil


def RenameFiles(go = False):
    file_list = []
    season_list = []
    for file in os.listdir():
        if "Season" not in file:
            try:
                ep_num = re.search(re.compile(r"^\d+"), file).group()
                if len(ep_num) == 4:
                    ep_num = "s" + ep_num[0:2] + "e" + ep_num[2:]
                elif len(ep_num) == 3:
                    ep_num = "s0" + ep_num[0] + "e" + ep_num[1:]
                elif len(ep_num) == 2:
                    ep_num = "s01e" + ep_num
                elif len(ep_num) == 1:
                    ep_num = "s01e0" + ep_num

                try:
                    ep_name = file[re.search(re.compile(r'^\d+'), file).span()[1]+3:]
                except AttributeError:
                    break
                file_list.append(show_name + " - " + ep_num + " - " + ep_name)
                # Find out which seasons are accounted for in this directory.
                if ep_num[1:3] not in season_list:
                    season_list.append(ep_num[1:3])
                if go:
                    os.rename(file, show_name + " - " + ep_num + " - " + ep_name)
            except AttributeError:
                pass
    return file_list, season_list


def MoveFiles():
    moveRegex = re.compile(r" - s\d\de\d\d - ")
    for file in os.listdir():
        if "Season" not in file:
            if re.search(moveRegex, file):
                shutil.move(file, "Season "  + re.search(moveRegex, file).group()[4:6])


try:
    path = input("Enter the directory containing episode files: ")
    os.chdir(path)

    # If working directory is e.g. "Z:\Shows\The Office (Seasons 5-6)", return show_name of "The Office" by splitting out the last "\" and the first "("
    show_name = os.getcwd().split("\\")[-1].split(" (")[0]
    # Ask user to verify correct directory and show name before proceeding.
    proceed = input("If show in " + os.getcwd() + " is called " + show_name + ", enter Y to proceed: ")
    if proceed.lower() not in ["y"]:
        print("Let's try the Unix way then.")
        proceed = ""
        show_name = os.getcwd().split("/")[-1].split(" (")[0]
        proceed = input("If show in " + os.getcwd() + " is called " + show_name + ", enter Y to proceed: ")
        if proceed.lower() not in ["y"]:
            print("Aborting.")
            sys.exit()

    # Call the Fileloop function with 0 for verification, 1 for execution.
    file_list, season_list = RenameFiles(0)

    print("Printing list of new file names:")
    for f in file_list:
        print("      " + f)
    # Ask user to verify list of new file names before proceeding.
    proceed = input("If new file names look accurate, enter Y to proceed: ")
    if proceed.lower() not in ["y"]:
        print("Aborting.")
        sys.exit()
    proceed = ""
    # Ask user to verify the last season before proceeding.
    try:
        proceed = input("If the last season is Season " + str(int(max(season_list))) + " and you wish to execute the name changes, enter Y to proceed: ")
    except ValueError:
        print("No max season found. Are files named correctly?")
        print("Aborting.")
        sys.exit()
    if proceed.lower() not in ["y"]:
        print("Aborting.")
        sys.exit()
    proceed = ""
    for x in range(1, int(max(season_list))+1):
        try:
            os.mkdir("Season " + "{:02d}".format(x))
        except:
            print("Directory creation failed.")
            print("Aborting.")
    RenameFiles(True)
    MoveFiles()

except FileNotFoundError:
    print("Please enter a valid directory.")
    print("Aborting.")
except OSError:
    print("Please enter a valid directory, or close the files to be renamed.")
    print("Aborting.")

sys.exit() 
