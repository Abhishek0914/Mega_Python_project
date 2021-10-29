import mysql.connector
m=mysql.connector.connect(host="localhost",user="root",passwd="India@123")
c=m.cursor()

def salesandmarketing():
    
    c.execute("USE  aa_premium_automobiles;")
    c.execute("DROP TABLE IF EXISTS SNM;")
    c.execute("CREATE TABLE SNM(S_no int(5),Company varchar(15),Model_name varchar(15),Units_sold int(15));")
    c.execute("INSERT INTO SNM VALUES(1,'Mercedes_Benz','S450',5);")
    c.execute("INSERT INTO SNM VALUES(2,'Mercedes_Benz','AMG GT',3);")
    c.execute("INSERT INTO SNM VALUES(3,'Mercedes_Benz','G63 AMG',9);")
    c.execute("INSERT INTO SNM VALUES(4,'BMW','7series',13);")
    c.execute("INSERT INTO SNM VALUES(5,'BMW','M5',19);")
    c.execute("INSERT INTO SNM VALUES(6,'BMW','320d',2);")
    c.execute("INSERT INTO SNM VALUES(7,'Jaguar','XJ',7);")
    c.execute("INSERT INTO SNM VALUES(8,'Jaguar','XF',3);")
    c.execute("INSERT INTO SNM VALUES(9,'Jaguar','XE',9);")
    c.execute("INSERT INTO SNM VALUES(10,'Audi','R8',21);")
    c.execute("INSERT INTO SNM VALUES(11,'Audi','A4',11);")
    c.execute("INSERT INTO SNM VALUES(12,'Audi','a6',12);")
    c.execute("INSERT INTO SNM VALUES(13,'Aston_Martin','DB9',11);")
    c.execute("INSERT INTO SNM VALUES(14,'Rolls_Royce','Ghost VI',3);")
    c.execute("INSERT INTO SNM VALUES(15,'Rolls_Royce','Cullinun',3);")
    c.execute("INSERT INTO SNM VALUES(16,'Lamborghini','Avantador',7);")
    c.execute("INSERT INTO SNM VALUES(17,'Buggati','Veyron',1);")
    c.execute("INSERT INTO SNM VALUES(18,'Lamborghini','Huracan_Evo',3);")
    c.execute("INSERT INTO SNM VALUES(19,'Lamborghini','Urus',12);")
    c.execute("INSERT INTO SNM VALUES(18,'Hyundai','SantaFe',3);")

    print("Please enter the brand you want to review")
    print("1. Mercedes Benz")
    print("2. BMW")
    print("3. Jaguar")
    print("4.Audi")
    print("5.Aston Martin")
    print("6.Rolls Royce")
    print("7.Lamborghini")
    print("8.Buggati")
    print("9.Hyundai")
    while True:
        c1=int(input("Enter choice"))
        if c1==1:
            c.execute("SELECT * FROM SNM WHERE Company='Mercedes_Benz' ;")
        elif c1==2:
            c.execute("SELECT * FROM SNM WHERE Company='BMW' ;")
        elif c1==3:
            c.execute("SELECT * FROM SNM WHERE Company='Jaguar' ;")
        elif c1==4:
            c.execute("SELECT * FROM SNM WHERE Company='Audi' ;")
        elif c1==5:
            c.execute("SELECT * FROM SNM WHERE Company='Aston_Martin' ;")
        elif c1==6:
            c.execute("SELECT * FROM SNM WHERE Company='Rolls_Royce' ;")
        elif c1==7:
            c.execute("SELECT * FROM SNM WHERE Company='Lamborghini' ;")
        elif c1==8:
            c.execute("SELECT * FROM SNM WHERE Company='Buggati' ;")
        elif c1==9:
            c.execute("SELECT * FROM SNM WHERE Company='Hyundai' ;")
        for i in c:
            print(i)
        cont=input("Continue?Y/N")
        if cont=="Y":
            continue
        elif cont=="N":
            break
#salesandmarketing()
        
def storelocator():
    print("Location of our outlet in your city")
    c.execute("USE aa_premium_automobiles;")
    c.execute("DROP TABLE IF EXISTS SL;")
    c.execute("CREATE TABLE SL(St_no int(5),City varchar(15),No_of_Stores int(5),Area varchar(50));")
    c.execute("INSERT INTO SL VALUES(1,'New Delhi',3,'Tughlaq lane');")
    c.execute("INSERT INTO SL VALUES(2,'Mumbai',2,'Bandra');")
    c.execute("INSERT INTO SL VALUES(3,'Chandigarh',1,'Sector 17');")
    c.execute("INSERT INTO SL VALUES(4,'Lahore',0,'Jine Lahore nai vekhya, O jamya-e-ni');")
    c.execute("INSERT INTO SL VALUES(5,'Ludhiana',1,'Sarabhanagar');")

    #query
    while True:
        city=input("Please select the city you live in ")
        print("1.New Delhi")
        print("2.Mumbai")
        print("3.Chandigarh")
        print("4.Lahore")
        print("5.Ludhiana")
        ci=int(input("Enter choice"))
        if ci==1:
            c.execute("SELECT Area,No_of_Stores FROM SL WHERE City='New Delhi';")
        elif ci==2:
            c.execute("SELECT Area,No_of_Stores FROM SL WHERE City='Mumbai';")
        elif ci==3:
            c.execute("SELECT Area,No_of_Stores FROM SL WHERE City='Chandigarh';")
        elif ci==4:
            c.execute("SELECT Area,No_of_Stores FROM SL WHERE City='Lahore';")
        elif ci==5:
            c.execute("SELECT Area,No_of_Stores FROM SL WHERE City='Ludhiana';")
        for i in c:
           print(i)
        cont=input("Continue?Y/N")
        if cont=="Y":
            continue
        elif cont=="N":
            break


