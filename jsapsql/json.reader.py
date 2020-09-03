import json
import os

# Path to config.json file
CWD = os.getcwd()
JSON_CONFIG_FILE_PATH = '%s/%s' % (CWD, 'config.json')

# Dictionary holding config.json
CONFIG_PROPERTIES = {}

# Open Config.json, pare
try:
    with open(JSON_CONFIG_FILE_PATH) as data_file:
        CONFIG_PROPERTIES = json.load(data_file)
