# Corporate Asset Tracking System

The Corporate Asset Tracking System is a web application designed to help companies manage their corporate assets efficiently. It allows companies to track devices such as phones, tablets, laptops, and other equipment that are assigned to employees.

## Features

- User authentication: Users can sign up, sign in, and sign out.
- Asset management: Companies can add, view, update, and delete assets.
- Employee management: Companies can manage employees, their departments, and assigned assets.
- Asset assignment: Admins can assign assets to employees and track assignments.
- API documentation: Comprehensive API documentation for developers to integrate with the system.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Junayed54/Asset-Tracking-System.git
```

## Install dependencies Navigate to the project directory
cd asset_tracking
## Install dependencies

pip install -r requirments.txt
    
## Run database migrations:
python manage.py migrate


## Start the development server:
python manage.py runserver
## Usage


- Open a web browser and go to http://localhost:8000.
- Log in with your administrator credentials.
- Navigate through the dashboard to manage assets, assign them to employees, and generate reports.


## API Documentation

The Corporate Asset Tracking System provides a RESTful API for accessing and managing assets programmatically. For API documentation, visit the /api/docs/ endpoint after starting the server.