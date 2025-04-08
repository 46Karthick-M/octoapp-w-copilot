# OctoFit Tracker

## Project Overview

The OctoFit Tracker is a fitness tracking application designed for Mergington High School. It aims to engage students in physical activities outside of school by providing a fun and competitive platform for tracking workouts, earning achievements, and fostering a sense of community through friendly competition.

## Directory Structure

The project is organized into two main directories: `backend` and `frontend`.

### Backend

The backend is built using Python and Django. It includes the following components:

- **app**: Contains the core application logic, including models, serializers, views, and URL routing.
- **manage.py**: A command-line utility for managing the Django project.
- **requirements.txt**: Lists the Python packages required for the backend application.
- **settings**: Contains configuration files for different environments (base, development, production).

### Frontend

The frontend is developed using React.js. It includes:

- **public**: Contains the main HTML file for the application.
- **src**: Contains the React components and styles for the application.

## Setup Instructions

### Backend Setup

1. Navigate to the `backend` directory:
   ```
   cd octofit-tracker/backend
   ```

2. Create a Python virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

5. Run the development server:
   ```
   python manage.py runserver
   ```

### Frontend Setup

1. Navigate to the `frontend` directory:
   ```
   cd octofit-tracker/frontend
   ```

2. Install the necessary dependencies (assuming you have Node.js and npm installed):
   ```
   npm install
   ```

3. Start the development server:
   ```
   npm start
   ```

## Contributing

Contributions to the OctoFit Tracker project are welcome! Please feel free to submit issues or pull requests.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.