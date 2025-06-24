from app import create_app
from models import db, User, Guest, Episode, Appearance
from datetime import date

app = create_app()

def seed_data():
    with app.app_context():
        
        db.drop_all()
        db.create_all()
        
       
        user = User(username='admin')
        user.set_password('admin123')
        db.session.add(user)
        
        
        guests = [
            Guest(name='John Mulaney', occupation='Comedian'),
            Guest(name='Lin-Manuel Miranda', occupation='Composer'),
            Guest(name='Emma Stone', occupation='Actress'),
            Guest(name='Tom Hanks', occupation='Actor')
        ]
        db.session.add_all(guests)
        
        
        episodes = [
            Episode(date=date(2023, 1, 1), number=101),
            Episode(date=date(2023, 1, 8), number=102),
            Episode(date=date(2023, 1, 15), number=103)
        ]
        db.session.add_all(episodes)
        
       
        appearances = [
            Appearance(rating=5, guest_id=1, episode_id=1),
            Appearance(rating=4, guest_id=2, episode_id=1),
            Appearance(rating=5, guest_id=3, episode_id=2),
            Appearance(rating=3, guest_id=4, episode_id=3)
        ]
        db.session.add_all(appearances)
        
        db.session.commit()
        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_data()