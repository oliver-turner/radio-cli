from pathlib import Path

from pydantic import BaseModel, HttpUrl

# Define a object class Radio_Stations
# Import the file data/stations-list-raw.json
# map the key value to the object attribute


class RadioStation(BaseModel):
    stationuuid: str
    name: str
    url_resolved: HttpUrl
    homepage: HttpUrl
    country: str
    countrycode: str


json_path = Path(__file__).parent / "data" / "stations-list-raw.json"

stations_json = json_path.read_text()

print(stations_json)
