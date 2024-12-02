# ATM Banking System

Greetings! This repository is intended for the final project of the ATM Banking System group of CSIT327 section G5 of the Cebu Institute of Technology-University to be submitted to Mr. Joemari Amparo.

The members/contributors for this project are so named:

---

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [ERD](#erd)
- [UI/UX](#uiux)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## Features

- **User Authentication**: Sign up and log in securely.
- **Account Management**: View account balances, transaction history, and manage banking services.
- **Responsive Design**: Optimized for desktop and mobile devices.
- **Customer Support**: Easily reach out for assistance via the contact page.

---

## Technologies

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS
- **Database**: SQLite3
- **Version Control**: Git, GitHub
- **Deployment**: Localhost for development, can be deployed on any server.

---

## Installation

Follow the steps below to set up the project locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/adxcz/ATM_banking.git
   cd atm_banking
Set up a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run database migrations:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Start the development server:

bash
Copy code
python manage.py runserver
Access the app: Open http://127.0.0.1:8000/ in your browser to start using the application.

Usage
New Users: Sign up and log in to start managing your account.
Existing Users: Log in to access your account details and manage transactions.
Admin Panel: Access the Django admin panel via /admin to manage users and application data.
Folder Structure
plaintext
Copy code
├── atm_banking         # Main Django app
├── static_collected    # Collected static files for deployment
├── web_project         # Django project settings and configurations
├── db.sqlite3          # SQLite database file
├── manage.py           # Django management commands script
├── .gitignore          # Git ignore file for version control
└── requirements.txt    # List of dependencies for the project
ERD
Add your Entity-Relationship Diagram (ERD) image or description here:

(Insert the ERD diagram showing the relationships between users, transactions, and accounts.)

UI/UX
Add your User Interface/User Experience (UI/UX) screenshots or descriptions here:

(Insert images of the application's user interface, such as login screens, dashboard, and transaction views.)

Contributing
We welcome contributions! If you want to improve the project, follow these steps:

Fork the repository to your own GitHub account.

Clone your fork to your local machine:

bash
Copy code
git clone https://github.com/your-username/ATM_banking.git
cd ATM_banking
Create a new branch for your feature:

bash
Copy code
git checkout -b feature-name
Make your changes and commit them:

bash
Copy code
git commit -m "Add feature-name"
Push your changes to your forked repository:

bash
Copy code
git push origin feature-name
Open a pull request to the main repository to propose your changes.

License
This project is licensed under the MIT License.

Acknowledgements
Django Framework: Django
SQLite Database: SQLite
GitHub: GitHub
