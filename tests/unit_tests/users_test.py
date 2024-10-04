from core import db
from core.models.users import User


def create_user(email, user_name):
    user = User(email=email, username=user_name)
    db.session.add(user)

def test_get_user_by_email():
    email = "test_user@gmail.com"
    user_name = "test_user"
    create_user(email, user_name)

    user = User.get_by_email(email)
    assert user is not None
    assert user.email == email









