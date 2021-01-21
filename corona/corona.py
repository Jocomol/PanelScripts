#!/usr/local/bin python3

import json
import argparse
import requests

parser = argparse.ArgumentParser(description='Reads corona-stats.online and prints out specified numbers.')
parser.add_argument('-c', '--country', help='select country', type=str, default="", action="store")
parser.add_argument('--cases', action='store_true', help="total cases")
parser.add_argument('--casespermil', action='store_true', help="cases per one million")
parser.add_argument('--todaycases', action='store_true', help="todays cases")
parser.add_argument('--deaths', action='store_true', help="total deaths")
parser.add_argument('--todaydeaths', action='store_true', help="todays deaths")
parser.add_argument('--recovered', action='store_true', help="total recovered")
parser.add_argument('--todayrecovered', action='store_true', help="todays recovered")
parser.add_argument('--active', action='store_true', help="active cases")
parser.add_argument('--critical', action='store_true', help="critical cases")

args = parser.parse_args()
data = json.loads(requests.get("https://corona-stats.online/" + args.country + "?format=json").content)

try:
    if args.country != "":
        part = data["data"][0]
    else:
        part = data["worldStats"]

    if args.cases:
        print("{:,}".format(part["cases"]))
    if args.casespermil:
        print("{:,}".format(part["casesPerOneMillion"]))
    if args.todaycases:
        print("{:,}".format(part["todayCases"]))
    if args.deaths:
        print("{:,}".format(part["deaths"]))
    if args.todaydeaths:
        print("{:,}".format(part["todayDeaths"]))
    if args.recovered:
        print("{:,}".format(part["recovered"]))
    if args.todayrecovered:
        print("{:,}".format(part["todayRecovered"]))
    if args.active:
        print("{:,}".format(part["active"]))
    if args.critical:
        print("{:,}".format(part["critical"]))

except Exception:
    pass

