import mysql.connector
from mysql.connector import Error
import pandas as pd
from constant import *

columns = ["First name", "Last name"]
new_result = []

class Database:
    def __init__(self, host_name, user_name, user_password, db_name):
        self.host_name = host_name
        self.user_name = user_name
        self.user_password = user_password
        self.db_name = db_name
        self.connection = None
        self.cursor = None

    def create_server_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host_name,
                user=self.user_name,
                passwd=self.user_password,
                database=self.db_name
            )
            self.cursor = self.connection.cursor()
            print("MySQL Database connection successful")
        except Error as err:
            print(f"Error: '{err}'")

    def execute_query(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully")
        except Error as err:
            print(f"Error: '{err}'")

    def execute_read_query(self, query):
        result = None
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            print("Query executed successfully")
        except Error as err:
            print(f"Error: '{err}'")
        return result



if __name__ == "__main__":
    create_database_query = "CREATE DATABASE bank;"
    create_table_query = """
CREATE TABLE Branch (
    branchNo VARCHAR(4) PRIMARY KEY,
	street VARCHAR(25) NOT NULL,
	city VARCHAR(8) NOT NULL,
	postcode VARCHAR(8) NOT NULL
);
"""
    create_table_query_1 = """
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
    insert_branches = """
INSERT INTO Branch (branchNo, street, city, postcode)
VALUES ('B005', '22 Deer Rd', 'London', 'SW1 4EH'),
        ('B007', '16 Argyll St', 'Aberdeen', 'AB2 3SU'),
        ('B003', '163 Main St', 'Glasgow', 'G11 9QX'),
        ('B004', '32 Manse Rd', 'Bristol', 'BS99 1NZ'),
        ('B002', '56 Clover Dr', 'London', 'NW10 6EU');
"""  
    select_staff = """
SELECT fName, lName FROM Staff;
"""
    select_branches = "SELECT * FROM Branch;"

    delete_staff = """
    DELETE FROM Staff WHERE staffNo = 'SL41';
    """

    db = Database("localhost","root",PASSWORD,"bank")
    db.create_server_connection()
    db.execute_query(create_table_query)
    db.execute_query(create_table_query_1)
    db.execute_query(insert_branches)
    db.execute_query(insert_staff)
    db.execute_query(delete_staff)
    results_staff = db.execute_read_query(select_staff)

    for result in results_staff:
        result = list(result)
        new_result.append(result)

    df = pd.DataFrame(new_result, columns=columns)
    print(df)