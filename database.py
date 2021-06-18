import mysql.connector

try:
	db = mysql.connector.connect(
		host='localhost',								#usually 'localhost'
		user='TYPE_YOUR_USER',							#usually 'root'
		passwd='TYPE_YOUR_MYSQL_PASW'
	)

	cursor = db.cursor()
	connected = True

except:
	connected = False


#if the database does not exist, it will be created
try:
	cursor.execute('USE AccountProj')

except:
	cursor.execute('CREATE DATABASE AccountProj') #Add users table
	cursor.execute('USE AccountProj')
	cursor.execute('CREATE TABLE Data (Nick VARCHAR(10), Pasw VARCHAR(10), Birth DATE)')

