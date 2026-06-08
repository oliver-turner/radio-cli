import json

from pyradios import RadioBrowser

rb = RadioBrowser()
results = ""
stations = ["fip", "Swiss Jazz", "somaFM groove", "Paradise main"]

for station in stations:
    results = rb.search(name=station, hidebroken=True, order="votes")

    if results:
        print(json.dumps(results, indent=2))
        print("\n")
