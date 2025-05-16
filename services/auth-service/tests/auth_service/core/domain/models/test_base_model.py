"""test BaseModel entity module"""

from datetime import datetime
from uuid import uuid4

from auth_service.core.domain.models import BaseModel


def test_base_model_init():
    """test BaseModel model init"""
    id_ = uuid4()
    created_at = datetime.now()
    update_at = datetime.now()

    _base_model = BaseModel(
        id_=id_,
        created_at=created_at,
        update_at=update_at,
    )

    assert _base_model.id_ == id_
    assert _base_model.created_at == created_at
    assert _base_model.update_at == update_at


def test_base_model_from_dict():
    """test base model from dict"""
    init_dict = {
        "id_": uuid4(),
        "created_at": datetime.now(),
        "update_at": datetime.now(),
    }

    _base_model = BaseModel.from_dict(init_dict)
    assert _base_model.id_ == init_dict.get("id_")
    assert _base_model.created_at == init_dict.get("created_at")
    assert _base_model.update_at == init_dict.get("update_at")
