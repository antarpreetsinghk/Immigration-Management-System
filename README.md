# Immigration Management System

A comprehensive Django-based web application designed to streamline operations for immigration consultancies. This system facilitates the management of client leads, formal applications, payments, and branch-specific data.

## Features

### 1. Lead Management
*   **Track Potential Clients**: Record and manage details of potential clients (`Leads`) including contact information, qualifications, experience, and desired destination country.
*   **Status Tracking**: Monitor lead status through stages: `Pending`, `Approved`, or `Rejected`.
*   **CRUD Operations**: Create, view, update, and delete lead records.
*   **Search**: Easily search for specific leads.

### 2. Application Management
*   **Detailed Records**: Manage formal applications with extensive details such as File Number, UIC Number, and Case Type.
*   **Progress Tracking**: Automatically calculates and visualizes the progress of an application based on the application date and estimated completion date.
*   **Time Estimation**: Provides dynamic estimates of remaining time (e.g., "2 Weeks", "3 Months").
*   **Image Handling**: Upload and automatically resize applicant images for consistent display.

### 3. Payment Tracking
*   **Record Payments**: Log payments against specific applications.
*   **History**: View payment history for financial tracking.

### 4. Branch Management
*   **Organization**: Categorize leads and applications by specific branches.
*   **Filtering**: View data filtered by branch.

### 5. User Dashboard
*   **Central Hub**: A dashboard view to oversee system activities.
*   **Authentication**: Secure login and logout functionality for staff access.

## Technology Stack

*   **Backend Framework**: Django (Python)
*   **Database**: SQLite (Default)
*   **Image Processing**: Pillow (PIL)
*   **Frontend**: Django Templates, HTML, CSS

## Installation & Setup

### Prerequisites
*   Python 3.x installed on your system.

### Steps

1.  **Clone the Repository**
    ```bash
    git clone <repository-url>
    cd immigration
    ```

2.  **Create a Virtual Environment (Recommended)**
    ```bash
    python -m venv env
    # Activate on Windows
    .\env\Scripts\activate
    # Activate on macOS/Linux
    source env/bin/activate
    ```

3.  **Install Dependencies**
    Since this project relies on Django and Pillow, install them using pip:
    ```bash
    pip install django pillow
    ```

4.  **Apply Migrations**
    Set up the database schema:
    ```bash
    python manage.py migrate
    ```

5.  **Create a Superuser**
    Create an admin account to access the backend:
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the Development Server**
    ```bash
    python manage.py runserver
    ```

7.  **Access the Application**
    *   Open your browser and navigate to `http://127.0.0.1:8000/`.
    *   Log in using the superuser credentials you created.

## Project Structure

*   `dashboard/`: Contains the main application logic (models, views, forms, templates).
*   `immigration/`: Project configuration settings.
*   `media/`: Stores user-uploaded files (e.g., application images).
*   `templates/`: HTML templates for the user interface.

## Contributing

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/YourFeature`).
3.  Commit your changes (`git commit -m 'Add some feature'`).
4.  Push to the branch (`git push origin feature/YourFeature`).
5.  Open a Pull Request.
