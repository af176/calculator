import requests

while True:
    formula = input("Enter the formula (or 'q' to quit): ")

    if formula == 'q':
        break

    response = requests.post("http://localhost:8000/calculate", json={"formula": formula})

    if response.status_code == 200:
        print("Result:", response.text)
    else:
        print("Error
