class Config:
    """Set Flask configuration vars from .env file."""

    # Load in enviornemnt variables
    TESTING = False
    FLASK_DEBUG = True
    SECRET_KEY = "thisismysecretkey"
    SERVER = '192.168.0.109'
