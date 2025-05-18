import firebase_admin
from firebase_admin import credentials, auth

# Initialize Firebase Admin SDK (if not already initialized)
cred = credentials.Certificate("firebasejson.json")
firebase_admin.initialize_app(cred)

uid = "ZAkxetv1KHTdopCW4cgXK8FYqxz1"  # Replace with your actual user UID

custom_token = auth.create_custom_token(uid)
print(custom_token.decode('utf-8'))  # This is your custom token
