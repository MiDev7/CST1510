import mysql.connector
from mysql.connector import Error
import pandas as pd
from constant import *

columns = ["First naem", "Last name"]
new_result = []

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


create_table_query = """
CREATE TABLE Staff(
	staffNo VARCHAR(4) PRIMARY KEY,
	fName VARCHAR(25) NOT NULL,
	lName VARCHAR(25) NOT NULL,
	position VARCHAR(15) NOT NULL,
	dob DATE NOT NULL,
	salary DECIMAL(7,2) NOT NULL,
	branchNo VARCHAR(4),
	FOREIGN KEY (branchNo) REFERENCES Branch(branchNo)
) ENGINE INNODB;
"""

insert_staff = """
INSERT INTO Staff (staffNo, fName, lName, position,dob, salary, branchNo)
VALUES ('SL21', 'John', 'White', 'Manager', '1945-10-01', 30000, 'B005'),
        ('SG37', 'Ann', 'Beech', 'Assistant', '1960-11-10', 12000, 'B003'),
        ('SG14', 'David', 'Ford', 'Supervisor', '1958-03-24', 18000, 'B003'),
        ('SA9', 'Mary', 'Howe', 'Assistant', '1970-02-19',9000, 'B007'),
        ('SG5', 'Susan', 'Brand', 'Manager', '1940-06-03', 24000, 'B003'),
        ('SL41', 'Julie', 'Lee', 'Assistant', '1965-06-13', 9000, 'B005');
"""

select_staff = """
SELECT fName, lName FROM Staff;
"""

delete_staff = """
DELETE FROM Staff WHERE staffNo = 'SL41';
"""

connection = create_server_connection("localhost","root",PASSWORD,"bank")
execute_query(connection, create_table_query)
execute_query(connection, insert_staff)
results = execute_read_query(connection, select_staff)
execute_query(connection, delete_staff)
results = execute_read_query(connection, select_staff)

for result in results:
    result = list(result)
    new_result.append(result)


df = pd.DataFrame(new_result, columns=columns)
print(df)