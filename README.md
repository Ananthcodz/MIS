# Micro Irrigation Reporting System (MIR)

A web application built with Django for tracking and visualizing data related to the Pradhan Mantri Krishi Sinchayee Yojana (PMKSY) micro-irrigation initiative.

## Technical Overview

This project implements a full-stack web application with:
- Django backend (version 2.2.2)
- MySQL database integration
- Custom HTML/CSS frontend
- Materialize CSS framework for UI components

## Project Structure

```
mir1/
├── manage.py              # Django management script
├── mir1/                  # Project configuration package
│   ├── __init__.py        # PyMySQL configuration
│   ├── settings.py        # Django settings (DB, installed apps, middleware)
│   ├── urls.py            # URL routing configuration
│   └── wsgi.py            # WSGI application definition
├── mirbase/               # Main application package
│   ├── __init__.py
│   ├── admin.py           # Django admin configuration
│   ├── apps.py            # Application configuration
│   ├── models.py          # Database models (to be implemented)
│   ├── tests.py           # Test cases
│   └── views.py           # View controllers
└── templates/             # Frontend templates
    ├── base1.html         # Base template with common structure
    ├── contacts.html      # Team contact information
    ├── home.html          # Dashboard with data visualization
    ├── login.html         # User authentication
    ├── register.html      # User registration
    ├── register2.html     # Additional registration form
    └── reports.html       # Dynamic reports with filtering
```

## Technical Implementation

### Backend Configuration

#### Database Setup
MySQL integration using PyMySQL:
```python
# mir1/__init__.py
import pymysql
pymysql.install_as_MySQLdb()
```

Database configuration in settings.py:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mir',
        'PORT': '3306',
        'USER': '*****',
        'PASSWORD': '********',
        'HOST': 'localhost'
    }
}
```

#### URL Routing
```python
# mir1/urls.py
from django.contrib import admin
from django.urls import path
from mirbase.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name="Home"),
]
```

#### View Implementation
```python
# mirbase/views.py
from django.shortcuts import render, redirect

def home_view(request):
    return render(request, "home.html", {})
```

### Frontend Architecture

#### Template Inheritance
The application uses Django's template inheritance system with a base template:
```html
<!-- base1.html -->
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title></title>
</head>
<body>
{% block content %}
    
{% endblock content %}
</body>
</html>
```

#### Frontend Features

1. **Responsive Navigation**
   - Consistent navbar across all pages
   - Mobile-friendly design using Materialize CSS

2. **Dynamic Content Loading**
   - JavaScript implementation for report filtering
   - Content display based on dropdown selection

3. **Form Validation**
   - Client-side validation for registration form
   - Password confirmation checks

4. **Interactive UI Elements**
   - Image carousel on homepage using JavaScript
   - Dropdown menus for report selection
   - Striped tables for better readability

5. **CSS Implementation**
   - Custom styling with CSS variables
   - Media queries for responsive design
   - Animation effects for interactive elements

#### JavaScript Implementation Example
```javascript
// Dynamic content switching based on dropdown selection
function dropdownoption(option) {
    if(option == 1) {
        document.getElementById("statereports").style.display = "block";
        document.getElementById("benefits").style.display = "none";  
        document.getElementById("water").style.display = "none";  
        document.getElementById("area").style.display = "none";        
    }
    // Additional options...
}
```

## Development Setup

### Prerequisites
- Python 3.6+
- MySQL Server
- pip (Python package manager)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/micro-irrigation-reporting.git
   cd micro-irrigation-reporting
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install django==2.2.2 pymysql
   ```

4. **Database setup**
   ```bash
   # Create MySQL database
   mysql -u root -p
   > CREATE DATABASE mir;
   > exit
   
   # Run Django migrations
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the application**
   - Open browser at: http://127.0.0.1:8000/

## Technical Challenges and Solutions

### Database Integration
- Used PyMySQL to connect Django with MySQL
- Implemented custom database configuration in settings.py

### Frontend Rendering
- Leveraged Django's template system for dynamic content
- Combined server-side rendering with client-side interactivity

### State Management
- Implemented form validation and data persistence
- Used JavaScript for client-side state management

## Future Technical Improvements

1. **API Development**
   - Create RESTful API endpoints using Django REST Framework
   - Enable data access for external applications

2. **Authentication Enhancement**
   - Implement JWT-based authentication
   - Add OAuth support for social login

3. **Database Optimization**
   - Create models for all data entities
   - Implement proper indexing and query optimization

4. **Frontend Modernization**
   - Convert to a React-based frontend
   - Implement state management with Redux

5. **Testing Infrastructure**
   - Add unit tests for views and models
   - Implement CI/CD pipeline with GitHub Actions

## License

This project is licensed under the [MIT License](LICENSE).
