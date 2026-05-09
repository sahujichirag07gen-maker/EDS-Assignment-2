# 1.1.3 Days between two dates 
from datetime import datetime

#write your code here...
date1=input()
date2=input()
date_format='%Y-%m-%d'
sdt=datetime.strptime(date1,date_format).date()
edt=datetime.strptime(date2,date_format).date()
d=edt-sdt
print(d.days)