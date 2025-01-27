# # Q1. What is a database? Differentiate between SQL and NoSQL databases.
# # Database: A database is an organized collection of structured information or data, typically stored electronically in a computer system. It allows for the efficient storage, retrieval, and manipulation of data.

# # SQL vs NoSQL:

# # SQL (Structured Query Language) Databases:

# # SQL databases are relational, meaning they store data in tables with rows and columns.
# # They use Structured Query Language (SQL) for querying and managing the database.
# # They are best suited for structured data that fits into predefined schemas.
# # Examples: MySQL, PostgreSQL, Oracle, MS SQL Server.
# # NoSQL Databases:

# # NoSQL databases are non-relational, meaning they do not store data in tables but use a variety of storage models like document-based, key-value pairs, graph, or columnar storage.
# # They are more flexible in handling unstructured or semi-structured data.
# # Best for use cases with high scalability, large volumes of data, or rapidly changing data models.
# # Examples: MongoDB, Cassandra, Redis, CouchDB.




# Q2. What is DDL? Explain why CREATE, DROP, ALTER, and TRUNCATE are used with an example.
# DDL (Data Definition Language): DDL refers to a set of SQL commands used to define, modify, and delete database structures such as tables, indexes, and views.

# CREATE: Used to create database objects like tables, indexes, or views.

# Example:
# sql
# Copy
# CREATE TABLE students (
#   id INT PRIMARY KEY,
#   name VARCHAR(50),
#   age INT
# );
# DROP: Used to delete database objects like tables, indexes, or views.

# Example:
# sql
# Copy
# DROP TABLE students;
# ALTER: Used to modify an existing database object, such as adding or removing columns in a table.

# Example:
# sql
# Copy
# ALTER TABLE students ADD COLUMN email VARCHAR(100);
# TRUNCATE: Used to remove all rows from a table but keep the structure intact (faster than DELETE).

# Example:
# sql

# TRUNCATE TABLE students;





# Q3. What is DML? Explain INSERT, UPDATE, and DELETE with an example.
# DML (Data Manipulation Language): DML refers to SQL commands that are used to manipulate the data in the database.

# INSERT: Adds new records to a table.

# Example:
# sql

# INSERT INTO students (id, name, age) VALUES (1, 'John Doe', 22);
# UPDATE: Modifies existing records in a table.

# Example:
# sql

# UPDATE students SET age = 23 WHERE id = 1;
# DELETE: Removes records from a table.

# Example:
# sql




# DELETE FROM students WHERE id = 1;
# Q4. What is DQL? Explain SELECT with an example.
# DQL (Data Query Language): DQL refers to SQL commands used for querying the database and retrieving data.

# SELECT: The SELECT statement is used to fetch data from a database table.
# Example:
# sql

# SELECT * FROM students WHERE age > 20;
# This query selects all columns (*) from the students table where the age is greater than 20.




# Q5. Explain Primary Key and Foreign Key.
# Primary Key: A primary key is a field in a table that uniquely identifies each record in that table. It cannot contain NULL values and must be unique.

# Example: In the students table, id can be the primary key.
# Foreign Key: A foreign key is a field (or a collection of fields) in one table that refers to the primary key in another table. It establishes a relationship between the two tables.

# Example: In a courses table, you might have a student_id field, which is a foreign key referring to the id in the students table.






# Q6. Write a Python code to connect MySQL to Python. Explain the cursor() and execute() method.
# python

# import mysql.connector

# # Establishing the connection
# conn = mysql.connector.connect(
#     host="localhost",
#     user="yourusername",
#     password="yourpassword",
#     database="yourdatabase"
# )

# # Creating a cursor object using the cursor() method
# cursor = conn.cursor()

# # Executing an SQL query using the execute() method
# cursor.execute("SELECT * FROM students")

# # Fetching all records from the result of the query
# result = cursor.fetchall()

# # Printing the result
# for row in result:
#     print(row)

# # Closing the connection
# conn.close()
# cursor(): The cursor() method creates a cursor object that allows interaction with the MySQL database. It is used to execute SQL queries and fetch results.

# execute(): The execute() method is used to run an SQL query. It sends the query to the database for processing. For example, cursor.execute("SELECT * FROM students") runs a SELECT query to fetch data from the students table.







# Q7. Give the order of execution of SQL clauses in an SQL query.
# The typical order of execution of SQL clauses in a query is:

# FROM: Identifies the tables involved in the query.
# WHERE: Filters rows based on the condition specified.
# GROUP BY: Groups rows that share a property.
# HAVING: Filters groups based on a condition (like WHERE but for groups).
# SELECT: Specifies the columns to be returned.
# DISTINCT: Removes duplicate rows from the result set.
# ORDER BY: Sorts the result set based on specified columns.
# LIMIT: Limits the number of rows returned (optional).
# For example:

# sql

# SELECT name, COUNT(*) 
# FROM students 
# WHERE age > 20
# GROUP BY name
# HAVING COUNT(*) > 1
# ORDER BY name
# LIMIT 10;