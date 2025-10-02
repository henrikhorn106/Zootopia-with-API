import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
      'name': ...,
      'taxonomy': {
        ...
      },
      'locations': [
        ...
      ],
      'characteristics': {
        ...
      }
    },
    """

    res = requests.get(
        "https://api.api-ninjas.com/v1/animals",
        params={"name": animal_name},
        headers={'X-Api-Key': API_KEY}
    )

    return res.json()
