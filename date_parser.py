from datetime import datetime, timedelta

for x in range(input()):
    date1 = raw_input()
    date2 = raw_input()
    d1 = datetime.strptime(date1[:-6],"%a %d %b %Y %H:%M:%S")
    d2 = datetime.strptime(date2[:-6],"%a %d %b %Y %H:%M:%S")
    d_1 = timedelta(hours=int(date1[-5:-2]),minutes=int(date1[-2:]))
    d_2 = timedelta(hours=int(date2[-5:-2]),minutes=int(date2[-2:]))
    d1_t = (d1 - d_1) - datetime(1970,1,1)
    d2_t = (d2 - d_2) - datetime(1970,1,1)
    print "%.f"%(abs(d1_t.total_seconds() - d2_t.total_seconds()))
