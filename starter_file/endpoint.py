import requests
import json

# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
scoring_uri = 'http://c88a41ff-3763-4990-a868-77fd6f0e3296.southcentralus.azurecontainer.io/score'

# Two sets of data to score, so we get two results back
data = {"data":
        [
          {
            "Column1": "vhigh",
            "Column2": "vhigh",
            "Column3": 2,
            "Column4": 2,
            "Column5": "small",
            "Column6": "low"
          },
          {
            "Column1": "high",
            "Column2": "med",
            "Column3": 4,
            "Column4": 4,
            "Column5": "med",
            "Column6": "med"
          }
        ]
    }

# Set the content type
headers = {'Content-Type': 'application/json'}

# Make the request and display the response
input_data = json.dumps(data)
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())
