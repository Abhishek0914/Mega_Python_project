#Project (login and register)

import mysql.connector

#mycs.execute("create table users(username varchar(20),password varchar(20))")

def check_credentials(user,pwd):
  mydb=mysql.connector.connect(host="localhost",user="root",passwd="India@123",database="aa_premium_automobiles")
  mycs=mydb.cursor()
  mycs.execute("select * from users where username='"+user+"' and password='"+pwd+"'")
  result=mycs.fetchone()
  #print ("Record: ",result)
  if result==None:
    return False
  else:
    return True
  mycs.close()
  mydb.close()
  
def store_credentials(user,pwd):
  mydb=mysql.connector.connect(host="localhost",user="root",passwd="India@123",database="aa_premium_automobiles")
  mycs=mydb.cursor()
  mycs.execute("select * from users where username='"+user+"'")
  result=mycs.fetchone()
  #print ("User Record: ",result)
  if result!=None:
    mycs.close()
    mydb.close()
    return False
  mycs.execute("insert into users values ('"+user+"', '"+pwd+"')")
  mydb.commit()
  mycs.close()
  mydb.close()
  return True

def sign_up():
  print("SignUp:")
  un=input("Enter username: ")
  pswd=input("Enter password: ")
  result=store_credentials(un,pswd)
  if result:
    print("You have Registered Successfully!")
    return True
  else:
    print("User already exists!!")
    return False

def sign_in():
  print("SignIn:")
  un=input("Enter Username: ")
  pswd=input("Enter Password: ")
  result=check_credentials(un,pswd)
  if result:
    print("Login Successfull!")
    return True
  else:
    print("Login Failed!! Either Username or Password is in-correct!")
    return False
  
#sign_in()

  
