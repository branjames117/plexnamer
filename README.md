# plexnamer

This is a script I wrote for my specific file naming situation. For years I had my own personal TV episode naming scheme, which worked perfectly well, until I met Plex, and Plex
told me they wanted everything to be this and that way, so that my server can gather up metadata and make everything look nice and official. So rather than manually go through my
entire collection, renaming files one by one, I wrote a script that should be intelligent enough to rename the files as Plex sees fit. It asks for confirmation along the way,
because some shows have 100s of episodes and the batch file renaming is irreversible and can be a pain to fix if all the files get renamed incorrectly. I know.

Install: Download main.py.
Run: python3 main.py
Instructions:
    1) Enter path to episode files (like C:\Shows\The Office (Seasons 1-2)
    2a) If on Windows, the show name should be pulled, confirm by entering y.
        2b) If on Linux, show name will still show path due to difference between \ and / in path. So enter n to reformat, then y to confirm.
    3) View list of files and see they look all right, then confirm by entering y. Only filenames which BEGIN with 1-4 digits will be processed.
    4) Confirm the # of the last season is right by entering y. This is the final confirmation step before file renaming, directory creation, and file moving takes place.
Result:
    Directory "The Office (Seasons 1-2)" containing files "101 - Pilot.mp4", "102 - Whatever Ep2 Is Called.mp4", "205 - This One Too.mp4" should be reformatted according to
    Plex standard:
        The Office (Seasons 1-2)
            Season 01
                s01e01 - Pilot.mp4
                s01e02 - Whatever Ep2 Is Called.mp4
            Season 02
                s02e05 - This One Too.mp4
    5) Rename directory to just be the show name ("The Office").

TO DO LIST:
[X] Easy: Make program not care whether path is Linux-like or Windows-like (maybe replace all "\" with "/" since Windows does not seem to care which way the slash leans?)
    [X] Bug: Realized that a global replace of "\" messes with escape characters in Linux directory names, so give alternate option to enter name manually.
[X] Easy: Allow program to accept path and show name as command line args
[X] Easy: Reduce number of user confirmations to 1
[ ] Lofty: Give program ability to reformat file naming schemas that are unlike the one I use (with regex), like:
        Show Name Already Here - 101 - Episode.avi
        s01e01 - Episode.mp4
        Ep. 05 - Episode 5 Sucks.mp4
        etc.