def trackresults():
    print("View our results in the recent Grand Prix")
    c.execute("USE  aa_premium_automobiles;")
    c.execute("DROP TABLE IF EXISTS CIRCUIT;")
    c.execute("CREATE TABLE CIRCUIT(Circuit varchar(30),Position int(15),Driver varchar(65),Team varchar(25));")
    c.execute("INSERT INTO CIRCUIT VALUES('Monza','12','Bakir','Rassenballsport');")
    c.execute("INSERT INTO CIRCUIT VALUES('Monaco',3,'Nusrat Fateh Ali Khan','Redbull');")
    c.execute("INSERT INTO CIRCUIT VALUES('Nurburgring',2,'Shamu Patel','Ferrari');")
    c.execute("INSERT INTO CIRCUIT VALUES('Silverstone',1,'Michael Schumacher','Highskis');")
    c.execute("SELECT * FROM CIRCUIT")
    for i in c:
        print(i)
    print("Check back soon!")

def history():
    f=open("aa_automobile's_history.txt","r")
    r=f.read()
    print(r)

def partnerships():
    print("It was only with the help of our esteemed sponsors that we were able to scale such heights and expand our business")
    c.execute("USE  aa_premium_automobiles;")
    c.execute("DROP TABLE IF EXISTS Partnershipsandsponsors;")
    c.execute("CREATE TABLE Partnershipsandsponsors(s_no int(30),Parent_organisation varchar(60),owner varchar(65),Shares_owned_percent int(25));")
    c.execute("INSERT INTO Partnershipsandsponsors VALUES(1,'AA Premium Automobile And Business Solutions','Abhishek Bohra',30);")
    c.execute("INSERT INTO Partnershipsandsponsors VALUES(2,'AA Premium Automobile And Business Solutions','Aryaman Singh Katoch',30);")
    c.execute("INSERT INTO Partnershipsandsponsors VALUES(3,'Mercedes Benz Petronas','Julian Brandt',5);")
    c.execute("INSERT INTO Partnershipsandsponsors VALUES(4,'Lamborghini Newport Beach','Horacio Pagani',3);")
    c.execute("INSERT INTO Partnershipsandsponsors VALUES(5,'Usher Usher Usher','Usher',12);")
    c.execute("INSERT INTO Partnershipsandsponsors VALUES(6,'Khoshbin Real Estate','Manny Khoshbin',20);")
    c.execute("SELECT * FROM Partnershipsandsponsors;")
    for i in c:
        print(i)

def fantest():
  import random
  print("Let's put your exotic car knowledge to the test :)")
  while True:
    print("1. Brands")
    print("2. Models")
    v=int(input("which version would you like to play?1/2"))
    
    if v==1:
      print("Test your brand knowledge")
      x=random.randint(1,4)
      if x==1:
        print("R__L_ _O__E")
        r1=input("enter the answer")
        if r1=="ROLLS ROYCE":
          print("Spot on!")
        else:
          print("Better luck next time :/")
    

    
      elif x==2:
        print("_A__O___I_I")
        r2=input("enter the answer")
        if r2=="LAMBORGHINI":
          print("Spot on!")
        else:
          print("Better luck next time :/")
    


      elif x==3:
        print("_A___R")
        r3=input("enter the answer")
        if r3=="JAGUAR":
          print("Spot on!")
        else:
          print("Better luck next time :/")
    


      elif x==4:
        print("__G__T_")
        r1=input("enter the answer")
        if r1=="BUGGATI":
          print("Spot on!")
        else:
          print("Better luck next time :/")
    

    elif v==2:
        print("Test your car model knowledge")
        y=random.randint(1,4)


        if y==1:
          print("_E__O_")
          p1=input("enter the answer")
          if p1=="VEYRON":
            print("Spot on!")
          else:
            print("Better luck next time :/")
    

        elif y==2:
          print("__U_")
          p3=input("enter the answer")
          if p3=="URUS":
            print("Spot on!")
          else:
            print("Better luck next time :/")
   

        elif y==3:
          print("S___A_E")
          p3=input("enter the answer")
          if p3=="SANTAFE":
            print("Spot on!")
          else:
            print("Better luck next time :/")
   

        elif y==4:
          print("_H__T")
          p4=input("enter the answer")
          if p4=="GHOST":
            print("Spot on!")
          else:
            print("Better luck next time :/")


    cre=input("continue playing? Y/N")
    if cre=="Y":
      continue
    elif cre=="N":
      break


