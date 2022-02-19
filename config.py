import logging
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# config logging
LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=LOGGING_FORMAT)
logging.getLogger(__name__).info("Logging configured")

MONGODB_DRIVER = os.getenv("MONGODB_DRIVER")
MONGODB_USERNAME = os.getenv("MONGODB_USERNAME")
MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")
MONGODB_HOST = os.getenv("MONGODB_HOST")
MONGODB_DATABASE = os.getenv("MONGODB_DATABASE", "bkac_profiles")
MONGODB_CONNECTION_URI = f"{MONGODB_DRIVER}://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@{MONGODB_HOST}/{MONGODB_DATABASE}?retryWrites=true&w=majority"
