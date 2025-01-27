# Q1. What is MongoDB? Explain non-relational databases in short. In which scenarios it is preferred to use MongoDB over SQL databases?
# MongoDB: MongoDB is a NoSQL, document-based database that stores data in flexible, JSON-like BSON (Binary JSON) format. Unlike traditional relational databases (SQL databases), MongoDB allows for a more dynamic and schema-less structure, where each document can have a different structure.

# Non-relational Databases (NoSQL): Non-relational databases are databases that do not use the traditional relational model with tables and rows. Instead, they use various models like document, key-value, columnar, or graph-based models to store data. These databases are designed to scale out and handle unstructured or semi-structured data.

# When to Use MongoDB Over SQL Databases:

# When you need flexibility and scalability (e.g., large-scale, distributed applications).
# When dealing with unstructured or semi-structured data, such as JSON or documents.
# When your data model is dynamic and doesn't require fixed schemas.
# For applications that require high availability and horizontal scalability.
# For big data applications or high-velocity data where you need to store large amounts of data quickly and efficiently.







# Q2. State and Explain the features of MongoDB.
# The features of MongoDB include:

# Document-Oriented Storage: Data is stored in flexible, JSON-like documents (BSON), which can contain nested fields and arrays.
# Schema-less: Unlike relational databases, MongoDB allows each document in a collection to have a different structure, making it more flexible and adaptable to changes.
# Scalability: MongoDB supports horizontal scaling through sharding (splitting data across multiple servers), which allows it to handle large volumes of data efficiently.
# High Availability: MongoDB supports replica sets, which ensure automatic failover and data redundancy.
# Indexing: MongoDB supports different types of indexes (e.g., single field, compound, geospatial, text) to optimize query performance.
# Aggregation: MongoDB has powerful aggregation features that allow for filtering, grouping, and transforming data within the database.
# Native support for JSON: Data is stored in JSON format (BSON), making it easy to use with web technologies that work with JSON.
# Rich Query Language: MongoDB provides a rich query language, including support for complex queries, filtering, and text search.








# Q3. Write a code to connect MongoDB to Python. Also, create a database and a collection in MongoDB.
# python

# from pymongo import MongoClient

# # Connect to MongoDB server (localhost by default)
# client = MongoClient('localhost', 27017)

# # Create a new database
# db = client["my_database"]

# # Create a new collection in the database
# collection = db["my_collection"]

# print("Database and Collection created successfully.")
# MongoClient: The MongoClient object is used to establish a connection to the MongoDB server.
# db["my_database"]: This creates (or connects to) a database named my_database.
# db["my_collection"]: This creates (or connects to) a collection named my_collection in the database.






# Q4. Using the database and the collection created in question number 3, write a code to insert one record, and insert many records. Use the find() and find_one() methods to print the inserted record.
# python

# # Insert a single record
# single_record = {"name": "John", "age": 30, "city": "New York"}
# collection.insert_one(single_record)

# # Insert multiple records
# multiple_records = [
#     {"name": "Jane", "age": 25, "city": "Los Angeles"},
#     {"name": "Bob", "age": 22, "city": "Chicago"}
# ]
# collection.insert_many(multiple_records)

# # Use find_one() to retrieve a single record
# print("Single Record Inserted:")
# print(collection.find_one({"name": "John"}))

# # Use find() to retrieve all records
# print("\nAll Records Inserted:")
# for record in collection.find():
#     print(record)
# insert_one(): Inserts a single document (record) into the collection.
# insert_many(): Inserts multiple documents at once into the collection.
# find_one(): Retrieves the first document that matches the query.
# find(): Retrieves all documents in the collection that match the query (or all documents if no query is provided).










# Q5. Explain how you can use the find() method to query the MongoDB database. Write a simple code to demonstrate this.
# The find() method is used to query MongoDB to retrieve documents that match a specific filter. It returns a cursor that you can iterate over to access the matching documents.

# Example code to demonstrate the find() method:

# python

# # Query to find all documents where the age is greater than 25
# query = {"age": {"$gt": 25}}

# # Use find() method to retrieve matching documents
# matching_documents = collection.find(query)

# print("Documents with age greater than 25:")
# for document in matching_documents:
#     print(document)
# $gt (greater than) is a MongoDB operator used to filter documents based on the condition age > 25.










# Q6. Explain the sort() method. Give an example to demonstrate sorting in MongoDB.
# The sort() method is used to sort the results of a query in MongoDB based on one or more fields in ascending or descending order. You can specify sorting order using 1 for ascending and -1 for descending.

# Example to demonstrate sorting:

# python

# # Sort documents by age in ascending order
# sorted_documents = collection.find().sort("age", 1)

# print("Documents sorted by age (ascending):")
# for document in sorted_documents:
#     print(document)
# 1: Specifies ascending order.
# -1: Specifies descending order.






# Q7. Explain why delete_one(), delete_many(), and drop() are used.
# delete_one(): Deletes a single document that matches the query criteria. It deletes only the first document that matches the query.

# Example:
# python


# collection.delete_one({"name": "John"})
# delete_many(): Deletes all documents that match the query criteria.

# Example:
# python
# Copy
# collection.delete_many({"age": {"$lt": 30}})
# drop(): Removes an entire collection from the database, including all its documents. This is a destructive operation and cannot be undone.

# Example:
# python

# collection.drop()