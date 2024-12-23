from firebase_admin import credentials, initialize_app, auth
import os

# Path to your Firebase service account key
SERVICE_ACCOUNT_KEY_PATH = os.path.join(
    os.path.dirname(__file__), 'serviceAccountKey.json'
)

# Initialize Firebase Admin SDK
cred = credentials.Certificate(SERVICE_ACCOUNT_KEY_PATH)
firebase_app = initialize_app(cred)

# Firebase auth object
firebase_auth = auth
