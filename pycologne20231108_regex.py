# https://regex101.com

# how to use regex in python

import re
line = "Unsere Pizza hat [Zwiebel]"
m=re.findall(r'\[(.+?)\]',line)
print(m)


print(re.search(r'\[(.+?)\]',line))

# Backus Naur form ist das Aequivalent zu regular expressions fuer kontext-freie Sprachen

with open('setup.py','r') as f:
    for line in f.readlines():
        if re.match(r'\s*#',line): # match startet automatisch am Anfang der Zeile
            continue
        print(line,end='')