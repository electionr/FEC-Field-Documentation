import re
field = '32-28(a)  Individuals'
match = re.match(r'(\d+\-\d+\(\w\))\s+(\w+)', field)
if (match):
    items = match.groups()
    (number,name) = items
    print number, name
else:
    print "none"
