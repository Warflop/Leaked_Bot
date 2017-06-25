from pymongo import MongoClient

#Script to import file leak.txt to into mongodb

client = MongoClient()
db = client.leaks
collection = db.leaked
f = open('leak.txt')
text = f.readlines()
for emails in text:
	email = emails.rpartition(':')[0]
	x = emails.rpartition(':')[2]
	senha = x.rstrip('\n')
	text_file_doc = {"email" : email, "password": password}
	collection.insert(text_file_doc)
