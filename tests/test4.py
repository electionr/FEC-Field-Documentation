import re
x='31-YES/NO (Activity is Public Communications {Referring Only to Party} Made by PAC'
match = re.match(r'\s*(\d+\-)(YES\/NO)\s(\([A-Za-z\{\}\.].+)', x)
if (match):
    items = match.groups()
    (number,ftype,name) = items
    print "OK"
else : 
    print "not ok"
