import sqlite3, os, time	#Importing neccessary modules


################################ LOG IN screen, first screen that will display
def login():
	print("""+--------------------------------------------------------------------------------+
				******* Showcast - LOG IN *******   
+--------------------------------------------------------------------------------+
Please enter your username and password

		""")
	username = str ( input("USERNAME: "))
	password = str ( input("PASSWORD: "))
	if len(username) < 1:
		print("ERROR: Sorry your password is incorrect. \n Please retry in 5 seconds")
		time.sleep(1)
		print("4..")
		time.sleep(1)
		print("3..")
		time.sleep(1)
		print("2..")
		time.sleep(1)
		print("1..")
		time.sleep(1)
		os.system('cls')
		login()
	else:
		menu1()

################################ MAIN & ADMIN MENU to call selected functions

def menu1():
	x = input("""

		******* Showcast - MAIN MENU *******

Please type the number of the option you would like to choose: 

** WHAT'S ON? **
1. VIEW UPCOMING SCREENINGS
2. BROWSE ANIME

** BOOKINGS **
3. CREATE NEW BOOKING
4. SEARCH BOOKING
5. VIEW ALL BOOKINGS

** CUSTOMERS **
6. CREATE NEW CUSTOMER 
7. SEARCH CUSTOMER 

** EXTRA **
8. ADMIN MENU
9. SET UP DEMO/FIX

Please type the option here: """)
	if x == "1":
		ScreeningVIEW()
		opt = input("To exit press '0' then enter: ")
		if opt=="0":
			menu1()
		else:
			print("ok")
	if x == "2":
		AnimeVIEW()
		opt = input("To exit press '0' then enter: ")
		if opt=="0":
			menu1()
		else:
			print("ok")
	if x == "3":
		BookingsADD()
		opt = input("To exit press '0' then enter: ")
		if opt=="0":
			menu1()
		else:
			print("ok")
	if x == "4":
		BookingsSearch()
		opt = input("To exit press '0' then enter: ")
		if opt=="0":
			menu1()
		else:
			print("ok")
	if x == "5":
		BookingsVIEW()
		opt = input("To exit press '0' then enter: ")
		if opt=="0":
			menu1()
		else:
			print("ok")
	if x == "6":
		CustomerADD()
		opt = input("To exit press '0' then enter: ")
		if opt=="0":
			menu1()
		else:
			print("ok")
	if x == "7":
		CustomersSearch()
		opt = input("To exit press '0' then enter: ")
		if opt=="0":
			menu1()
		else:
			print("ok")
	if x == "8":
		print("Opening admin menu")
		menu2()
	if x == "9":
		demo()
		opt = input("To exit press '0' then enter: ")
		if opt=="0":
			menu1()
		else:
			print("ok")
	else:
		print("ERROR: Please just type the number of the option you would like to \n select, for example type '1' without the apostrophes")
		opt = print("To exit press '0' then enter: ")
		if opt=="0":
			menu1()
		else:
			print("ok")

def menu2():
	x = input("""

		******* Showcast - ADMIN MENU *******

Please type the number of the option you would like to choose: 

** MANAGE **
1. MANAGE BOOKINGS
2. MANAGE GENRES
3. MANAGE CUSTOMERS
4. MANAGE STAFF
5. MANAGE ANIME
6. MANAGE SCREENS 

** ADD NEW **
7. ADD NEW ANIME
8. ADD NEW SCREENING
9. ADD NEW SCREEN

** STAFF **
10. CREATE NEW STAFF
11. RESET PASSWORD FOR STAFF

12. RETURN TO MAIN MENU

Please type the option here: """)
	if x == "1":
		print("Work in progress!")
		menu2()
	if x == "2":
		print("Work in progress!")
		menu2()
	if x == "3":
		print("Work in progress!")
		menu2()
	if x == "4":
		print("Work in progress!")
		menu2()
	if x == "5":
		print("Work in progress!")
		menu2()
	if x == "6":
		print("Work in progress!")
		menu2()
	if x == "7":
		menu2()
	if x == "8":
		screeningsADD()
		menu2()
	if x == "9":
		print("Hi9")
		menu2()
	if x == "10":
		menu2()
	if x == "11":
		menu2()
	if x == "12":
		menu1()
	else:
		print("ERROR: Please just type the number of the option you would like to \n select, for example type '1' without the apostrophes")
		menu2()

