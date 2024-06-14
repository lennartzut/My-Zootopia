import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)

animals_data = load_data("animals_data.json")


def fox_data(data):
    """Prints Name, Location, Diet and Type of every fox"""
    for fox in data:
        fox_name = fox.get("name")
        fox_location = fox.get("locations")[0]
        fox_diet = fox.get("characteristics", {}).get("diet")
        fox_type = fox.get("characteristics", {}).get("type")
        if fox_name is not None:
            print(f"Name: {fox_name}")
        if fox_diet is not None:
            print(f"Diet: {fox_diet}")
        if fox_location is not None:
            print(f"Location: {fox_location}")
        if fox_type is not None:
            print(f"Type: {fox_type}")
        print()

fox_data(animals_data)
