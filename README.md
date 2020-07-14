 # Scopy 
MADE BY ALPHAROAH

Collects all valid scopes from hackerone programs
Can collect multiple scopes at once and output their scopes 

DISCLAIMER: This tool only collects in-scope URLS.


Usage: scopy.py [-u NAME] [-o] [-t TIME] [...]

Optional Args:
    -h                  Displays this message
    -u URL(s)           Name of program (hackerone.com/NAME)
                        -u NAME,NAME1,NAME2 (Make sure to have no spaces between , )
    -o                  Output only results
    -t TIME             Time to allow javascript to load (Default: 4)
    -s                  Add "https://" to scopes
  