def demo():
	## Deleting faulty database file
	if os.path.exists("showcast_db.db"):
		os.remove("showcast_db.db")
		print("Successfully removed old database")
	else:
		print("No old database to remove, proceeding to create new demo database")

		## Creating database with all tables and example data
	if not os.path.isfile("showcast_db.db"): #Executed if the filename doesn't exist



		showcast_db = sqlite3.connect("showcast_db.db") #Creates new file for database
		c=showcast_db.cursor()

		c.execute ('''CREATE TABLE tblCustomers	#Creates table
		(CustomerID INTEGER PRIMARY KEY AUTOINCREMENT, #Adding all columns, inc first to be auto incrementing primary key so customers can have unique identifier
		Title text,
		FirstName text,
		LastName text,
		DOB date,
		Address1 text,
		Address2 text,
		City text,
		PostCode text,
		PhoneN int,		
		EMail text,
		BookingB text)		
		''')
		#Rest is the same but for seperate tables as labeled
		c.execute ('''CREATE TABLE tblBookings
		(id INTEGER PRIMARY KEY AUTOINCREMENT,
		CustomerID int,
		ScreeningREF text,
		NormalTKS int,
		ConcessionTKS int)
		''')
		
		c.execute ('''CREATE TABLE tblScreenings
		(ScreeningsID INTEGER PRIMARY KEY AUTOINCREMENT,
		AnimeID int,
		ScreenID int,
		Date_S date,
		Time_S time,
		Availability int,
		AutismF boolean)
		''')
		
		c.execute ('''CREATE TABLE tblStaff
		(StaffID INTEGER PRIMARY KEY AUTOINCREMENT,
		Username text,
		Password text,
		SQ1 text,
		SQ2 text,
		DOB date,
		PhoneN int,
		Address1 text,
		Address2 text,
		City text,
		PostCode text,
		Admin boolean)
		''')

		c.execute ('''CREATE TABLE tblAnime
		(AnimeID INTEGER PRIMARY KEY AUTOINCREMENT,
		Title text,
		Genre text,
		Lang text,
		MovieType boolean,
		AgeR text,
		rating text)
		''')
		c.execute ('''CREATE TABLE tblScreens
		(ScreenID INTEGER PRIMARY KEY AUTOINCREMENT,
		Seats int,
		Proj text,
		Sound text)
		''')
		
		print("New demo databse created successfully")


		showcast_db.commit()
		showcast_db.close()


	###Adding all example data into tables
	showcast_db = sqlite3.connect("showcast_db.db") #connect to database
	c=showcast_db.cursor() #shortcut to save typing
	print("Database connected successfully")


#inserts example data
	c.execute('''INSERT INTO tblCustomers
	VALUES (NULL, "Mr","James","Richards","16/05/00","12 Korok Avenue","St Mellons","Cardiff","CF30FA","07711632221","super@yahoo.com","2")''')
	c.execute('''INSERT INTO tblCustomers
	VALUES (NULL, "Miss","Jogn","Kenedy","27/09/99","21 Nomans Street","St Mellons","Cardiff","CF35BA","07511627251","danger@yahoo.com","4")''')
	c.execute('''INSERT INTO tblCustomers
	VALUES (NULL, "Ms","Annie","Yasuo","04/08/90","23 Korok Avenue","St Mellons","Cardiff","CF30FA","07512632421","annie@yahoo.com","6")''')
	
	c.execute('''INSERT INTO tblBookings
	VALUES (NULL, "1","1","1","0")''')
	c.execute('''INSERT INTO tblBookings
	VALUES (NULL, "2","1","2","1")''')	
	c.execute('''INSERT INTO tblBookings
	VALUES (NULL, "3","2","0","2")''')

	c.execute('''INSERT INTO tblScreenings
	VALUES (NULL,"0001","1","26/02/20","18:00","50","1")''')
	c.execute('''INSERT INTO tblScreenings
	VALUES (NULL, "0002","2","26/02/20","17:00","20","0")''')
	c.execute('''INSERT INTO tblScreenings
	VALUES (NULL, "0003","3","26/02/20","15:00","13","0")''')

	c.execute('''INSERT INTO tblStaff
	VALUES (NULL, "user2","pass2","llewllyn","pink","18/02/97","07711835552","52 Korok Avenue","St Mellons","Cardiff","CF30FA","1")''')
	c.execute('''INSERT INTO tblStaff
	VALUES (NULL, "user2","pass2","smith","blue","18/05/92","07511835552","50 Korok Avenue","St Mellons","Cardiff","CF30FA","0")''')
	c.execute('''INSERT INTO tblStaff
	VALUES (NULL, "user3","pass3","john","yellow","23/02/91","07722835552","42 Korok Avenue","St Mellons","Cardiff","CF30FA","0")''')

	c.execute('''INSERT INTO tblAnime
	VALUES (NULL, "My Hero Academia: Two Heroes","Action","Dub","1","PG 13","7.6")''')
	c.execute('''INSERT INTO tblAnime
	VALUES (NULL, "Spirited Away","Adventure","Sub","1","PG","8.6")''')
	c.execute('''INSERT INTO tblAnime
	VALUES (NULL, "Full Metal Alchemist - Brotherhood","Action","Dub","1","TV 14","9.1")''')

	c.execute('''INSERT INTO tblScreens
	VALUES (NULL, "70","Barco DP4K-40LHC","Dolby Atmos")''')
	c.execute('''INSERT INTO tblScreens
	VALUES (NULL, "40","Christie CP4450-RGB","Christie Surround System")''')
	c.execute('''INSERT INTO tblScreens
	VALUES (NULL,"42","Sony SRX-R510P","Bose Lifestyle® 650 ")''')

	showcast_db.commit()




