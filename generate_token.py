import firebase_admin
from firebase_admin import credentials, auth

# Initialize Firebase Admin SDK only once
def initialize_firebase():
    try:
        # Check if already initialized
        firebase_admin.get_app()
    except ValueError:
        cred = credentials.Certificate('firebasejson.json')  # Replace with your JSON file path
        firebase_admin.initialize_app(cred)

def generate_custom_token(uid):
    initialize_firebase()
    try:
        # Create a custom token for the specified user ID
        custom_token = auth.create_custom_token(uid)
        # custom_token is bytes, decode to string
        return custom_token.decode('utf-8')
    except Exception as e:
        print(f"Error generating custom token: {e}")
        return None

if __name__ == "__main__":
    user_uid = input("Enter user UID: ")
    token = generate_custom_token(user_uid)
    if token:
        print("Custom token generated:")
        print(token)
    else:
        print("Failed to generate custom token.")
