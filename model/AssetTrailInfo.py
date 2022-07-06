from config import app_config, app_active
from app import db
from model.AssetTrail import AssetTrail
from sqlalchemy.orm import relationship

class AssetTrailInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(200), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)
    static = db.Column(db.Boolean(), default=True, nullable=False)
    type = db.Column(db.String(3), default=True, nullable=False)
    numeric_value = db.Column(db.Numeric(), default=0.0)
    str_value = db.Column(db.Text())
    bool_value = db.Column(db.Boolean(), default=False)
    assettrail_id = db.Column(db.Integer, db.ForeignKey(AssetTrail.id), nullable=False)
    assettrail = relationship(AssetTrail)
    def __repr__(self) -> str:
        return self.code
