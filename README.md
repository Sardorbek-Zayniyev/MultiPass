# MultiPass Authentication Project

## Overview
MultiPass is a comprehensive authentication project that consolidates multiple authentication methods into a single cohesive system. It leverages Django's robust framework to provide users with flexible and secure login options, such as Google OAuth, Facebook Login, Telegram Login, and more. This project showcases the ability to handle various authentication integrations seamlessly.

---

## Features

1. **Authentication Methods**
 - **Django Allauth**
    - **Google OAuth**: Enables secure Google-based logins.
    - **Facebook OAuth**: Provides seamless integration via Facebook API.
    - **Twitter OAuth**: Allows secure logins via Twitter API.
 - **Email & Password Authentication**: Standard login method with password reset functionality.
 - **Email based two-step verification using Django OTP** for enhanced security.
 - **Telegram Login**: Leveraging Telegram Bot API.
 - **Phone Number with Firebase OTP**: Integrated with Google Firebase for secure OTP verification and Firebase ReCAPTCHA to prevent automated abuse.

2. **Additional Functionalities**
   - Secure handling of sensitive information using environment variables.
   - Modularized design for scalability and maintainability.
   - Enhanced user experience with social login buttons.
   - Integration-ready template designs for custom branding.

---

## Installation

### Prerequisites
- Python 3.8+
- Django 5.x
- PostgreSQL or SQLite
- [Telegram Bot API token](https://core.telegram.org/bots#botfather)
- OAuth credentials for Google, Facebook, and Twitter
- Firebase project set up for phone authentication

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Sardorbek-Zayniyev/multipass-auth.git
   cd multipass-auth
   ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run database migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

6. Start the development server:
    ```bash
    python manage.py runserver
    ```

7. **Setup Environment Variables**:
   Create a `.env` file in the project root and configure the following:

```
TELEGRAM_BOT_API_TOKEN=<Your Telegram Token>
GOOGLE_CLIENT_ID=<Your Google Client ID>
GOOGLE_SECRET=<Your Google Secret>
FACEBOOK_CLIENT_ID=<Your Facebook Client ID>
FACEBOOK_SECRET=<Your Facebook Secret>
TWITTER_CLIENT_ID=<Your Twitter Client ID>
TWITTER_SECRET=<Your Twitter Secret>
FIREBASE_API_KEY=<Your Firebase API Key>
FIREBASE_AUTH_DOMAIN=<Your Firebase Auth Domain>
FIREBASE_PROJECT_ID=<Your Firebase Project ID>
```
The app will be available at `http://127.0.0.1:8000/`.

## Project Structure

```
MultiPass/
├── auth_providers/
│   ├── email_password_auth/
│   ├── facebook_auth/
│   ├── google_auth/
│   ├── phone_number_auth/
│   ├── telegram_auth/
│   └── twitter_oauth/
├── templates/
│   ├── account/
│   ├── alerts.html
│   ├── main.html
│   ├── phone_number.html
│   └── profile.html
├── static/
│   ├── assets/
│   ├── css/
│   ├── img/
│   └── js/
├── manage.py
└── requirements.txt
```

## Usage

1. **User Login**  
   Navigate to `/accounts/login/` for user login. Supported methods include:
   - Email/Password
   - Google
   - Facebook
   - Telegram
   - Phone number-based authentication

2. **Phone-Based Authentication**  
   - Ensure Firebase is set up correctly.  
   - Use the phone number input on the login page to request an OTP.  
   - Enter the OTP to complete the authentication process.  

3. **Admin Panel**  
   Access Django's admin interface at `/admin/`.  

4. **Testing Telegram Authentication**  
   - Set up a bot using [BotFather](https://core.telegram.org/bots#botfather).  
   - Direct users to your bot with the `/start auth` command.  


## Contributing  
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.  


## Acknowledgements  
- [Django](https://www.djangoproject.com/): The robust web framework used for building the project.  
- [Allauth](https://django-allauth.readthedocs.io/en/latest/): Django package that provides seamless user authentication via various methods.  
- [django-otp](https://django-otp-official.readthedocs.io/en/stable/): Used to implement email-based two-step verification for enhanced security.
- [Google Cloud Console](https://console.cloud.google.com/): Used to configure APIs for Google OAuth and Firebase integration.  
- [Facebook Developer Portal](https://developers.facebook.com/): Platform for setting up and managing Facebook API credentials.  
- [Twitter Developer Portal](https://developer.twitter.com/): Platform for managing Twitter API keys to enable secure login functionality.  
- [Telegram Bot API](https://core.telegram.org/bots/api): Used for integrating Telegram-based login functionality.  
- [Firebase](https://firebase.google.com/): Provides services like Firebase OTP and ReCAPTCHA for phone number authentication.  


## Contact  
For any issues or feedback, please open an issue on this repository.  