################################ Viewing all data from tables

def ScreeningVIEW():

	showcast_db = sqlite3.connect("showcast_db.db") #connecting to database
	c=showcast_db.cursor()
	print("Database connected successfully")

	c.execute('''SELECT * FROM tblScreenings''') #Selecting everything from screenings table
	row = c.fetchall()
#displaying column names
	print("""

+--------------------------------------------------------------------------------+
				SCREENINGS    
+--------------------------------------------------------------------------------+
ScreeningID | AnimeID | ScreenID | Date | Time | Availability | Autism Friendly""")
	for x in range(len(row)):	#Displaying results in seperated row format
		print(" ")
		print(row[x])
	
	print("Databse read succesfully")

	showcast_db.commit()
	showcast_db.close()

def AnimeVIEW():

	showcast_db = sqlite3.connect("showcast_db.db")
	c=showcast_db.cursor()
	print("Database connected successfully")

	c.execute('''SELECT * FROM tblAnime''')    
	row = c.fetchall()

	print("""

+--------------------------------------------------------------------------------+
				ANIMES    
+--------------------------------------------------------------------------------+
AnimeD | Title | Genre | Dub/Sub | Movie Yes/No | Age | Rating""")
	for x in range(len(row)):
		print(" ")
		print(row[x])
	
	print("Databse read succesfully")

	showcast_db.commit()
	showcast_db.close()

def BookingsVIEW():

	showcast_db = sqlite3.connect("showcast_db.db")
	c=showcast_db.cursor()
	print("Database connected successfully")

	c.execute('''SELECT * FROM tblBookings''')    
	row = c.fetchall()

	print("""

+--------------------------------------------------------------------------------+
				BOOKINGS    
+--------------------------------------------------------------------------------+
ID | CustomerID | Screening Reference | Normal Tickets | Concession Tickets """)
	for x in range(len(row)):
		print(" ")
		print(row[x])
	
	print("Databse read succesfully")

	showcast_db.commit()
	showcast_db.close()

def CustomersVIEW():

	showcast_db = sqlite3.connect("showcast_db.db")
	c=showcast_db.cursor()
	print("Database connected successfully")

	c.execute('''SELECT * FROM tblCustomers''')    
	row = c.fetchall()

	print("""

+--------------------------------------------------------------------------------+
				CUSTOMERS    
+--------------------------------------------------------------------------------+
CustomerID | Title | First Name | Last Name | Address 1 | Address 2 | City | Post Code | Phone | Booking Balance""")
	for x in range(len(row)):
		print(" ")
		print(row[x])
	
	
	print("Databse read succesfully")

	showcast_db.commit()
	showcast_db.close()

def StaffVIEW():

	showcast_db = sqlite3.connect("showcast_db.db")
	c=showcast_db.cursor()
	print("Database connected successfully")

	c.execute('''SELECT * FROM tblStaff''')    
	row = c.fetchall()
	print("""

+--------------------------------------------------------------------------------+
				CUSTOMERS    
+--------------------------------------------------------------------------------+
StaffID | Username | Password | SQ1 | SQ2 | DOB | Phone | Address1 | Address2 | City | Post Code | Admin""")
	for x in range(len(row)):
		print(" ")
		print(row[x])
	
	print("Databse read succesfully")

	showcast_db.commit()
	showcast_db.close()

################################ Inputting single row of data into tables

