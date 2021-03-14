from data import db, initialize
from main import app

if __name__ == "__main__":
    with app.app_context():
        initialize(app)
        # Run this file directly to create the database tables.
        print ("Creating database tables...")
        db.create_all()
        print ("Done!")