from pymongo import MongoClient
import subprocess
import json
import re

def get_database():
	CONNECTION_STRING = "mongodb+srv://<user_name>:<password>@<hostname>/sample_airbnb"
	client = MongoClient(CONNECTION_STRING)
	return client['sample_airbnb']

def mgenerate_values(n):
	final_list = []
	#print(n)
	process="""mgeneratejs '{"childName": "$name", "isNice":"{{chance.bool()}}", "isDelivered":"{{chance.bool()}}"}' -n %d""" % (n)
	output = subprocess.check_output(process, shell=True, universal_newlines = False)
	string_output = output.decode("utf-8")
	#res = string_output[string_output.findAll('{')+1:string_output.find('}')]
	res = re.findall('\{.*?}',string_output)
	for a in res:
		res_obj = json.loads(a)
		#print (res_obj)
		#Convert Bool Strings to real bool values
		res_obj['isNice'] = (json.loads(res_obj['isNice']))
		res_obj['isDelivered'] = (json.loads(res_obj['isDelivered']))
		#print (res_obj['isNice'])

		final_list.append(res_obj)

	return final_list

def welcome_screen():
	print ("Welcome! This utility tool will update existing records in Mongo Sample Database with additional fields you choose using mgeneratejs")

if __name__ == "__main__":
	welcome_screen()
	dbname = get_database()
	coll = dbname["listingsAndReviews"]
	number_of_docs = coll.count_documents({})
	#randomly_generated_values = mgenerate_values(number_of_docs) REAL LINE WE WILL USE SOON
	randomly_generated_values = mgenerate_values(number_of_docs)

	count = 0
	airbnbs = coll.aggregate([{"$project":{"_id":1, "name":1}}])
	for airbnb in airbnbs:
		coll.update_one(
			{"_id":airbnb["_id"]},
			{"$set": randomly_generated_values[count]}
		)
		count +=1
		if((count % 100) == 0): 
			print (str(count) + " documents have been updated")
	print (str(number_of_docs) + " documents have been updated with randomly generated data. Script complete.")

	
	
	
