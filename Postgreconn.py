import psycopg2
from psycopg2 import Error

try:
    # Connect to an existing database
    # connection= psycopg2.connect(user="postgres",
    #                               password="Peacock",
    #                               host="localhost",
    #                               port="5432",
    #                               database="test")

    # Create a cursor to perform database operations
    cursor = connection.cursor()
    # Print PostgreSQL details
    print("PostgreSQL server information")
    print(connection.get_dsn_parameters(), "\n")
    # Executing a SQL query
    # cursor.execute("SELECT version();")
    # cursor.execute("CREATE TABLE person(id bigserial NOT NULL PRIMARY KEY,name varchar(100) NOT NULL,country varchar(50) NOT NULL);")
    # cursor.execute("INSERT INTO person (name,country) values ('JAYSHRI','U.K');")
    # cursor.execute("INSERT INTO person (name,country) values ('Sania','U.K');")
    # cursor.execute("INSERT INTO person (name,country) values ('Anthony','Zambia');")
    #cursor.execute("UPDATE person set name='Evan' WHERE id=1;")
    cursor.execute("DELETE FROM person where id=2;")
    cursor.execute("SELECT * FROM person;")
    # Fetch result
    connection.commit()
    record = cursor.fetchall()
    print( record, "\n")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
