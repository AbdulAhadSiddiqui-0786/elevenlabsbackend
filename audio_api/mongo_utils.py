from pymongo import MongoClient
from django.conf import settings
import os

def get_mongo_client():
    """Create and return a MongoDB client"""
    # Get MongoDB URI from environment variable or settings
    mongodb_uri = os.environ.get('MONGODB_URI', getattr(settings, 'MONGODB_URI', 'mongodb://localhost:27017/'))
    return MongoClient(mongodb_uri)

def get_mongo_db():
    """Get the MongoDB database instance"""
    client = get_mongo_client()
    # Get database name from environment variable or settings
    db_name = os.environ.get('MONGODB_NAME', getattr(settings, 'MONGODB_NAME', 'elevenlabs'))
    return client[db_name]

def get_audio_collection():
    """Get the audio collection from MongoDB"""
    db = get_mongo_db()
    return db['audio_languages']