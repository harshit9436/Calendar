def lenMonth(i,year):
  days31 = [0,2,4,6,7,9,11]
  if i == 1:
    if year%4 != 0 :
      return 28
    elif year%100 != 0 :
      return 29
    elif year%400 != 0 :
      return 28
    return 29
  elif i in days31:
    return 31
  else:
    return 30

def firstDay(year):
  x = year-1582
  y = year-1
  new = x + y//4 - y//100 + y//400 - 383
  return (4+new)%7

def monthsCal(year):
  lastDay = firstDay(year)-1
  months = [0 for i in range(0,12)]
  for iter in range(0,12):
    week = ["   " for p in range(0,43)]
    for i in range(lenMonth(iter,year)):
      if i<9:
        week[(lastDay+1)%7+i] = str(i+1)+"  "
      else:
        week[(lastDay+1)%7+i] = str(i+1)+" "
    months[iter] = week
    lastDay = (lastDay+lenMonth(iter,year))%7
  return months

days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun",]
monthnames = ["JANUARY","FEBRUARY","MARCH","APRIL","MAY","JUNE","JULY","AUGUST","SEPTEMBER","OCTOBER","NOVEMBER","DECEMBER"]

def printCalendar(year):
  months = monthsCal(year)
  calend = open("calender{}.txt".format(year),"a")
  print("{:^91}".format(year),file=calend)
  print("",file=calend)
  for l in range(0,4):
    print("{a[0]:^27}{a[1]:^37}{a[2]:^27}".format(a=monthnames[3*l:3*l+3]),file=calend)
    print(*days, sep = " ", end="     ",file=calend)
    print(*days, sep = " ", end="     ",file=calend)
    print(*days, sep = " ",file=calend)
    for i in range(0,7):
      for k in range(3*l,3*l+3):
        if k < 3*l+2:
          print(*months[k][7*i:7*i+7],sep = " ", end="     ",file=calend)
        else:
          print(*months[k][7*i:7*i+7],sep = " ",file=calend)
  calend.close()
  print("The calender for the year {} has been printed! Please check the directory.".format(year))

