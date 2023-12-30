import requests
# You can add a "category" by adding that key to the parameters dictionary with the category number you can pull from the API.
# Category 18 is computer related questions
parameters = {
    "amount": 10,
    "type": "boolean"
}
response = requests.get(url="https://opentdb.com/api.php?", params=parameters)
response.raise_for_status()
question_data = response.json()['results']

