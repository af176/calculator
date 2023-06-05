from flask import Flask, request

app = Flask(__name__)


def calculate_formula(formula):
    formula = formula.replace(" ", "")  # Remove spaces from the formula

    if any(char for char in formula if char not in "0123456789+-*/AZ"):
        return "Error: Invalid characters in the formula"

    stack = []
    operators = set(['+', '-', '*', '/'])
    error_message = "Invalid formula: Invalid brackets"

    for char in formula:
        if char == 'A':
            stack.append(char)
        elif char == 'Z':
            if len(stack) == 0 or 'A' not in stack:
                return error_message
            while len(stack) >= 3:
                while len(stack) >= 3 and stack[-2] in operators:
                    operand2 = stack.pop()
                    operator = stack.pop()
                    operand1 = stack.pop()
                    result = perform_operation(operator, operand1, operand2)
                    if result is None:
                        return "Invalid formula: Division by zero"
                    stack.append(result)
                if 'A' in stack:
                    while stack[-1] != 'A' and len(stack) != 0:
                        stack2 = [stack.pop()]
                    stack.pop()
                    while len(stack2) != 0:
                        stack.append(stack2.pop())
        elif char.isdigit():
            stack.append(int(char))
        elif char in operators:
            stack.append(char)

    if 'A' in stack or 'Z' in stack:
        return error_message

    return evaluate_stack(stack)


def perform_operation(operator, operand1, operand2):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        if operand2 == 0:
            return None  # Division by zero error
        return operand1 / operand2


def evaluate_stack(stack):
    while len(stack) > 1:
        if len(stack) == 2:
            a = stack.pop()
            op = stack.pop()
            if op == '-':
                stack.append(-a)
        elif len(stack) >= 3:
            a = stack.pop()
            op = stack.pop()
            b = stack.pop()
            result = perform_operation(op, b, a)
            if result is None:
                return "Invalid formula: Division by zero"
            stack.append(result)
        else:
            return "Invalid formula: Invalid brackets"

    return stack[0]


@app.route("/calculate", methods=["POST"])
def calculate():
    formula = request.json.get("formula")

    if formula is None:
        return "Error: No formula provided"

    result = calculate_formula(formula)
    return str(result)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
