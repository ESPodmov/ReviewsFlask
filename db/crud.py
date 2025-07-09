from contextlib import contextmanager
from datetime import datetime
from sqlalchemy.orm import Session
from .base import SessionLocal, engine
from .models import Review
from sqlalchemy.exc import SQLAlchemyError
from schemas.reviews import ReviewFullRead


class Database:
    @contextmanager
    def session_scope(self):
        session = SessionLocal()
        try:
            yield session
            session.commit()
        except SQLAlchemyError:
            session.rollback()
            raise
        finally:
            session.close()

    def add_review(self, text: str, sentiment: str) -> ReviewFullRead:
        with self.session_scope() as session:
            review = Review(
                text=text,
                sentiment=sentiment,
                created_at=datetime.utcnow().isoformat()
            )
            session.add(review)
            session.flush()
            session.refresh(review)
            return ReviewFullRead.model_validate(review)

    def get_reviews(self, sentiment: str = None) -> list[ReviewFullRead]:
        with self.session_scope() as session:
            query = session.query(Review)
            if sentiment:
                query = query.filter(Review.sentiment == sentiment)
            return list(map(ReviewFullRead.model_validate, query.all()))
