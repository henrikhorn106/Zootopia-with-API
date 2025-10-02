import requests

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
      headers={'X-Api-Key': 'iS3F1u7/UlgFt343Rnq1ig==7gvCdHf7m4mRUgTJ'}
  )

  return res.json()