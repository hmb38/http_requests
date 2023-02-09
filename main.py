import json
import requests
import sys
from pprint import pprint

response = requests.get("https://raw.githubusercontent.com/dariusk/corpora/master/data/science/planets.json")

if response.status_code != 200:
    print("http request failed",response.status_code)
    sys.exit(1)

planets_dict = json.loads(response.text)
pprint(planets_dict)

planets_moons_list = planets_dict["planets"]
planets_list = [p["name"] for p in planets_moons_list]

def make_moon_tuple(p):
    return (p["name"] , len(p["moons"]))

moons_count = [make_moon_tuple(p) for p in planets_moons_list]
print(moons_count)
