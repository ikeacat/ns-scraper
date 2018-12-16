import urllib.request
import time

print("Nationstates Puller")
print("Brought to you by Entitize or ikeacat.")
time.sleep(2)
print("Please type the nation you want to access below. (lowercase).Please replace spaces with '+' signs.")
nation = input("")
time.sleep(1)
print("Type what you want to recieve (lowercase) (religion, category, animal, firstlogin, religion, wa, zombie (ONLY Z-DAY))")
print("More categories at https://www.nationstates.net/pages/api.html#nationapi-publicshards")
category = input("")
time.sleep(2)
print("The Text will be exported to downloadns.html")
time.sleep(3)
url='https://www.nationstates.net/cgi-bin/api.cgi?nation=%s&q=name+%s' % (nation, category)
urllib.request.urlretrieve(url, 'downloadns.html')
