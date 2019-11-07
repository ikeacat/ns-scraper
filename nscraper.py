import urllib.request
import time

print("Nationstates Puller")
print("Brought to you by Entitize or ikeacat.")
time.sleep(2)
print("Please type the nation you want to access below. (lowercase).Please replace spaces with '+' signs.")
nation = input("")
time.sleep(1)
print("Type what you want to recieve (lowercase) (religion, category, animal, firstlogin (not recommended, returns with a long number), religion, wa, zombie (ONLY Z-DAY))")
print("use ALL to get all of them (be prepared for a quite long wait.).")
print("More categories at https://www.nationstates.net/pages/api.html#nationapi-publicshards")
category = input("")
if(category != "ALL"):
    time.sleep(1)
    print("The Text will be exported to downloadns.html")
    time.sleep(3)
    url='https://www.nationstates.net/cgi-bin/api.cgi?nation=%s&q=name+%s' % (nation, category)
    urllib.request.urlretrieve(url, 'downloadns.html')
    print("Done!")
elif(category == "ALL"):
    print("Whoops! We forgot enable this. It will be enabled later.")
    print("")
    print('END.')
    time.sleep(2)
    raise SystemExit
