from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session


class BaseRepository:
    def __init__(
        self, session_factory: Callable[..., AbstractContextManager[Session]], model
    ) -> None:
        self.session_factory = session_factory
        self.model = model

    def read_all(self):
        with self.session_factory() as session:
            query = session.query(self.model)
            query = query.all()
            return query

    def create(self, schema):
        with self.session_factory() as session:
            query = self.model(**schema.dict())
            try:
                session.add(query)
                session.commit()
                session.refresh(query)
            except IntegrityError as e:
                raise e
            except Exception as e:
                raise e
            return query

    def update_by_product_name(self, product_name: str, reservation_id: int):
        with self.session_factory() as session:
            session.query(self.model).filter(
                self.model.product_name == product_name
            ).update({"reservation_id": reservation_id})
            session.commit()
