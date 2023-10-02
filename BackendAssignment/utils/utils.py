"""
    Utility file
"""
import uuid


def get_random_username(email):
    """
    return: username based on the the email and random number
    """
    return f"{email.split('@')[0].lower()}_{uuid.uuid4().hex[:10]}"


def normalize_email(email):
    """
    return: normalize email
    """
    return email.strip().lower()
