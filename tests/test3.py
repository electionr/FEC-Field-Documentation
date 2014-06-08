import re
field = '16-D YESNO (WAS THE effort made BY creditor to collect similar to other debt collection efforts' 
match = re.match(r'\s*(\d+\-[A-F])\s(YESNO)\s(\([A-Za-z\s\.]+)', field)
if (match):
    items = match.groups()
    (number,ftype,name) = items
    print number, name
else:
    print "none"
