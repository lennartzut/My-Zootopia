import requests

API_KEY = "HedPHbPSZtALl0SQRFp4fQ==qOKjRD7GpmnbzRsl"


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
    api_url = (f"https://api.api-ninjas.com/v1/animals?name="
               f"{animal_name}")
    headers = {"X-Api-Key": API_KEY}
    try:
        response = requests.get(api_url, headers=headers)
        if response.status_code == requests.codes.ok:
            return response.json()
        else:
            print("Error:", response.status_code, response.json())
            return None
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None
