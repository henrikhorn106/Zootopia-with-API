"""
This module provides functionality to load data from a file, format specific
data into HTML, and generate an HTML file based on template replacement.

Functions:
- load_data: Loads JSON data from a specified file.
- create_animals_html: Fetches and formats animal data into HTML list item strings.
- generate_html: Generates an HTML file by replacing placeholders in a
  template with formatted animal data.
"""
import json
import requests


def get_animal_data(animal_name):
    """Gets animal data from the API."""

    res = requests.get(
        "https://api.api-ninjas.com/v1/animals",
        params={"name": animal_name},
        headers={'X-Api-Key': 'iS3F1u7/UlgFt343Rnq1ig==7gvCdHf7m4mRUgTJ'}
    )

    return res.json()


def serialize_animal(animal_obj):
    """Serializes an animal object into a string."""

    output = ''
    output += '<li class="cards__item">'
    output += (f'<div class="card__title">{animal_obj['name']} '
               f'({animal_obj['taxonomy']['scientific_name']})</div>\n')
    if 'slogan' in animal_obj['characteristics']:
        output += f'<p class="card__text"><em>{animal_obj['characteristics']['slogan']}</em></p>'
    output += '<div class="card__text">'
    output += '<ul>'
    output += f"<li><strong>Diet:</strong> {animal_obj['characteristics']['diet']}</li>\n"
    output += f"<li><strong>Location:</strong> {animal_obj['locations'][0]}</li>\n"
    if 'type' in animal_obj['characteristics']:
        output += f"<li><strong>Type:</strong> {animal_obj['characteristics']['type']}</li>\n"
    output += '</ul>'
    output += "</div>"
    output += "</li>"

    return output


def create_animals_html(animals_data):
    """Fetches and formats animal data into HTML list item strings."""

    output = ""
    for animal in animals_data:
        output += serialize_animal(animal)

    return output


def generate_html(data):
    """Generates an HTML file by replacing placeholders in a template with formatted animal data."""

    with open('animals_template.html', 'r', encoding="utf-8") as file:
        template = file.read()

    template = template.replace("__REPLACE_ANIMALS_INFO__", create_animals_html(data))

    with open('animals.html', 'w', encoding="utf-8") as file:
        file.write(template)


def filter_data(data, skin_type):
    """Filters data by skin type."""

    data = [animal for animal in data if animal['characteristics']['skin_type'] == skin_type]
    return data


def get_skin_types(data):
    """Returns a set of all available skin types."""

    skin_types = set()
    for animal in data:
        skin_types.add(animal['characteristics']['skin_type'])

    sorted_skin_types = sorted(list(skin_types))
    return sorted_skin_types


def main():
    """Main function."""
    animal_name = input("Enter a name of an animal: ").strip()

    # Get skin type
    data = get_animal_data(animal_name)
    skin_types = get_skin_types(data)

    print("The following skin types are available:")
    for skin_type in skin_types:
        print(f"- {skin_type}")

    # Filter for skin type
    while True:
        skin_type_input = input("\nSelect a skin type you want to filter for: ").strip()

        if skin_type_input in skin_types:
            break

        print("Invalid skin type. Please try again.")

    filtered_data = filter_data(data, skin_type_input)

    generate_html(filtered_data)
    print("Website was successfully generated to the file animals.html.")


if __name__ == "__main__":
    main()
