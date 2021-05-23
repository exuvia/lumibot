import os
import pytz

# SOURCE PATH
LUMIBOT_SOURCE_PATH = os.path.abspath(os.path.dirname(__file__))

# GLOBAL PARAMETERS
LUMIBOT_DEFAULT_TIMEZONE = "America/New_York"
LUMIBOT_DEFAULT_PYTZ = pytz.timezone(LUMIBOT_DEFAULT_TIMEZONE)

# CACHING CONFIGURATIONS
LUMIBOT_CACHE_FOLDER = os.path.join(LUMIBOT_SOURCE_PATH, "cache")
LUMIBOT_DATE_INDEX_FILE = os.path.join(LUMIBOT_CACHE_FOLDER, "date_index.pkl")

if not os.path.exists(LUMIBOT_CACHE_FOLDER):
    os.makedirs(LUMIBOT_CACHE_FOLDER)
