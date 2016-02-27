import unittest
from config import *
from smappdragon import MongoCollection

class TestMongoCollection(unittest.TestCase):

	def test_mongo_top_entities_returns_dict(self):
		collection = MongoCollection(config['mongo']['host'], config['mongo']['port'], config['mongo']['user'], config['mongo']['password'], config['mongo']['database'], config['mongo']['collection'])
		returndict = collection.top_entities({'hashtags':5})
		self.assertTrue(isinstance(returndict, dict))

	def test_mongo_top_entities_returns_hashtags(self):
		collection = MongoCollection(config['mongo']['host'], config['mongo']['port'], config['mongo']['user'], config['mongo']['password'], config['mongo']['database'], config['mongo']['collection'])
		returndict = collection.top_entities({'hashtags':5})
		self.assertTrue(returndict['hashtags'])

	def test_mongo_top_entities_returns_hashtags_and_media(self):
		collection = MongoCollection(config['mongo']['host'], config['mongo']['port'], config['mongo']['user'], config['mongo']['password'], config['mongo']['database'], config['mongo']['collection'])
		returndict = collection.top_entities({'user_mentions':5, 'media':3})
		self.assertTrue(returndict['user_mentions'] and returndict['media'])

	def test_mongo_top_entities_returns_counts(self):
		collection = MongoCollection(config['mongo']['host'], config['mongo']['port'], config['mongo']['user'], config['mongo']['password'], config['mongo']['database'], config['mongo']['collection'])
		returndict = collection.top_entities({'urls':5, 'symbols':3})
		if len(returndict['urls']) > 0:
			self.assertTrue(len(returndict['urls']) == 5)
		if len(returndict['symbols']) > 0:
			self.assertTrue(len(returndict['symbols']) == 3)

if __name__ == '__main__':
	unittest.main()

'''
read about twitter entities here:
https://dev.twitter.com/overview/api/entities-in-twitter-objects
'''

