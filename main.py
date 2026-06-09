import json

from pyradios import RadioBrowser

rb = RadioBrowser()
results = ""

results = rb.search(
    tag="classical", hidebroken=True, order="votes", bitrate_min=64, countrycode="au"
)

if results:
    print(json.dumps(results, indent=2))
    print("\n")
