import os
import argparse
import urllib.request

# Vars & other stuff
filesave = "nsdownload.html"

mainParser = argparse.ArgumentParser(description="Process main commands")
mainParser.add_argument('-nation', help='Define the Nation you would like to scrape from.')
mainParser.add_argument('-password', help='(Optional), Enter the password, if you would like to get something that is private (Ex. Issues)')
