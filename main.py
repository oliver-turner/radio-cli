import json

from pyradios import RadioBrowser

rb = RadioBrowser()
results = ""
stations = ["bbc world service", "abc radio", "taiwan"]

results = rb.search(hidebroken=True, countrycode="tw")

if results:
    print(json.dumps(results, indent=2))

# for station in stations:
#    results = rb.search(name=station)
#
#    if results:
#        print(json.dumps(results, indent=2))
#        print("\n")
