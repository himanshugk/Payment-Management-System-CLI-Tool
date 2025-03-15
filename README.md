# Payment-Management-System-CLI-Tool
Simple payment system where we can simply add user and make payments.

Project Overview
The Payment Management System CLI Tool is a command-line interface (CLI) application built using Python. It allows users to manage payments, track transactions, and generate payment reports. The system simulates basic payment functionalities and is a great starting point for learning Python and applying Object-Oriented Programming (OOP) principles in a real-world scenario.

Features
User Management: Add and manage users.
Payment Records: Record payments made by users.
Balance Tracking: Track user balances and transaction history.
Transaction History: View a history of payments.
Report Generation: Generate reports of transactions in a text-based format.


Usage
1. User Registration
Register a new user by entering their name and initial balance.
2. Payment Process
Add a payment by specifying the user and the payment amount.
3. Viewing Transaction History
View the transaction history of a particular user or all users.
4. Balance Overview
Check the current balance of a user.
5. Generate Report
Generate a report for all transactions made within the system.


Here's the Directory Structure

payment_system/              IT JUST TELLS FILE WORKING
0. │
1. ├── main.py                # CLI Handler
2. ├── payment.py             # Class for Payment object
3. ├── file_handler.py        # File operations (Save/Load)
4. └── payments.json          # Data storage (auto-created)




FOLLOWING COMMAND TO RUN THIS CODE IN TERMINAL.
1. python main.py --add 101 5000 Alice
2. python main.py --view

How it store values for simple understanding or for non coders
For first command:
101 is for ID
5000 is for MONEY
Alice is for user (If user is not listed it will list it or add it)

For second comman:
It will show the payment details.
