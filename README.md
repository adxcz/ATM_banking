# ATM Banking System

A Django-based web application for managing banking operations, including user authentication, transactions, and account management.

## Features
- **User Authentication**: Secure login and signup system.
- **Account Management**: Manage bank accounts and view transaction history.
- **24/7 Accessibility**: Mobile-friendly and responsive design.
- **Customer Support**: Contact page for inquiries.

## Technologies
- **Backend**: Django
- **Frontend**: HTML, CSS
- **Database**: SQLite3
- **Version Control**: Git/GitHub

## Installation
1. **Clone the repository**:
   ```
   git clone https://github.com/adxcz/ATM_banking.git
   cd atm_banking
   
Set up a virtual environment:
```
python -m venv venv
```

source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies:
```
pip install -r requirements.txt
```

Run migrations:
```
python manage.py makemigrations
python manage.py migrate
```

Start the development server:
```
python manage.py runserver
Access the app: Open http://127.0.0.1:8000/ in your browser.
```
Folder Structure
```
      ├── atm_banking         # Main Django app
      ├── static_collected    # Collected static files
      ├── web_project         # Django project settings
      ├── db.sqlite3          # SQLite database
      ├── manage.py           # Django management script
      ├── .gitignore          # Ignored files
      └── requirements.txt    # Dependencies
```
Usage
New Users: Sign up and log in to access your account.
Existing Users: Log in to view account details or manage transactions.
Admin Panel: Access /admin to manage users and data.
Contributing
Fork the repository.


Create a new branch:
```
git checkout -b feature-name
```
Commit your changes:
```
git commit -m "Add feature-name"
```
Push to your branch:
```
git push origin feature-name
```
Open a pull request.
License
This project is licensed under the MIT License.
