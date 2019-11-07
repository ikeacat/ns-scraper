import argparse
import urllib.request
import sys

# Vars & other stuff
filesave = "nsdownload.html"

mainParser = argparse.ArgumentParser(description="Process main commands")
mainParser.add_argument('-nation', help='Define the Nation you would like to scrape from.', type=str)
mainParser.add_argument('-password', help='(Optional), Enter the password, if you would like to get something that is private (Ex. Issues), Command Ex: -password "insertpasshere"')
mainParser.add_argument('-saveToFile', help='(Optional), Save to a specific file. Is not compatible with "--saveOutputToSTDOUT". (EX: -saveToFile "downfile")', type=str)
mainParser.add_argument('-saveOutputToSTDOUT', help='(Optional), print output to STDOUT at end. Put (without quotes) "True" or "False" (CaSe SeNsItIvE!). Is not compatible with "-saveToFile", default is False')

userDefArgs = mainParser.parse_args()

if(userDefArgs.nation == None):
  print("ERROR: Nation not defined. Please define a nation using '-nation'. Exiting.")
  raise SystemExit
else: pass

print("Nation defined. Proceeding")

if(userDefArgs.saveOutputToSTDOUT != None):
  filesave = sys.stdout
else:
  if(userDefArgs.saveToFile != None):
		if(userDefArgs.saveToFile is str):
    	filesave = userDefArgs.saveToFile
		elif(userDefArgs.saveToFile is not str):
