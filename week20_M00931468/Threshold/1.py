import mysql.connector
from mysql.connector import Error
from constant import *

def create_server_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password,
            database = db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as err:
        print(f"Error: '{err}'")

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        print("Query executed successfully")
        return result
    except Error as err:
        print(f"Error: '{err}'")


connection = create_server_connection("localhost","root",PASSWORD,"bank")

create_database_query = "CREATE DATABASE bank;"
create_table_query = """
CREATE TABLE Branch (
    branchNo VARCHAR(4) PRIMARY KEY,
	street VARCHAR(25) NOT NULL,
	city VARCHAR(8) NOT NULL,
	postcode VARCHAR(8) NOT NULL
);
"""

insert_branches = """
INSERT INTO Branch (branchNo, street, city, postcode)
VALUES ('B005', '22 Deer Rd', 'London', 'SW1 4EH'),
        ('B007', '16 Argyll St', 'Aberdeen', 'AB2 3SU'),
        ('B003', '163 Main St', 'Glasgow', 'G11 9QX'),
        ('B004', '32 Manse Rd', 'Bristol', 'BS99 1NZ'),
        ('B002', '56 Clover Dr', 'London', 'NW10 6EU');
"""

select_branches = "SELECT * FROM Branch;"

execute_query(connection, create_table_query)
execute_query(connection, insert_branches)
print(execute_read_query(connection, select_branches))
