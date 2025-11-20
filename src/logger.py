import logging
import os
from datetime import datetime

# Create logs directory
LOG_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

# Log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Full log file path (CORRECT)
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="[ %(asctime)s ] %(levelname)s - %(name)s - Line %(lineno)d - %(message)s"
)

if __name__=="__main__": 
    logging.info("Logging has started")
# logger = logging.getLogger("mlproject")
