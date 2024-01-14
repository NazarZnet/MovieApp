from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

jwt=JWTManager()
db=SQLAlchemy()

@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    from .models.user import User
    
    identity = jwt_data["sub"]
    return User.query.filter_by(id=identity).one_or_none()
