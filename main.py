#!/usr/bin/python3

import os
import sys
import re
import shutil


def renameFiles(go = False):
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


def moveFiles():
    moveRegex = re.compile(r" - s\d\de\d\d - ")
    for file in os.listdir():
        if re.search(moveRegex, file):
            shutil.move(file, "Season "  + re.search(moveRegex, file).group()[4:6])


def main(path, show_name):
    try:
        os.chdir(path)

        # Call the Fileloop function with 0 for verification, 1 for execution.
        file_list, season_list = renameFiles()

        print("Printing list of new file names:")
        for f in file_list:
            print("      " + f)
        # Ask user to verify list of new file names before proceeding.
        try:
            proceed = input("If new file names look accurate, and Season " + str(int(max(season_list))) + " is the last season, enter go: ")
        except ValueError:
            print("Error: No season info found. Are files named correctly (e.g. 0102 - Episode Name.mp4)?")
            sys.exit()
        if proceed.lower() != "go":
            print("Error: User permission not granted.")
            sys.exit()
        proceed = ""

        for x in range(1, int(max(season_list))+1):
            try:
                os.mkdir("Season " + "{:02d}".format(x))
            except:
                print("Error: Directory creation failed.")
        renameFiles(True)
        moveFiles()

    except FileNotFoundError:
        print("Error: Please enter a valid directory.")
        print("Syntax: python3 main.py 'C:\\Path' 'Name of Show'")
    except OSError:
        print("Syntax: Please enter a valid directory, or close the files to be renamed.")
        print("Syntax: python3 main.py 'C:\\Path' 'Name of Show'")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Error: Incorrect number of arguments given.")
        print("Syntax: python3 main.py 'C:\\Path' 'Name of Show'")
        sys.exit()
    if not os.path.isdir(sys.argv[1]):
        print("Error: Invalid path argument. Path must exist.")
        print("Syntax: python3 main.py 'C:\\Path' 'Name of Show'")
        sys.exit()
    if os.path.isdir(sys.argv[2]):
        print("Error: Second argument should not be path, but rather the name of the show.")
        print("Syntax: python3 main.py 'C:\\Path' 'Name of Show'")
        sys.exit()
    path = sys.argv[1].replace("\\", "/")
    show_name = sys.argv[2]
    main(path, show_name)