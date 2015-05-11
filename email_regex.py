import re
pattern = '^[A-Za-z0-9_-]+@[A-Za-z0-9]+\.[a-zA-Z]{1,3}$'
times = input()
emails = []
for x in range(0,times):
    emails.append(raw_input())

emails.sort()
emails = list(filter(lambda x: re.match(pattern,x),emails))
print emails