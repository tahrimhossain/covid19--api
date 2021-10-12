from flask import Flask
from flask_restful import Api,Resource,reqparse,abort
from pymongo import MongoClient
from bson import ObjectId
from bson import json_util
import json
import os

app = Flask(__name__)
api = Api(app)

mongoURL = os.environ.get('MONGO_URL')



client = MongoClient(mongoURL)
database = client["covidDatabse"]


class Summary(Resource):
	
	def get(self):
		
		summary = database.summary.find_one({"_id":"summary"})

		if summary == None:
			abort(404,message = "Data not found")
		else:
			return summary	


class AllDailyNewConfirmed(Resource):

	def get(self,country):
		allDailyNewConfirmed = database.confirmedGraphData.find_one({"_id":country})
		if allDailyNewConfirmed == None:
			abort(404,message = "Data not found")
		else:
			return allDailyNewConfirmed["data"]	


class AllDailyNewDeaths(Resource):

	def get(self,country):
		allDailyNewDeath = database.deathGraphData.find_one({"_id":country})
		if allDailyNewDeath == None:
			abort(404,message = "Data not found")
		else:
			return allDailyNewDeath["data"]	

class CountryInfo(Resource):

	def get(self,country):
		info = database.summary.find_one({"_id":"summary"},{"Countries":{'$elemMatch':{"Country":country}}})
		if "Countries" in info and len(info["Countries"]) == 1:
			return info["Countries"][0]
		else:
			abort(404,message = "Data not found")	

api.add_resource(Summary,"/summary")
api.add_resource(AllDailyNewConfirmed,"/all/confirmed/<string:country>")
api.add_resource(AllDailyNewDeaths,"/all/death/<string:country>")
api.add_resource(CountryInfo,"/country/<string:country>")

if __name__ == "__main__": 
	app.run()