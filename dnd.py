import json
import requests
import sys
from pprint import pprint

response = requests.get("https://www.dnd5eapi.co/api/spells/acid-arrow/")

if response.status_code != 200:
    print("http request failed",response.status_code)
    sys.exit(1)

acid_arrow_response_dict = json.loads(response.text)
pprint(acid_arrow_response_dict)

