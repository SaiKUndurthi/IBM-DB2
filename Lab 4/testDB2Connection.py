import ibm_db;
import pandas;
import ibm_db_dbi;
import config;

dsn_driver = "{IBM DB2 ODBC DRIVER}"
dsn_database = "BLUDB"            # e.g. "BLUDB"
dsn_hostname = "dashdb-txn-sbox-yp-dal09-03.services.dal.bluemix.net" # e.g.: "awh-yp-small03.services.dal.bluemix.net"
dsn_port = "50000"                # e.g. "50000" 
dsn_protocol = "TCPIP"            # i.e. "TCPIP"
dsn_uid = config.dsn_uid        # e.g. "dash104434"
dsn_pwd = config.dsn_pwd		# e.g. "7dBZ3wWt9XN6$o0JiX!m"

#Create the dsn connection string
dsn = ( 
		 "DRIVER={0};"
		 "DATABASE={1};"
		 "HOSTNAME={2};"
		 "PORT={3};"
		 "PROTOCOL={4};"
		 "UID={5};"
		 "PWD={6};"
 ).format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd) #print the connection string to check correct values are specified print(dsn)

try:
    conn = ibm_db.connect(dsn, "", "")
    pconn = ibm_db_dbi.Connection(conn)
    print ("Connected!")

except:
    print ("Unable to connect to database")
#Lets first drop the table INSTRUCTOR in case it exists from a previous attempt
dropQuery = "drop table INSTRUCTOR"

#Now execute the drop statment
dropStmt = ibm_db.exec_immediate(conn, dropQuery)
#Construct the Create Table DDL statement - replace the ... with rest of the statement
createQuery = "Create table Instructor (ins_id Integer not null Primary Key,lastname varchar(25) not null,firstname varchar(25) not null,city varchar(25),country char(2));"

#Now fill in the name of the method and execute the statement
createStmt = ibm_db.exec_immediate(conn, createQuery)

#Construct the query - replace ... with the insert statement
insertQuery = "insert into Instructor values(1, 'Ahuja', 'Rav', 'Toronto', 'CA')"

#execute the insert statement
insertStmt = ibm_db.exec_immediate(conn, insertQuery)
#replace ... with the insert statement that inerts the remaining two rows of data
insertQuery2 = "insert into Instructor values (2, 'Chong', 'Raul', 'Toronto', 'CA'),(3, 'Vasudevan', 'Hima', 'Chicago', 'US');"

#execute the statement
insertStmt2 = ibm_db.exec_immediate(conn, insertQuery2)
#Construct the query that retrieves all rows from the INSTRUCTOR table
selectQuery = "select * from INSTRUCTOR"
#retrieve the query results into a pandas dataframe
pdf = pandas.read_sql(selectQuery, pconn)

#print just the LNAME for first row in the pandas data frame
print(pdf.LASTNAME[0])
print(pdf)
pdf.shape
#Execute the statement
selectStmt = ibm_db.exec_immediate(conn, selectQuery)
#Fetch the Dictionary (for the first row only) - replace ... with your code
#ibm_db.fetch_both(selectStmt)
updateQuery = "update Instructor set city = 'Markham' where ins_id = 1"
updateStmt = ibm_db.exec_immediate(conn, updateQuery)
print(pdf)
while ibm_db.fetch_row(selectStmt) != False:
   print (" ID:",  ibm_db.result(selectStmt, 0), " FNAME:",  ibm_db.result(selectStmt, "FIRSTNAME")," CITY:",  ibm_db.result(selectStmt, 3))
print(pdf.CITY[0])
ibm_db.close(conn)