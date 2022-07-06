from enum import unique
from config import app_config, app_active
from app import db
from sqlalchemy import func

class Market(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(30), unique=True, nullable=False)
    description = db.Column(db.Text(), unique=False, nullable=False)
    date_create = db.Column(db.DateTime(6), 
                        default=db.func.current_timestamp(),
                        nullable = False)
    def __repr__(self) -> str:
        return self.code

    def get_total_markets(self):
        try:
            res = db.session.query(func.count(Market.id)).first()
        except Exception as e:
            res = []
            print(e)
        finally:
            db.session.close()
            return res
