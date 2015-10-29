#!/usr/bin/python

import argparse
import re

parser = argparse.ArgumentParser(description='Count initiators in "symaccess list login" output.')
parser.add_argument('-f','--file', help='Filename containing symaccess list login output.', required=True)
args = vars(parser.parse_args())

logins = open(args['file'])

loggedinlist = []
completelist = []

for line in logins:
    if re.match("(.*)Fibre(.*)", line):
        loggedin = line.split()[5]
        wwn = line.split()[0]
        if loggedin == "Yes":
            # This is a logged in initiator; add it to both arrays
            loggedinlist.append(wwn)
            completelist.append(wwn)
        else:
            # This is not a logged in initiator; add it only to the complete array
            completelist.append(wwn)

uniqloggedinlist = []
uniqcompletelist = []

for element in loggedinlist:
    if element not in uniqloggedinlist:
        uniqloggedinlist.append(element)

for element in completelist:
    if element not in uniqcompletelist:
        uniqcompletelist.append(element)

print("\n")
print("                           Total login table entries: " + str(len(completelist)))
print("        Unique WWNs within total login table entries: " + str(len(uniqcompletelist)))
print("\n")
print("                     'Logged in' login table entries: " + str(len(loggedinlist)))
print("  Unique WWNs within 'Logged in' login table entries: " + str(len(uniqloggedinlist)))
print("\n")

