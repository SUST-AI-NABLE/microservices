"""test User entity module"""

from datetime import date, datetime
from uuid import uuid4

import pytest

from auth_service.core.domain.errors import BaseModelUnexpectedKeyArgumentError
from auth_service.core.domain.models import User


def test_user_model_init():
    """test user model init"""
    id_ = uuid4()
    created_at = datetime.now()
    update_at = datetime.now()
    first_name = "John"
    last_name = "DOE"
    birthday = date.today()
    password = "test"
    email = "test@test.com"
    phone_number = "002290152445460"
    country = None

    _user = User(
        id_=id_,
        first_name=first_name,
        last_name=last_name,
        birthday=birthday,
        password=password,
        created_at=created_at,
        update_at=update_at,
        roles=None,
        email=email,
        phone_number=phone_number,
        country=country,
    )

    assert _user.first_name == first_name
    assert _user.last_name == last_name
    assert _user.birthday == birthday
    assert _user.password == password
    assert _user.roles is None


def test_user_model_from_dict():
    """test user model from dict"""
    init_dict = {
        "id_": uuid4(),
        "first_name": "John",
        "last_name": "DOE",
        "birthday": date.today(),
        "password": "test",
        "created_at": datetime.now(),
        "update_at": datetime.now(),
        "roles": None,
        "email": "test@test.com",
        "phone_number": "002290152445460",
        "country": None,
    }
    _user = User.from_dict(init_dict)
    assert _user.id_ == init_dict.get("id_")
    assert _user.first_name == init_dict.get("first_name")
    assert _user.last_name == init_dict.get("last_name")
    assert _user.birthday == init_dict.get("birthday")
    assert _user.password == init_dict.get("password")
    assert _user.created_at == init_dict.get("created_at")
    assert _user.update_at == init_dict.get("update_at")
    assert _user.roles == init_dict.get("roles")
    assert _user.email == init_dict.get("email")
    assert _user.phone_number == init_dict.get("phone_number")
    assert _user.country == init_dict.get("country")


def test_user_model_to_dict():
    """test user model to_dict method"""
    user_data = {
        "id_": uuid4(),
        "first_name": "John",
        "last_name": "DOE",
        "birthday": date.today(),
        "password": "test",
        "created_at": datetime.now(),
        "update_at": datetime.now(),
        "roles": None,
        "email": "test@test.com",
        "phone_number": "002290152445460",
        "country": None,
    }

    user = User.from_dict(user_data)
    user_dict = user.to_dict()

    assert user_dict["id_"] == user_data["id_"]
    assert user_dict["first_name"] == user_data["first_name"]
    assert user_dict["last_name"] == user_data["last_name"]
    assert user_dict["birthday"] == user_data["birthday"]
    assert user_dict["password"] == user_data["password"]
    assert user_dict["created_at"] == user_data["created_at"]
    assert user_dict["update_at"] == user_data["update_at"]
    assert user_dict["roles"] == user_data["roles"]
    assert user_dict["email"] == user_data["email"]
    assert user_dict["phone_number"] == user_data["phone_number"]
    assert user_dict["country"] == user_data["country"]


def test_user_model_unexpected_keys():
    """test user model raises error with unexpected keys"""
    user_data = {
        "id_": uuid4(),
        "first_name": "John",
        "last_name": "DOE",
        "birthday": date.today(),
        "password": "test",
        "created_at": datetime.now(),
        "update_at": datetime.now(),
        "roles": None,
        "email": "test@test.com",
        "phone_number": "002290152445460",
        "country": None,
        "unexpected_key": "unexpected_value",
    }

    with pytest.raises(BaseException) as error:
        _ = User.from_dict(user_data)

    assert error.errisinstance(BaseModelUnexpectedKeyArgumentError)
