import re


a = 'appleba21na11na'

if re.search(r'a1\dn', a) is not None:
    print 'be'
else:
    print 'nope.'