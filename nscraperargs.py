import argparse
import sys
import requests
import json

# Vars & other stuff
filesave = "nsdownload.xml"

def listCategories(ppb):
    if(ppb == "public"):
	    print("Public Categories:")
	    sys.stdout.write("animal\nbanner\nbanners - returns a list of Rift banners that should be displayed: the nation's primary banner (if any) is always listed first, with the remainder in random order. Banner codes can be converted into image URLs by prepending /images/banner           s/ and appending .jpg. \ncapital\ncategory\ncrime\ncurrency\ncustomleader\ncustomcapital\ncustomreligion\ndbid\ndeaths\ndemonym\ndispatches\ndispatchlist\nendorsements\nfactbooks\nfactbooklist\nfirstlogin\nflag\nfounded\nfoundedtime\nfreedom\nfullname\ngavote\ngdp\ngovt\ngovtdesc\ngovtpriority\nhappenings\nincome\nindustrydesc\ninfluence\nlastactivity\nlastlogin\nleader\nlegislation\nmajorindustry\nmotto\nname\nnotable\npolicies\npoorest\npopulation\npublicsector\nrcensus\nregion\nreligion\nrichest\nscvote\nsectors\nsensibilities\ntax\ntgcanrecruit\ntype\nwa\nwabadges\nwcensus\n\n")
    if(ppb == "private"):
        print("Private Categories: (Requires -password argument with correct password!)")
        sys.stdout.write("dossier (Note!: Returns only new, unread dossier notices & notices less than 48 hours! keep this in mind.)\nissues (Note: Returns ALOT!)\nissuesummary\nnextissue\nnextissuetime\nnotices\nping (Will just keep a nation from ceasing to exist from inactivity)\nrdossier (same note as dossier)\nunread")

def dataaccess(data):
    if(data == "password"):
        if(nationpassword != None):
            return nationpassword
# Main
mainParser = argparse.ArgumentParser(description="Process main commands")
mainParser.add_argument('-nation', help='Define the Nation you would like to scrape from.', type=str)
mainParser.add_argument('-password', help='(Optional), Enter the password, if you would like to get something that is private (Ex. Issues), Command Ex: -password "insertpasshere"')
mainParser.add_argument('-saveToFile', help='(Optional), Save to a specific file. Is not compatible with "--saveOutputToSTDOUT". (EX: -saveToFile "downfile")', type=str)
# mainParser.add_argument('-saveOutputToSTDOUT', help='(Optional), print output to STDOUT at end. Put (without quotes) "True" or "False" (CaSe SeNsItIvE!). Is not compatible with "-saveToFile", default is False')
mainParser.add_argument('-category', help='Choose the category, put in double quotes NOT SINGLE QUOTES', default="")
mainParser.add_argument('-listCategories', help='(Optional) List the categories avaliable. use public or private after to view either public or private categories', type=str)

userDefArgs = mainParser.parse_args()

#List categories
if(userDefArgs.listCategories != None):
    if(userDefArgs.listCategories == "public"):
        listCategories("public")
        raise SystemExit
    elif(userDefArgs.listCategories == "private"):
        listCategories("private")
        raise SystemExit
    else:
        print("Use public or private for this arg, or dont define it at all.")
        raise SystemExit

#Check for password
if(userDefArgs.password != None):
    nationpassword = userDefArgs.password
    print("Password defined, proceeding.")
elif(userDefArgs.password == None):
    nationpassword = None
    print("No password defined, still proceeding.")

#Check for nation
if(userDefArgs.nation == None):
	print("ERROR: Nation not defined. Please define a nation using '-nation'. Exiting.")
	raise SystemExit
else:
	nation = userDefArgs.nation

print("Nation defined. Proceeding")

#replace category spaces with plus signs.
strcat = userDefArgs.category
strcat = strcat.replace(" ", "+")

#if(userDefArgs.saveOutputToSTDOUT == "True"):
#	filesave = sys.stdout
#	print("Writing result to STDOUT")
#else:
if(userDefArgs.saveToFile != None):
	filesave = userDefArgs.saveToFile
elif(userDefArgs.saveToFile == None):
	print("No file defined. Defaulting to default.")

if(userDefArgs.category != None):
	category = strcat
	print("I am hoping you used a valid category, because I dont feel like checking. If its invalid, it will usually just return with the NATION tags. Proceeding")
elif(userDefArgs.category == None):
	print("ERROR: Category not defined PLease define a category using '-category'. Exiting.")

print("Don't know if you defined a password, it doesn't matter yet because I haven't coded that path yet.")

url='https://www.nationstates.net/cgi-bin/api.cgi'
head = {'user-agent':"ns-scraper, NationStates Scraper, <mfryk268@gmail.com>, https://github.com/ikeacat/ns-scraper",
        'X-Password':dataaccess("password")}
data = {'nation':nation,
        'q':category}
pr = requests.post(url, data=data, headers=head)
save = open(filesave, "w")
save.write(pr.text)
save.close()
print("Done!")