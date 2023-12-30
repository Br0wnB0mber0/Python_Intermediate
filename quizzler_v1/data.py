import requests
# You can add a "category" by adding that key to the parameters dictionary with the category number you can pull from the API.
# Category 18 is computer related questions
# Parameters for the request we are going to send the API
parameters = {
    "amount": 10,
    "type": "boolean"
}
# Response we get from the Open Trivia Database, using the API URL and the parameters as defined above
response = requests.get(url="https://opentdb.com/api.php?", params=parameters)
# Raises an exception if there is a problem with the response
response.raise_for_status()
# Stores the JSON data with the results of the response. Here, the results key is the question and answer data we pull from the API
question_data = response.json()['results']

