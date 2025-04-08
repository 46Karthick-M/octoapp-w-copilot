# Documentation for Monafit Tracker

## Overview

The Monafit Tracker is a fitness application developed for Mona High School, aimed at promoting physical activity among students. The application allows users to log their workouts, track their progress, and engage in friendly competition with peers. This document outlines the key features, technical specifications, and setup instructions for the Monafit Tracker.

## Key Features

1. **User Registration and Profiles**: Students can create accounts and maintain personal profiles to track their fitness journey.
2. **Activity Logging**: Users can log various types of physical activities, including running, walking, cycling, and strength training.
3. **Achievement Badges**: The app rewards users with badges for reaching specific milestones, encouraging continued engagement.
4. **Team Competitions**: Students can form teams and compete in fitness challenges, fostering a sense of community and motivation.
5. **Progress Tracking**: Users can view their activity history and progress through a user-friendly dashboard.

## Technical Specifications

- **Frontend**: Built using React.js for a responsive and interactive user experience.
- **Backend**: Developed with Python and Django REST Framework to handle API requests and manage data.
- **Database**: Utilizes MongoDB for storing user data and activity logs.
- **Authentication**: Secure user authentication is implemented to protect user data and privacy.

## Setup Instructions

### Prerequisites

- Python 3.x
- Node.js and npm
- MongoDB

### Backend Setup

1. Clone the repository:
   ```
   git clone <repository-url>
   cd octofit-tracker/backend
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Run migrations to set up the database:
   ```
   python manage.py migrate
   ```

5. Start the development server:
   ```
   python manage.py runserver
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```
   cd ../frontend
   ```

2. Install the necessary dependencies:
   ```
   npm install
   ```

3. Start the React application:
   ```
   npm start
   ```

## Conclusion

The Monafit Tracker serves as a foundational model for the OctoFit Tracker application, providing essential features and a robust technical framework. By leveraging the insights and structure from the Monafit Tracker, the OctoFit Tracker aims to enhance student engagement in physical fitness at Mergington High School.