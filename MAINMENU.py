#MAIN MENU

from showmodels import *
from modeldetails import *
from colourQuery import *
from preferencial_search import *
from LoginScreen import *

print("Welcome to AA Premium Automobiles!!")
usr=input("Are you existing user? (yes/no) :")
r=False
if usr=='Yes' or usr=='yes':
  r=sign_in()
else:
  r=sign_up()
choice='no'
if r:
  choice='yes'
else:
  choice='no'

while choice=='yes' or choice=='Yes':
  print("1.Show our car linup")
  print("2.Search cars")
  print("3.A detailed overview of a selected brand collection")
  print("4.Show colour options available with various car brands")
  print("5.Sales and marketing reports")
  print("6.Store locator")
  print("7.View our results in recent track race collaborations")
  print("8.See our history")
  print("9.See our partnerships with other companies")
  print("10.Take the FAN TEST !!")
  ch=int(input("Enter your choice: "))
  if ch==1:
    showmodels()
  elif ch==2:
    preferencial_search()
  elif ch==3:
    totaldetails()
  elif ch==4:
    colouroptions()
  elif ch==5:
    salesandmarketing()
  elif ch==6:
    storelocator()
  elif ch==7:
    trackresults()
  elif ch==8:
    history()
  elif ch==9:
    partnerships()
  elif ch==10:
    fantest()
  else:
    print("Please enter a valid choice...")
  choice=input("Do you want to continue?: ")
