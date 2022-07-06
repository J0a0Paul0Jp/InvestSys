from config import app_config, app_active
from app import db
from model.Asset import Asset
from sqlalchemy.orm import relationship
from sqlalchemy import func

class AssetInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(200), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)
    static = db.Column(db.Boolean(), default=True, nullable=False)
    type = db.Column(db.String(3), default=True, nullable=False)
    numeric_value = db.Column(db.Numeric(), default=0.0)
    str_value = db.Column(db.Text())
    bool_value = db.Column(db.Boolean(), default=False)
    asset_id = db.Column(db.Integer, db.ForeignKey(Asset.id), nullable=False)
    asset = relationship(Asset)

    def get_total_assetsinfo(self):
        try:
            res = db.session.query(func.count(AssetInfo.id)).first()
        except Exception as e:
            res = []
            print(e)
        finally:
            db.session.close()
            return res

    def __repr__(self) -> str:
        return self.code