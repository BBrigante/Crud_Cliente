import pyodbc

server = 'BRUNO'
database = 'Crud_Python' 
username = 'sa' 
password = 'root'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=no;UID='+username+';PWD='+ password)
cursor = cnxn.cursor()