from pymongo import *
import json

class User(json.JSONEncoder):
    def __init__(self, username, password, city, country):
        self.user_id = 0
        self.login = username
        self.password = password
        self.city = city
        self.country = country
    def check_password(self, passwd):
        return self.password == passwd
    def to_DICT(self):
        return {"login": self.login, 'password':self.password, 'city':self.city, 'country':self.country}
    def from_DICT(self,userDict):
        user = User(userDict['login'], userDict['password'],userDict['city'],userDict['country'])
        return user

    def to_JSON(self):
        return json.dumps(self, default=lambda self: self.__dict__, sort_keys=True, indent=4)
    def from_JSON(self,obj):
        login = ''
        password = ''
        city = ''
        country = ''
        user = None
        try:
            user = User(obj['login'],obj['password'], obj['city'], obj['country'])
        except:
            pass
        return user

class Mongo_Abstract(object):
    def __init__(self,hostname='localhost',localport=27017,sample_collection='test_collection'):
        self.host=hostname
        self.port=localport
        self.collection=sample_collection

    def try_connect(self):
        try:
            self.client = MongoClient()
            self.client = MongoClient('localhost', 27017)
            
            self.db     = self.client.MyDB
            self.collection = self.db.My_collection
            self.dicts = self.collection.posts
        except errors.ConnectionFailure:
            raise Exception("Please check if Mongo DB is up and running")

    def deserialize_User(self,user, username):
        try:
            obj = self.dicts.find_one({"login" : username})
            user = user.from_JSON(obj)
        except :
            user = None

    def serialize_User(self, user):
        try:
            dctResult = user.to_DICT()
            user_id = self.dicts.insert_one(dctResult)
        except:
            raise Exception("Error storing data to db")
            strResult = None

    def find_user(self,strFilterCity="Dummy"):
        try:
            for dictionary in self.dicts.find({"city": {strFilterCity}}).sort("login"):
                user = User("Dummy",'123','123','123')
                user = user.from_JSON(dictionary)
        except :
            raise Exception("Not able to query the database")
        return user

    def serialize_all_users(self,users):
        for user in users:
            self.serialize_User(user)
        return True

    def deserialize_all_users(self):
        users = {}
        try:
            results = list(self.dicts.find())
            for result in results:
                user = User("Dummy",'123','123','123')
                user = user.from_JSON(result)
                #user.from_DICT(result)
                if user is not None:
                    users[user.login] = user
        except:
            raise Exception("Not able to retrieve data")
        return users
    def sort_filter_all_users(self,sortCriteria):
        users = {}
        print(sortCriteria)
        filteredResults = self.dicts.find({"city":sortCriteria}).sort("country")
        print(filteredResults)
        #results = self.dicts.find({"city":{"$eq":sortCriteria}}).sort("country")
        for result in filteredResults:
            user = User("Dummy",'123','123','123')
            user = user.from_DICT(result)
            if user is not None:
                users[user.login] = user
        #print(users)
        return users
    
    def sort_users_by(self,sortCriteria):
        users = {}
        results = list(self.dicts.find().sort(sortCriteria))
        for result in results:
            user = User("Dummy",'123','123','123')
            user = user.from_JSON(result)
            if user is not None:
                users[sortCriteria] = user
        return users


