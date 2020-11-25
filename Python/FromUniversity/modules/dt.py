import datetime
print(datetime.datetime.now().year, datetime.datetime.now().hour, datetime.datetime.now().minute)
print(datetime.datetime.ctime(datetime.datetime.now()))
print(datetime.datetime.strftime(datetime.datetime.now(), '%Y-%X-%D-%A-%B'))

t = "2 June 2020 10:12:30"
tm = datetime.datetime(2001, 10, 22)
ks = datetime.datetime.timestamp(datetime.datetime.now())-datetime.datetime.timestamp(tm)#timestamp saniye çevirme
print(datetime.datetime.fromtimestamp(ks)) 