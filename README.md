# plexnamer

## Why?
For years I've been using my own personal TV episode naming scheme, which worked perfectly well, until I met Plex, and Plex told me they wanted everything to be this and that way, so that my server can gather up metadata and make everything look nice and official. So rather than manually go through my entire collection, renaming files one by one, I wrote a script that should be intelligent enough to rename the files as Plex sees fit. The catch is, it only works if your files are already named the way mine were. The scope of this project is rather narrow.

## Instructions
- Install: Download main.py. No additional dependencies required.
- From a command line: `python3 main.py "\Path\to\show\" "Name of Show"`

For example, if I have a directory called "The Office (Seasons 1-2)", and it contains files "101 - Pilot.mp4", "102 - Whatever Ep2 Is Called.mp4", "205 - This One Too.mp4," then I would run:

`python3 main.py "The Office (Seasons 1-2)" "The Office"`

The script will then present a list of what the newly-formatted files would look like and asks the user to enter "go" to confirm the changes. It will then create a number of Season XX directories based on the last season found, so that the final directory will look like this:
- The Office (Seasons 1-2)
  - Season 01
    - The Office - s01e01 - Pilot.mp4
    - The Office - s01e02 - Whatever Ep2 Is Called.mp4
  - Season 02
    - The Office - s02e05 - This One Too.mp4

You then just need to rename the directory "The Office (Seasons 1-2)" to "The Office" and move it to wherever Plex looks for your TV shows.

## TO DO LIST
1. DONE: Make program not care whether path is Linux-like or Windows-like (maybe replace all "\" with "/" since Windows does not seem to care which way the slash leans?)
2. BUG FIXED: Realized that a global replace of "\" in the directory messes with escape characters in Linux directory names, so give alternate option to enter name manually.
3. DONE: Allow program to accept path and show name as command line args
4. DONE: Reduce number of user confirmations to 1

## FUTURE
Eventually I'd like to write the script to detect various episode naming schemes based on multiple regexes, and then go from there, to broaden the scope of the project. That way, people who have large TV show collections might be able to use my script to rename their files per Plex standards regardless of their file name preferences. For example:
- "101 - Pilot.mp4"
- "0101 - Pilot.mp4"
- "s01.e01 - Pilot.mp4"
- "s1e1 - Pilot.mp4"
- "Season 1 Episode 1 - Pilot.mp4"
- "Season 01 Episode 01 - Pilot.mp4"
- "The Office - 101 - Pilot.mp4"
- etc.