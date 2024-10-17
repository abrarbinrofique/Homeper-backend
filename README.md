# Homper - A Home Service System

Homper is a comprehensive platform designed to provide home cleaning, plumbing, and other household services. Users can book services, manage service slots, and contact service providers directly through the platform.

## Features

- **Book Services**: Users can book home services like cleaning, plumbing, and more.
- **Manage Service Slots**: Allocate time slots for services and get reminders.
- **Contact Us**: Users can reach out to the customer support team via the contact form.
- **User Profiles**: Each user has a profile that includes personal information and booking history.

## Technologies Used

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL (Supabase)](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Vercel](https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)
![Cloudinary](https://img.shields.io/badge/Cloudinary-3448C5?style=for-the-badge&logo=cloudinary&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

## Installation

1. Clone the repository:
    ```bash
    git clone git@github.com:abrarbinrofique/Homeper-backend.git
    ```

2. Navigate to the project directory:
    ```bash
    cd Homeper-backendv
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up Supabase as the database (instructions can be found in the Supabase documentation).

5. Run the Django development server:
    ```bash
    python manage.py runserver
    ```

## Project Structure

- **Hommer/**: Core app for handling services and bookings.
- **contactus/**: Handles customer inquiries and feedback.
- **customer/**: Manages user profiles and customer-related data.
- **service/**: Contains logic for home services, service categories, etc.
- **serviceslot/**: Manages service booking slots.
- **staticfiles/**: Static assets like CSS and JS files.

## Requirements

Here are the main dependencies used in this project (as listed in `requirements.txt`):

- Django
- djangorestframework
- django-cloudinary-storage
- django-cors-headers
- psycopg2-binary (for PostgreSQL)
- requests
- and more...

## Deployment

This project is deployed using Vercel and Supabase for database management.

- **Live Frontend**: [Homper Frontend](https://abrarbinrofique.github.io/Homper-frontend/)
- **Live Backend**: Hosted on Vercel


