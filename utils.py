# utils.py
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def log(msg, level="info"):
    if level == "error":
        logger.error(msg)
    else:
        logger.info(msg)