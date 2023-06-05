import requests
import json

formula = input("Enter the formula: ")

# Prepare the payload data with the formula
payload = {"formula": formula}

# Send the formula to the server as JSON data
response = requests.post("http://localhost:8000/calculate", json=payload)

# Print the server's response
print(response.text)
