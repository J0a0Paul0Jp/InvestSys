from enum import unique
from config import app_config, app_active
from model.Market import Market
from app import db
from sqlalchemy.orm import relationship
from sqlalchemy import func

class Asset(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     code = db.Column(db.String(30), unique=True, nullable=False)
     description = db.Column(db.Text(), unique=False, nullable=False)
     date_create = db.Column(db.DateTime(6), 
                            default=db.func.current_timestamp(),
                            nullable = False)
     market_id = db.Column(db.Integer, db.ForeignKey(Market.id), nullable=False)
     market = relationship(Market)

     def get_total_assets(self):
          try:
               res = db.session.query(func.count(Asset.id)).first()
          except Exception as e:
               res = []
               print(e)
          finally:
               db.session.close()
               return res

     def __repr__(self) -> str:
          return self.code
