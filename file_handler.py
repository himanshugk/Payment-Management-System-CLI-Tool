import json

def load_payments(filename="payments.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_payments(payments, filename="payments.json"):
    with open(filename, "w") as file:
        json.dump(payments, file, indent=4)
