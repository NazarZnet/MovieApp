from datetime import datetime
from ..extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import validates

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    @validates('username')
    def validate_username(self, key, username):
        if not username:
            raise ValueError('Username is required.')
        if len(username) > 50:
            raise ValueError('Username must be less than or equal to 50 characters.')
        return username

    @validates('email')
    def validate_email(self, key, email):
        if not email:
            raise ValueError('Email is required.')
        if len(email) > 120:
            raise ValueError('Email must be less than or equal to 120 characters.')
        return email

    @validates('password_hash')
    def validate_password_hash(self, key, password):
        if not password:
            raise ValueError('Password is required.')
        if len(password) < 8:
            raise ValueError('Password must be at least 8 characters long.')
        return generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
