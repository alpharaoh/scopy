import sys
import warnings
import requests
import time 
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class colours:
    HEADER = "\033[95m"
    COLOUR1 = "\033[94m"
    COLOUR2 = "\033[35m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"

if sys.version_info < (3, 0):
    sys.stdout.write(f"{colours.FAIL}[+] Sorry, this tool only works with Python 3.X\n{colours.ENDC}")
    exit()

class printText:
  ascii = f"""{colours.HEADER}  ____ ____ ____ ___  _   _ 
  [__  |    |  | |__]  \_/   
  ___] |___ |__| |      |    ᴍᴀᴅᴇ ʙʏ ᴀʟᴘʜᴀʀᴀᴏʜ{colours.ENDC}                        
  """
  help = f"""  ____ ____ ____ ___  _   _ 
  [__  |    |  | |__]  \_/  
  ___] |___ |__| |      |    ᴍᴀᴅᴇ ʙʏ ᴀʟᴘʜᴀʀᴀᴏʜ    

Usage: scopy.py [-n NAME] [-o] [-t TIME] [...]

Optional Args:
    -h                  Displays this message
    -n NAME(s)           Name of program (hackerone.com/NAME)
                        -n NAME,NAME1,NAME2 (Make sure to have no spaces between , )
    -o                  Output only results
    -t TIME             Time to allow javascript to load (Default: 4)
    -s                  Add "https://" to scopes
  """

class main:

  def __init__(self):
    self.ttime = 4
    self.show_visuals = True
    self.show_http = False
    self.programs = []

  warnings.filterwarnings("ignore", category=DeprecationWarning)

  def validation(self): #Validate input and program availability

    for i in range(len(sys.argv)):
      if sys.argv[i] == "-o":
        self.show_visuals = False
      elif sys.argv[i] == "-h":
        print(printText.help)
        exit()
      elif sys.argv[i] == "-t":
        if sys.argv[i+1] not in ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"]:
          print(f"{colours.FAIL}[+] Error: Need valid time between 1-15s{colours.ENDC}")
          exit()
        else:
          if sys.argv[i+1] in ["1","2","3"]:
            print(f"{colours.WARNING}[+] Warning: Lower time may result in failure to load scopes{colours.ENDC}")
          self.ttime = sys.argv[i+1]
      elif sys.argv[i] == "-s":
        self.show_http = True
      elif sys.argv[i] == "-n":
        try:
          self.programs = (sys.argv[i+1]).split(",")
        except:
          print(f"{colours.FAIL}[+] Error: Name not specified{colours.ENDC}")
          exit()
        
    if self.show_visuals:
      print(printText.ascii)

    self.ttime = int(self.ttime)
    self.ttime /= 2

    if len(sys.argv) > 1:
      try:
        site = requests.get(f'https://hackerone.com/{self.programs[0]}')
        if (site.status_code) != 200:
          print(f"{colours.FAIL}[+] Error: Program(s) not found{colours.ENDC}")
          exit()
      except:
        print(f"{colours.FAIL}[+] Error: Something went wrong {colours.ENDC}")
    else:
      print(f"{colours.FAIL}[+] Error: Missing argument {colours.ENDC}")
      exit()
    
    #Validated
    self.run()

  def run(self):
    for j in self.programs:
      if self.show_visuals:
        print(f"{colours.COLOUR2}[+] Gathering data for {j}...{colours.ENDC}")
      site = f"https://hackerone.com/{j}"

###################################################################################################

      path = "/home/USER/Documents/chromedriver"             #Please change chrome driver location 

###################################################################################################

      chrome_options = Options()
      chrome_options.add_argument("--headless")
      try:
        driver = webdriver.Chrome(path, options=chrome_options)
      except:
        print(f"{colours.FAIL}[+] Error: Check if chrome driver path is changed in scopy.py {colours.ENDC}")
        exit()

      driver.get(site)
      
      ## 4s threshhold 
      time.sleep(self.ttime) #Allow javascript to load
      if self.show_visuals:
        print(f"{colours.COLOUR2}[+] Loading data...{colours.ENDC}")
      time.sleep(self.ttime)
      ##

      try:
        scopes=[]
        scopes = driver.find_elements_by_xpath("//td[@class='daisy-table__cell table__row--align-top break-word']/div/span/strong")
        if self.show_visuals:
          print(f"{colours.COLOUR1}[+] {len(scopes)} scopes found.{colours.ENDC}")

        if len(scopes) <= 0:
          print(f"{colours.FAIL}[+] Error: Failed to load scopes{colours.ENDC}")

        for i in scopes:
          tmp = i.text
          tmp = tmp.replace("*.", "")
          if " " in tmp:
            pass
          elif self.show_http:
            print(f"https://{tmp}")
          else:
            print(tmp)

      except Exception as e:
        print(f"{colours.FAIL}[+] Error: {e}{colours.ENDC}")
        print(f"{colours.WARNING}[+] Try: Increase threshhold time{colours.ENDC}")

main().validation()
