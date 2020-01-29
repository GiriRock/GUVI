def cal_distance():
  km = abs(dest - src)
  taxi['distance']=km
  return km
def cal_fare():
  km = cal_distance()
  print("1.Mini (per Km 10)")
  print("2.Micro (per Km 30)")
  print("3.prime (per Km 50)")
  tc = int(input("Select the type of cab"))
  if(tc==1):
    fare = 10*km
  elif(tc==2):
    fare = 30*km
  elif(tc==3):
    fare = 50*km
  else:
    print("Enter the proper value")
    cal_fare(km)
  taxi['fare'] = fare

taxi = {'distance':0,'fare':0}

ch = 'y'
while (ch=='Y' or ch=='y'):
  src = int(input("Enter the source: "))
  if(src<0):
    print("Enter the proper value")
  else:
    dest = int(input("Enter the Destination: "))
    if(dest<0):
      print('Enter the proper value')
    else:
      if(dest>src):
        fare = cal_fare()
        print(taxi)
        ch  = input("Do u want to continue(y/n)")
      else:
        print("pls enter the valid Destination")
      