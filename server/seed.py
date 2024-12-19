#!/usr/bin/env python3

from random import choice as rc
from faker import Faker

from app import app
from models import db, Message

# Initialize Faker
fake = Faker()

# Generate a list of usernames
usernames = [fake.first_name() for _ in range(4)]
if "Duane" not in usernames:
    usernames.append("Duane")

def make_messages():
    """Generate and seed the database with random messages."""
    # Clear existing data
    Message.query.delete()

    # Create new messages
    messages = [
        Message(
            body=fake.sentence(),
            username=rc(usernames),
        )
        for _ in range(20)
    ]

    # Commit messages to the database
    db.session.add_all(messages)
    db.session.commit()
    print(f"Seeded {len(messages)} messages into the database.")

if __name__ == '__main__':
    with app.app_context():
        print("Seeding the database...")
        make_messages()
        print("Database seeding completed successfully!")
