from pymongo import MongoClient

#Lo que esta afuera del main son variables globales
#Access to remote cluster
MONGO_URI = ""


def db_connect(MONGO_URI,db_name,col_name):
	#Connect to MongoClient:
	client = MongoClient(MONGO_URI) 
	database = client[db_name]
	collection = database[col_name]
	return collection

def db_insert_user(collection,user):
	return collection.insert_one(user)

#If query is empty, it will return all the collection
def db_find_all(collection, query={}):
	return collection.find(query)

if __name__ == '__main__':
    #print("MongoClient imported successfully!")
    #Create a datadabe called mi_app
    #database = client['mi_app']

    #Create a collection called users
    #users = database['users']

    #usuario_demo = {
    #	"user": "Cristopher Paredes",
    #	"email": "cristopher.pl451@gmail.com"
    #}
    #users.insert_one(usuario_demo)