from pathlib import Path

from pydantic import BaseModel, HttpUrl, TypeAdapter


class RadioStation(BaseModel):
    stationuuid: str
    name: str
    url_resolved: HttpUrl
    homepage: HttpUrl
    country: str
    countrycode: str
    codec: str
    bitrate: int


def parse_json() -> list[RadioStation]:
    json_path = Path(__file__).parent / "data" / "stations_list_raw.json"
    stations_json = json_path.read_text()

    stations_adapter = TypeAdapter(list[RadioStation])
    stations: list[RadioStation] = stations_adapter.validate_json(stations_json)

    return stations
