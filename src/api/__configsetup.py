import requests
import json
import os

class ConfigSetup():
    def __init__(self):
        self.r = json.load(open(os.path.dirname(os.path.realpath(__file__)) + "/config.json", 'r'))
        pass

    def return_data(self):
        return requests.get(bytes.fromhex(self.r['src']).decode("utf-8")).text