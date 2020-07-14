```
  ____ ____ ____ ___  _   _ 
  [__  |    |  | |__]  \_/  
  ___] |___ |__| |      |    ᴍᴀᴅᴇ ʙʏ ᴀʟᴘʜᴀʀᴀᴏʜ    

```
# Scopy 
Written in Python3<br />
Collects all valid scopes from hackerone programs<br />
Can collect multiple scopes at once and output their scopes<br />
![Demo](/demo/demo.gif)

# Disclaimer 
CHROMER DRIVER DEPENDANT<br />
This tool only collects in-scope URLS.<br />
"*." is removed from scope text e.g. *.api.example = api.example<br />

## Installation

1) Download [chromedriver](https://chromedriver.chromium.org/downloads) 
4) git clone https://github.com/AkaamS/scopy.git
4) cd scopy
5) Change chromedriver path location in scopy.py
6) python3 scopy.py -h

## Example Usage

Single Program:
```
python3 scopy.py -n NAME
```
List of Programs:
```
python3 scopy.py -n NAME,NAME1,NAME2,NAME3
```
## Options

```
Usage: scopy.py [-n NAME] [-o] [-t TIME] [...]

Optional Args:
    -h                  Displays this message
    -n NAME(s)           Name of program (hackerone.com/NAME)
                        -u NAME,NAME1,NAME2 (Make sure to have no spaces between , )
    -o                  Output only results
    -t TIME             Time to allow javascript to load (Default: 4)
    -s                  Add "https://" to scopes

```
