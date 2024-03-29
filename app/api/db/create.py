"""
This module creates a database if not already exists.

This main() function from this method should be called
with each start of the program.
"""

import logging
from sqlalchemy import Engine, text


import models

_logger = logging.getLogger(__name__)


def create_db(engine: Engine) -> dict:
    """Creates all tables from ORM models

    :param db: Database session
    :return: A dict with the status and an optional message
    """
    _logger.info("Creating database from ORM models...")
    try:
        # Create schema core
        with engine.connect() as conn:
            conn.execute(text("CREATE SCHEMA IF NOT EXISTS core"))
            conn.commit()

        # Create all tables
        models.Base.metadata.create_all(bind=engine, checkfirst=True)
    except Exception as e:
        _logger.error(f"Creating database from ORM models failed with error {e}")
        raise e
    else:
        _logger.info("Creating database from ORM models finished")
        return {"status": "ok"}
