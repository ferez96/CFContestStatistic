import logging
from typing import Optional
from pymongo import MongoClient
from pymongo.database import Database

import config

_logger = logging.getLogger(__name__)


def _get_db() -> Optional[Database]:
    if not config.MONGODB_CONNECTION_URI:
        _logger.error("MONGODB_CONNECTION_URI is not set")
        return None

    client = MongoClient(config.MONGODB_CONNECTION_URI)
    return client[config.MONGODB_DATABASE]


def get_db() -> Optional[Database]:
    return _get_db()
