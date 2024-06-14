import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)

animals_data = load_data("animals_data.json")


def fox_data(data):
    """Prints Name, Location, Diet and Type of every fox"""
    fox_data_string = ""
    for fox in data:
        fox_name = fox.get("name")
        fox_location = fox.get("locations")[0]
        fox_diet = fox.get("characteristics", {}).get("diet")
        fox_type = fox.get("characteristics", {}).get("type")
        if fox_name is not None:
            fox_data_string += f"Name: {fox_name}\n"
        if fox_diet is not None:
            fox_data_string += f"Diet: {fox_diet}\n"
        if fox_location is not None:
            fox_data_string += f"Location: {fox_location}\n"
        if fox_type is not None:
            fox_data_string += f"Type: {fox_type}\n"
        fox_data_string += "\n"
    return(fox_data_string)


# Reads local HTML file
with open("animals_template.html", "r") as file:
    html_content = file.read()


# Replace text in HTML with data string
html_new_content = html_content.replace("__REPLACE_ANIMALS_INFO__", fox_data(animals_data))


# Write new HTML file
with open("animals.html", "w") as file:
    file.write(html_new_content)
