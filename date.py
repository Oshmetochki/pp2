import datetime
import calendar
date_start=[int(i) for i in input().split('-')]
date_end=[int(i) for i in input().split('-')]
if date_start[1] == date_end[1]:
    a=((date_end:=datetime.datetime(year=date_end[0], month=date_end[1], day=date_end[2]))-(date_start:=datetime.datetime(year=date_start[0], month=date_start[1], day=date_start[2])))
    print(int(a.days+1))
else:
    a=calendar.monthrange(date_start[0],date_start[1])
    print(a[1]-date_start[2]+1)


















