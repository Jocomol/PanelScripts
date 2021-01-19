#!/usr/local/bin python3

import json
import argparse

gradefile_path = "./example.json"

with open(gradefile_path) as json_file:
    data = json.load(json_file)


crser = argparse.ArgumentParser(description='Script to add grades and to calculate grades')
parser.add_argument('-a', '--add', help='adds grade', type=float, default=0.0, action="store")
parser.add_argument('-c', '--course', help='specifies course', type=int, default=0, action="store")
parser.add_argument("-l", '--list', help='lists all grades', action='store_true')
parser.add_argument("-C", "--courses", help="list all courses", action='store_true')asesPerOneMillion = data["data"][0]["casesPerOneMillion"]

cases = data["data"][0]["cases"]
todayCases = data["data"][0]["todayCases"]
deaths = data["data"][0]["deaths"]
todayDeaths = data["data"][0]["todayDeaths"]
recovered = data["data"][0]["recovered"]
todayRecovered = data["data"][0]["todayRecovered"]
active = data["data"][0]["active"]
critical = data["data"][0]["critical"]
