import re

pattern = '^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
inp = raw_input()
if re.search(pattern,inp):
    print 'True'
else:
    print 'False'
