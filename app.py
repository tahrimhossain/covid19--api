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


class DailyNewConfirmed(Resource):

	def get(self,country):
		dailyNewConfirmed = database.confirmedGraphData.find_one({"_id":country})
		if dailyNewConfirmed == None:
			abort(404,message = "Data not found")
		else:
			return dailyNewConfirmed["data"]	


class DailyNewDeaths(Resource):

	def get(self,country):
		dailyNewDeath = database.deathGraphData.find_one({"_id":country})
		if dailyNewDeath == None:
			abort(404,message = "Data not found")
		else:
			return dailyNewDeath["data"]	


api.add_resource(Summary,"/summary")
api.add_resource(DailyNewConfirmed,"/dailynewconfirmed/<string:country>")
api.add_resource(DailyNewDeaths,"/dailynewdeath/<string:country>")

if __name__ == "__main__": 
	app.run()