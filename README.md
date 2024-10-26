# Homper - A Home Service System
<img src="https://github.com/abrarbinrofique/Homeper-backend/blob/main/homper.png">

Homper is a comprehensive platform designed to provide home cleaning, plumbing, and other household services. Users can book services, manage service slots, and contact service providers directly through the platform.

## Features

- **User Signup and Email Confirmation**: New users register and receive an email confirmation link. Upon clicking the link, they are redirected to the login page.
- **Role-Based Access**:
  - **Customers** can view service details, post reviews, and book services.
  - **Admins** can add services and manage users.
  - **Admin Promotion**: Admins can promote other users to admin status, allowing them to add new services.
- **Book Services**: Users can book home services like cleaning, plumbing, and more.
- **Manage Service Slots**: Allocate time slots for services and receive reminders.
- **Contact Us**: Users can reach out to customer support via the contact form.
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
    cd Homeper-backend
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Configure the environment variables for email settings and database credentials.

5. Set up Supabase as the database (refer to Supabase documentation).

6. Run the Django development server:
    ```bash
    python manage.py runserver
    ```

## API Endpoints

### Service Endpoints
- List of Services: `https://homeper-backend.vercel.app/service/list/`
- See Service Reviews: `https://homeper-backend.vercel.app/service/review/`
- Give a Service Review: `https://homeper-backend.vercel.app/service/review/?service_id=${param}`

### Customer Endpoints
- Customer Profile Information: `https://homeper-backend.vercel.app/customer/${customerId}/`
- List of Customers: `https://homeper-backend.vercel.app/customer/`
- Make a User Admin: `https://homeper-backend.vercel.app/customer/makeadmin/${customerId}/`

### Service Slot Endpoints
- See Services Booked by Customer: `https://homeper-backend.vercel.app/serviceslot/?customer_id=${customerId}`
- Book a Service: `https://homeper-backend.vercel.app/serviceslot/`

## Requirements

Dependencies include:
- Django
- djangorestframework
- django-cloudinary-storage
- django-cors-headers
- psycopg2-binary (for PostgreSQL)
- requests

## Deployment

This project is deployed using Vercel and Supabase.

- **Live Frontend**: [Homper Frontend](https://abrarbinrofique.github.io/Homper-frontend/)
- **Live Backend**: Hosted on Vercel

## Authentication Flow

1. **Signup**: Users register and receive a confirmation email.
2. **Email Confirmation**: Upon clicking the link, users are redirected to the login page.
3. **Login**: Once logged in, users can access services based on their role (Admin/Customer).
