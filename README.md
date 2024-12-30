# User Authentication System 🛡️

## Project Overview

This project is a secure user authentication system built with Django. It includes secure login and registration functionality, allowing users to sign up for an account, log in securely, and access protected routes only after successful authentication. The system leverages Django's built-in encryption mechanisms for password security.

## Features ✨

- **User Registration:** Users can create an account with a unique username and secure password.
- **User Login:** Authenticated users can securely log in using their credentials.
- **Password Encryption:** Utilizes Django's built-in password hashing mechanism for secure storage.
- **Role-Based Access Control:** Different user roles have different access permissions.

## Technologies Used 🛠️

- **Django:** Web framework for rapid development.
- **SQLite:** Lightweight database for development purposes.

## Installation 🚀

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

2. **Create a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

## Usage 📚

1. **Register a new account:**
    - Navigate to `/register` and fill out the registration form.
2. **Log in to your account:**
    - Navigate to `/login` and enter your credentials.
3. **Access protected routes:**
    - After logging in, navigate to routes that require authentication.

## Project Structure 🗂️

```markdown
    .
    ├── manage.py
    ├── mysite
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── auth_app
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── templates
    │   ├── base.html
    │   ├── login.html
    │   └── register.html
    └── requirements.txt
```

---

## 📜 License
This project is licensed under the [MIT License](LICENSE).

---

## 👥 Acknowledgments
- **Django Documentation**: For extensive guidance.
- **CSS Tricks**: For helping style the application.

---