def BookingsADD():
	###Create table if it doesn't exist
	if not os.path.isfile("showcast_db.db"):
		print("ERROR: Unable to connect to database please select \n option '9' from the main menu to set up the demo and try again")
		menu1()


	###Executed if table exists
	showcast_db = sqlite3.connect("showcast_db.db")
	c=showcast_db.cursor()
	print("Database connected successfully")

	CustomerID = input ("What is the CustomerID: ")
	ScreeningREF = input ("What is the ScreeningREF: ")
	NormalTKS = input ("How many normal tickets: ")
	ConcessionTKS = input ("How many concession tickets: ")


	c.execute('''INSERT INTO tblBookings
	VALUES (NULL,?, ?, ?, ?)''',(CustomerID, ScreeningREF, NormalTKS, ConcessionTKS))
	showcast_db.commit()
		

	print("Booking created successfully.") #!Booking reference coming soon!

	showcast_db.commit()
	showcast_db.close()



## Adding new screens
def screeningsADD():
	###Create table if it doesn't exist
	if not os.path.isfile("showcast_db.db"):
		print("ERROR: Unable to connect to database please select \n option '9' from the main menu to set up the demo and try again")
		menu1()


	###Executed if table exists
	showcast_db = sqlite3.connect("showcast_db.db")
	c=showcast_db.cursor()
	print("Database connected successfully")

	AnimeID = input ("What is the AnimeID?: ")
	ScreenID = input ("What is the ScreenID?: ")
	Date_S = input ("When is the screening?: ")
	Time_S = input ("What time is it on?: ")
	Availability = input ("Seats left?: ")
	AutismF = input ("Is it Autism Friendly?: ")

	c.execute('''INSERT INTO tblScreenings
	VALUES (NULL,?, ?, ?, ?, ?,?)''',(AnimeID, ScreenID, Date_S, Time_S, Availability, AutismF))
		


	showcast_db.commit()
	showcast_db.close()

## Adding new customer
def CustomerADD():
	###Create table if it doesn't exist
	if not os.path.isfile("showcast_db.db"):
		print("ERROR: Unable to connect to database please select \n option '9' from the main menu to set up the demo and try again")
		menu1()


	###Executed if table exists
	showcast_db = sqlite3.connect("showcast_db.db")
	c=showcast_db.cursor()
	print("Database connected successfully")

	Title = input ("What is the customer's title?: ")
	FirstName = input ("What is the First name?: ")
	LastName = input ("What is the Last name?: ")
	DOB = input ("What is the date of birth DD/MM/YY: ")
	Address1 = input ("What is the first line of the address including house name/number?: ")
	Address2 = input ("What is the second line?: ")
	City = input ("What is the city?: ")
	PostCode = input ("What is the post code?: ")
	PhoneN = input ("What is the contact number: ")
	EMail = input ("What is the E-Mail address: ")
	BookingB = input("What is the customers current booking balance?: ")
	c.execute('''INSERT INTO tblCustomers
	VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?)''',(Title, FirstName, LastName, DOB, Address1, Address2, City, PostCode, PhoneN, EMail, BookingB))
		

	showcast_db.commit()
	showcast_db.close()
################################ Searching and print functons

def BookingsSearch():
	showcast_db = sqlite3.connect("showcast_db.db")
	c=showcast_db.cursor()
	print("Database connected successfully")

	cid_input = input("What is the customer ID you would like to search for? \n Please enter just the number : ")
	c.execute('''SELECT * FROM tblBookings WHERE CustomerID = ? ''', (cid_input,))    
	row = c.fetchall()

	for x in range(len(row)):
		print(row[x])
	
	print("Databse read succesfully")

	showcast_db.commit()
	showcast_db.close()


def CustomersSearch():
	showcast_db = sqlite3.connect("showcast_db.db")
	c=showcast_db.cursor()
	print("Database connected successfully")

	dob_input = input("What is the data of birth you would like to search for? \n Please enter it in DD/MM/YY format: ")
	c.execute('''SELECT * FROM tblCustomers WHERE DOB = ?''', (dob_input,))    
	row = c.fetchall()
	
	print("""

+--------------------------------------------------------------------------------+
				CUSTOMERS    
+--------------------------------------------------------------------------------+
CustomerID | Title | First Name | Last Name | Address 1 | Address 2 | City | Post Code | Phone | Booking Balance""")
	for x in range(len(row)):
		print(row[x])
	
	print("Databse read succesfully")

	showcast_db.commit()
	showcast_db.close()



login()
