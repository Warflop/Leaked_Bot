from pymongo import MongoClient
import hug

#Webservice hug (https://github.com/timothycrosley/hug)
#use command: hug -f consult.py

@hug.get()
def consult(query):
	client = MongoClient()
	db = client.leaks
	collection = db.dropbox
	status = collection.find_one({"email" : query}, {"_id" : 0, "email" : 0})
	retorno = status["password"].strip()
	return retorno
