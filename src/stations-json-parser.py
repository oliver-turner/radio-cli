from pathlib import Path

from pydantic import BaseModel, HttpUrl, TypeAdapter

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

stations_adapter = TypeAdapter(list[RadioStation])
stations: list[RadioStation] = stations_adapter.validate_json(stations_json)

for station in stations:
    print(
        f" id: {station.stationuuid}\n name: {station.name} \n url: {station.url_resolved} \n"
    )
