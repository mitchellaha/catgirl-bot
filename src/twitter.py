from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
from dotenv import load_dotenv
import os

load_dotenv()
apiKey = os.getenv('apiKey')
apiSecret = os.getenv('apiSecret')
token = os.getenv('token')


