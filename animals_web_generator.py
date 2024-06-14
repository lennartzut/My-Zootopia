import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal):
    """Serializes the animal data"""
    output = ""
    animal_name = animal.get("name")
    animal_location = animal.get("locations")[0]
    animal_diet = animal.get("characteristics", {}).get("diet")
    animal_type = animal.get("characteristics", {}).get("type")
    output += "<li class=\"cards__item\">\n"
    if animal_name is not None:
        output += f"\t<div class=\"card__title\">{animal_name}</div>\n"
    output += "\t<p class=\"card__text\">\n"
    if animal_diet is not None:
        output += f"\t\t<strong>Diet:</strong> {animal_diet}<br/>\n"
    if animal_location is not None:
        output += f"\t\t<strong>Location:</strong> {animal_location}<br/>\n"
    if animal_type is not None:
        output += f"\t\t<strong>Type:</strong> {animal_type}<br/>\n"
    output += "\t</p>\n"
    output += "</li>"
    output += "\n"
    return output


def animal_data(data):
    """Creates an instance of animal data to be serialized"""
    output = ""
    for animal in data:
        output += serialize_animal(animal)
    return output


# Load data from JSON file
animals_data = load_data("animals_data.json")


# Reads local HTML file
with open("animals_template.html", "r") as file:
    html_content = file.read()


# Replace placeholder in template with animal data
html_new_content = html_content.replace("__REPLACE_ANIMALS_INFO__", animal_data(animals_data))


# Write new HTML content to a file
with open("animals.html", "w") as file:
    file.write(html_new_content)
