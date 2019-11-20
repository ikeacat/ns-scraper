import argparse
import urllib.request
import sys

# Vars & other stuff
filesave = "nsdownload.html"

def listCategories():
	print("Public Categories:")
	sys.stdout.write("animal\nbanner\nbanners - returns a list of Rift banners that should be displayed: the nation's primary banner (if any) is always listed first, with the remainder in random order. Banner codes can be converted into image URLs by prepending /images/banner           s/ and appending .jpg. \ncapital\ncategory\ncrime\ncurrency\ncustomleader\ncustomcapital\ncustomreligion\ndbid\ndeaths\ndemonym\ndispatches\ndispatchlist\nendorsements\nfactbooks\nfactbooklist\nfirstlogin\nflag\nfounded\nfoundedtime\nfreedom\nfullname\ngavote\ngdp\ngovt\ngovtdesc\ngovtpriority\nhappenings\nincome\nindustrydesc\ninfluence\nlastactivity\nlastlogin\nleader\nlegislation\nmajorindustry\nmotto\nname\nnotable\npolicies\npoorest\npopulation\npublicsector\nrcensus\nregion\nreligion\nrichest\nscvote\nsectors\nsensibilities\ntax\ntgcanrecruit\ntype\nwa\nwabadges\nwcensus\n\n")
# Main
mainParser = argparse.ArgumentParser(description="Process main commands")
mainParser.add_argument('-nation', help='Define the Nation you would like to scrape from.', type=str)
mainParser.add_argument('-password', help='(Optional), Enter the password, if you would like to get something that is private (Ex. Issues), Command Ex: -password "insertpasshere"')
mainParser.add_argument('-saveToFile', help='(Optional), Save to a specific file. Is not compatible with "--saveOutputToSTDOUT". (EX: -saveToFile "downfile")', type=str)
# mainParser.add_argument('-saveOutputToSTDOUT', help='(Optional), print output to STDOUT at end. Put (without quotes) "True" or "False" (CaSe SeNsItIvE!). Is not compatible with "-saveToFile", default is False')
mainParser.add_argument('-category', help='Choose the category', type=str, default="")
mainParser.add_argument('--listCategories', help='(Optional) List the categories avaliable, categories that have (P) before it require the defined nation\'s password. Use alone. Use True or False after.', type=bool)
mainParser.add_argument('-numOfCategories', help='(Optional) Choose how many categories to use. Defaults to 1. Entering 0 will crash the program.', type=int, default=1)

userDefArgs = mainParser.parse_args()

if(userDefArgs.listCategories == True):
	listCategories()
	raise SystemExit

if(userDefArgs.nation == None):
	print("ERROR: Nation not defined. Please define a nation using '-nation'. Exiting.")
	raise SystemExit
else:
	nation = userDefArgs.nation

print("Nation defined. Proceeding")

if(userDefArgs.numOfCategories == 0):
    print("ERROR: Number of Categories is defined as 0. Must be 1 or above.")
    raise SystemExit
elif(userDefArgs.numOfCategories == 1):
    print("1 category defined.")
elif(userDefArgs.numOfCategories > 1):
    print("%i of categories defined to parse. If the number of categories is smaller than the amount " % userDefArgs.numOfCategories)
maxCategories = userDefArgs.numOfCategories - 1

categories = userDefArgs.numOfCategories.split()

#if(userDefArgs.saveOutputToSTDOUT == "True"):
#	filesave = sys.stdout
#	print("Writing result to STDOUT")
#else:
if(userDefArgs.saveToFile != None):
	filesave = userDefArgs.saveToFile
elif(userDefArgs.saveToFile == None):
	print("No file defined. Defaulting to default.")

if(userDefArgs.category != None):
	category = userDefArgs.category
	print("I am hoping you used a valid category, because I dont feel like checking. If its invalid, it will usually just return with the NATION tags. Proceeding")
elif(userDefArgs.category == None):
	print("ERROR: Category not defined PLease define a category using '-category'. Exiting.")

print("Don't know if you defined a password, it doesn't matter yet because I haven't coded that path yet.")

url='https://www.nationstates.net/cgi-bin/api.cgi?nation=%s&q=%s' % (nation, category)
urllib.request.urlretrieve(url, filesave)
print("Done!")