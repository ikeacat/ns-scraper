import argparse
import urllib.request

# Vars & other stuff
filesave = "nsdownload.html"

mainParser = argparse.ArgumentParser(description="Process main commands")
mainParser.add_argument('-nation', help='Define the Nation you would like to scrape from.', type=str)
mainParser.add_argument('-password', help='(Optional), Enter the password, if you would like to get something that is private (Ex. Issues), Command Ex: -password "insertpasshere"')
mainParser.add_argument('-saveToFile', help='(Optional), Save to a specific file. (EX: -saveToFile "downfile")')
mainParser.add_argument('--saveOutputtoSTDOUT', help='(Optional), print output to STDOUT at end. Please append to end.')

userDefArgs = mainParser.parse_args()

if(userDefArgs == ""):
  print("ERROR: Nation not defined. Please define a nation using '-nation'. Exiting.")
  raise SystemExit
else: pass

print("Nation defined. Proceeding")
