# CRMatic

Designed and developed a Customer Relationship Management (CRM) system using Python and Django to streamline client and agent management, enabling businesses to manage customer interactions more efficiently.

Deployed on Pythonanywhere: [CRMatic](https://thenamelessone.pythonanywhere.com/)

# Features

Client Management: Add, update, and track client information seamlessly.

Agent Coordination: Assign agents to clients and monitor their activities.

Category Organization: Categorize clients for better segmentation and targeting.

User Authentication: Secure login and registration system for users.

Responsive Design: Accessible on various devices with a user-friendly interface.


# Installation

To set up CRMatic locally, follow these steps:

Clone the repository:

git clone https://github.com/ABDULKARIM-BOUTA/CRMatic.git

cd CRMatic


Create a virtual environment:

python -m venv env

env\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Apply migrations:

python manage.py migrate


Run the development server:

python manage.py runserver


Access the application at http://127.0.0.1:8000/


# Project Structure

  _crm/: Core Django project settings and configurations.

  accounts/: Handles user authentication and profile management.

  agents/: Manages agent-related functionalities.

  clients/: Manages client data and interactions.

  categories/: Organizes clients into categories.

  templates/: HTML templates for rendering views.

  static/: Static files like CSS and JavaScript.


# Technologies Used

Python, Django, AllAuth, HTML, MySQL, Tailwind
