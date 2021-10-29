# PROJECT (Models Choice menu)

import mysql.connector
def totaldetails(bname):
  mydb=mysql.connector.connect(host="localhost",user="root",passwd="India@123",database="aa_premium_automobiles")
  mycs=mydb.cursor()
  #print ("Connection to our server is ",mydb.is_connected)
  mycs.execute("select Company, Model_name,Model_year,Year_of_addition, Price from models_available where Company='"+bname+"'")#+"' and model_name='"+mname+"' ")
  print("Details for the car you chose are: ")
  print("Company\tModel\tYear\tDate of addition\t\tPrice")
  for x in mycs:
    print(x[0],end="\t")
    print(x[1],end="\t")
    print(x[2], end="\t")
    print(x[3], end="\t")
    print(x[4])
  mycs.close()
  mydb.close()

#totaldetails("BMW")
def get_company_names():
  mydb=mysql.connector.connect(host="localhost",user="root",passwd="India@123",database="aa_premium_automobiles")
  mycs=mydb.cursor()
  mycs.execute("select distinct(company),Model_name from models_available order by company")
  comp_list=[]
  for comp in mycs:
    comp_list.append(comp[0])
  mycs.close()
  mydb.close()
  return comp_list

def history():
  file = open("history.txt","r")
  print(file.read())
  file.close()

'''history()
c='y'
while c=='y' or c=='Y':
  print("Choose from our range of luxury car brands to see the models available in them: ")
  c_list=get_company_names()
  i=1
  print("0 . History")
  for comp in c_list:
    print(i,". ",comp)
    i+=1
  ch=int(input("Enter your choice: "))
  if ch>=i or ch<0:
    print("Invalid choice!!")
  elif ch==0:
    history()
  else:
    totaldetails(c_list[ch-1])
  c=input("Do you want to continue? (y/n) ")'''











    
