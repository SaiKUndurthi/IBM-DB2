import ibm_db;

dsn_driver = "{IBM DB2 ODBC DRIVER}"
dsn_database = "BLUDB"            # e.g. "BLUDB"
dsn_hostname = "<hostname>" # e.g.: "awh-yp-small03.services.dal.bluemix.net"
dsn_port = "50000"                # e.g. "50000" 
dsn_protocol = "TCPIP"            # i.e. "TCPIP"
dsn_uid = "<username>"        # e.g. "dash104434"
dsn_pwd = "<password>" 		# e.g. "7dBZ3wWt9XN6$o0JiX!m"

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
    print ("Connected!")

except:
    print ("Unable to connect to database")

ibm_db.close(conn)
