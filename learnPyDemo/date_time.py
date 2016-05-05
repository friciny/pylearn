from datetime import datetime

now = datetime.now()
print(type(now))
print(now)
print(now.timestamp())


import re
from datetime import datetime,timezone,timedelta

def to_timestamp(dt_str,tz_str):
	dt_time=datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
	tz=re.match(r'^UTC([\+|\-]\d+):(\d+)',tz_str)
	hour=int(tz.group(1))-8
	minute=int(tz.group(2))
	dt_stamp=dt_time-timedelta(hours=hour,minutes=minute)
	return dt_stamp
t1=to_timestamp('2015-6-1 08:10:30','UTC+7:00')
print(t1)
t2=to_timestamp('2015-5-31 16:10:30','UTC-9:00')
print(t2)

def to_timestamp1(dt_str,tz_str):
	dt_time=datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
	tz=re.match(r'^UTC([\+|\-]\d+):(\d+)',tz_str)
	hour=int(tz.group(1))
	minute=int(tz.group(2))
	tz_utc=timezone(timedelta(hours=hour,minutes=minute))
	return dt_time.replace(tzinfo=tz_utc).timestamp()
t1=to_timestamp1('2015-6-1 08:10:30','UTC+7:00')
print(t1)
t2=to_timestamp1('2015-5-31 16:10:30','UTC-9:00')
print(t2)