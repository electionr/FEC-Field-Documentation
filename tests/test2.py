import re
field = '16-D. YESNO (effort made by creditor to collect...'
match = re.match(r'\s*(\d+\-[A-F]\.)\s(YESNO)\s(\([A-Za-z\.].+)', field)
if (match):
    items = match.groups()
    (number,ftype,name) = items
    print number, name
else:
    print "none"
