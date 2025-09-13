import os
import django
from decouple import config
from pymongo import MongoClient

# Setup Django environment (if needed for other functionality)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'elevenlabs_backend.settings')
django.setup()

def seed_audio_data():
    """Seed initial audio data directly to MongoDB"""
    # MongoDB connection
    mongodb_uri = config('MONGODB_URI', default='mongodb://localhost:27017/')
    db_name = config('MONGODB_NAME', default='elevenlabs')
    
    client = MongoClient(mongodb_uri)
    db = client[db_name]
    collection = db['audio_languages']
    
    # Clear existing data
    collection.delete_many({})
    
    # Create sample data
    audio_data = [
        {
            'code': 'en',
            'name': 'English',
            'flag_code': 'US',
            'audio_url': 'https://rawcdn.githack.com/AbdulAhadSiddiqui-0786/my-audio-files/82981bc6b62423f50cd7e049b37f39506f583e86/Peaches%20-%20City%20Sessions%20(1).mp3',
        },
        {
            'code': 'ar',
            'name': 'Arabic',
            'flag_code': 'SA',
            'audio_url': 'https://rawcdn.githack.com/AbdulAhadSiddiqui-0786/my-audio-files/22852b39c69e407b9e231eabd3af5498b3348d67/Humood%20-%20Kun%20Anta%20(Lyrics%20Video)%20-%20Music%20Everyday.mp3',
        }
    ]
    
    # Insert data
    result = collection.insert_many(audio_data)
    
    print(f"Inserted {len(result.inserted_ids)} audio records")
    print("English audio URL:", audio_data[0]['audio_url'])
    print("Arabic audio URL:", audio_data[1]['audio_url'])
    
    client.close()

if __name__ == '__main__':
    seed_audio_data()