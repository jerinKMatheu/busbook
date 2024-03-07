# utils.py

from firebase_admin import auth

def send_otp(phone_number):
    if not firebase_admin._apps:
        firebase_admin.initialize_app()  # Initialize Firebase Admin SDK if not already initialized
    session_verification = auth.create_session_verification(phone_number)
    verification_id = session_verification.id
    return verification_id
def verify_otp(verification_id, otp):
    auth.PhoneAuthProvider.verify_session_cookie(verification_id, otp)
    return True  # OTP is valid