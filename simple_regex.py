import re
pattern = '^[7-9][\d]{9}$'

times = input()
for x in range(0,times):
    s = raw_input()
    print 'YES' if re.match(pattern,s) else 'NO'