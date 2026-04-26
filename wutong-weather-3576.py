import requests
import json
import argparse

def get_weather(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    response = requests.get(url)
    return response.json()

def main():
    parser = argparse.ArgumentParser(description="Weather CLI tool with 7-day forecast")
    parser.add_argument("--key", required=True, help="OpenWeatherMap API key")
    parser.add_argument("--loc", required=True, help="Location to query for weather")
    parser.add_argument("--json", action="store_true", help="Output in JSON format")
    parser.add_argument("--output", type=str, help="Specify an output file")

    args = parser.parse_args()

    try:
        data = get_weather(args.key, args.loc)
        if args.json:
            with open(args.output, 'w') as f:
                json.dump(data, f, indent=4)
        else:
            print(json.dumps(data))

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()