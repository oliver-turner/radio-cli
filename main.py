from src.stations_json_parser import parse_json


def main():
    my_stations = parse_json()
    print("=== My Stations ===\n")
    for station in my_stations:
        print(
            f"Name: {station.name}\nCountry: {station.country}\nQuality: {station.codec} ({station.bitrate}Kpbs)\nURL: {station.url_resolved}\n"
        )


if __name__ == "__main__":
    main()
