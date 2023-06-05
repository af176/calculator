HTTP Calculator
This repository contains an HTTP calculator application that allows clients to send formulas to a server using the HTTP protocol and receive the calculated result. The server evaluates the formulas based on a set of valid characters: numbers [0-9], +, -, *, /, A, Z.


Accepts formulas as strings from clients via HTTP requests.
Handles basic arithmetic operations: addition, subtraction, multiplication, and division.
Supports parentheses-like characters (A and Z) for grouping expressions.
Validates input formulas for invalid characters and unclosed brackets.

Usage
Start the server by running the server.py file.

python server.py
The server will listen for HTTP requests on http://localhost:8000.

Run the client.py file to send a formula to the server.

python client.py
Enter the desired formula when prompted. The client will send an HTTP request to the server.

The server will evaluate the formula and return the calculated result or an error message as the response.

Examples
Valid formulas:

1 + 2 (Result: 3)
2 * (3 + 4) (Result: 14)
3 * A5 + 2 * 2Z + 7 (Result: 34)
Invalid formulas:

A1 + 2 (Error: The brackets are not closed)

