import sys
import os
import traceback

from app import create_app, db
from app.models.login import User

try:
    app = create_app()
    with app.app_context():
        email = 'superadmin@example.com'
        if not User.query.filter_by(email=email).first():
            new_user = User(username='superadmin', email=email, password='superadmin123')
            db.session.add(new_user)
            db.session.commit()
            print(f"User {email} created successfully.")
        else:
            print("User already exists.")
except Exception as e:
    with open('error.log', 'w') as f:
        f.write(traceback.format_exc())
    print("Error saved to error.log")
