import argparse
from payment import Payment
from file_handler import load_payments, save_payments

def add_payment(payment_id, amount, payer):
    payments = load_payments()
    new_payment = Payment(payment_id, amount, payer)
    payments.append(new_payment.to_dict())
    save_payments(payments)
    print("✅ Payment added successfully.")

def view_payments():
    payments = load_payments()
    for p in payments:
        print(p)

def search_payment(payment_id):
    payments = load_payments()
    found = [p for p in payments if p['payment_id'] == payment_id]
    if found:
        print(found[0])
    else:
        print("❌ Payment not found.")

# Argument parser setup
parser = argparse.ArgumentParser(description="Payment Management System")
parser.add_argument("--add", nargs=3, metavar=('ID', 'AMOUNT', 'PAYER'), help="Add a new payment")
parser.add_argument("--view", action="store_true", help="View all payments")
parser.add_argument("--search", metavar='ID', help="Search payment by ID")

args = parser.parse_args()

# Function calling based on arguments
if args.add:
    payment_id, amount, payer = args.add
    try:
        amount = float(amount)  # Convert amount to float safely
        add_payment(payment_id, amount, payer)
    except ValueError:
        print("❌ Amount must be a number.")
elif args.view:
    view_payments()
elif args.search:
    search_payment(args.search)
else:
    print("⚙️ Use --help to see available commands.")
