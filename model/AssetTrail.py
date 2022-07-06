from config import app_config, app_active
from app import db
from model.Asset import Asset
from model.User import User
from sqlalchemy.orm import relationship

class AssetTrail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    asset_id = db.Column(db.Integer, db.ForeignKey(Asset.id), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    asset = relationship(Asset)
    user = relationship(User)
