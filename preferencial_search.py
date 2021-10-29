#PROJECT (car suggestion option)
def preferencial_search():
  import mysql.connector
  db=mysql.connector.connect(host="localhost",user="root",passwd="India@123",database="aa_premium_automobiles")
  mycs=db.cursor()
  brand=input("Enter brand name: ")
  price=input("Enter your budget: ")
  mycs.execute("select Company,Price,Model_name from models_available where Company='"+brand+"' and Price<="+price+" ")
  x=False
  for i in mycs:
    print ("The car matching your preferences is: ",i)
    x=True
  if x==False:
    print("Could Not find the car matching your preferences...!!!")
  mycs.close()
  db.close()



