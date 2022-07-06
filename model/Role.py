from config import app_active, app_config
from app import db
from sqlalchemy import func

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True, nullable=False)
    def get_total_roles(self):
        try:
            res = db.session.query(func.count(Role.id)).first()
        except Exception as e:
            res = []
            print(e)
        finally:
            db.session.close()
            return res

    def get_role_by_id(self, id=None):
        if id is None:
            id = self.id
        try:
            res = db.session.query(Role).filter(Role.id==id).first()
        except Exception as e:
            res = None
            print(e)
        finally:
            db.session.close()
            return res
    def __repr__(self) -> str:
        return self.name

