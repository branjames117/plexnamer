import os
import sys

running = True

while running:
    try:
        path = input("\nCopy and paste the full directory: ")
        os.chdir("Z:\Brandon\TestDir")
        show_name = input("\nEnter the name of the show: ")
        for f in os.listdir():
            file_name, file_ext = os.path.splitext(f)
            episode_number, episode_name = file_name.split(" - ")
            if len(episode_number) == 3:
            	enumb = "s0" + episode_number[0] + "e" + episode_number[1:]
            if len(episode_number) == 4:
            	enumb = "s" + episode_number[0:2] + "e" + episode_number[2:]
            os.rename(f, "{} - {} - {}{}".format(show_name, enumb, episode_name, file_ext))
        quit = input("Quit? ")
        if quit == "y" or "yes" or "Y":
        	sys.exit()    
    except FileNotFoundError:
        print("FileNotFoundError - Please enter a valid directory.")
    except OSError:
        print("OSError - Please enter a valid directory, or close the files to be renamed.")
