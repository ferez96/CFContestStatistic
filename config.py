import logging

# config logging
LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=LOGGING_FORMAT)
logging.getLogger(__name__).info("Logging configured")
