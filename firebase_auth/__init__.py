import os
import firebase_admin
from firebase_admin import credentials

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cred_path = os.path.normpath(os.path.join(BASE_DIR, 'config', 'firebase-service-account.json'))
if not os.path.exists(cred_path):
    raise RuntimeError(f"Firebase cred not found: {cred_path!r}")

cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)
