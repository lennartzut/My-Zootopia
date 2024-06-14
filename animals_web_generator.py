import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)

animals_data = load_data("animals_data.json")


def animal_data(data):
    """Prints Name, Location, Diet and Type of every animal"""
    animal_data_string = ""
    for animal in data:
        animal_name = animal.get("name")
        animal_location = animal.get("locations")[0]
        animal_diet = animal.get("characteristics", {}).get("diet")
        animal_type = animal.get("characteristics", {}).get("type")
        animal_data_string += "<li class=\"cards__item\">\n"
        if animal_name is not None:
            animal_data_string += f"\t<div class=\"card__title\">{animal_name}</div>\n"
        animal_data_string += "\t<p class=\"card__text\">\n"
        if animal_diet is not None:
            animal_data_string += f"\t\t<strong>Diet:</strong> {animal_diet}<br/>\n"
        if animal_location is not None:
            animal_data_string += f"\t\t<strong>Location:</strong> {animal_location}<br/>\n"
        if animal_type is not None:
            animal_data_string += f"\t\t<strong>Type:</strong> {animal_type}<br/>\n"
        animal_data_string += "\t</p>\n"
        animal_data_string += "</li>"
        animal_data_string += "\n"
    return(animal_data_string)


# Reads local HTML file
with open("animals_template.html", "r") as file:
    html_content = file.read()


# Replace text in HTML with data string
html_new_content = html_content.replace("__REPLACE_ANIMALS_INFO__", animal_data(animals_data))


# Write new HTML file
with open("animals.html", "w") as file:
    file.write(html_new_content)
