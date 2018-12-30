from realestateapi import db
from sqlalchemy import event, DDL


class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    iban = db.Column(db.String(40), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    account_holder = db.Column(db.String(150), nullable=False)
    payment_json = db.Column(db.JSON, nullable=False)
    date = db.Column(db.Date, nullable=False)
    tenant_id = db.Column(db.Integer, db.ForeignKey(
        'tenant.id'), nullable=False)

    def __repr__(self):
        return f"Payment('{self.id}', '{self.iban}, '{self.rent}','{self.account_holder}')"


class Upload(db.Model):
    __tablename__ = "json_upload"
    id = db.Column(db.Integer, primary_key=True)
    upload_content = db.Column(db.JSON)
    uploaded_at = db.Column(db.Date)

    def __init__(self, upload_content, uploaded_at):
        self.upload_content = upload_content
        self.uploaded_at = uploaded_at

    def __repr__(self):
        return f"Upload('{self.id}', '{self.upload_content}')"


class Tenant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    account_holder = db.Column(db.String(150), unique=True)
    first_name = db.Column(db.String(25))
    last_name = db.Column(db.String(35))
    iban = db.Column(db.String(35), nullable=False)
    rent = db.Column(db.Float)
    phone = db.Column(db.String(12))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'email': self.email,
            'account_holder': self.account_holder,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'iban': self.iban,
            'rent': self.rent,
            'phone': self.phone
        }

    # def __repr__(self):
    #     return f"Tenant('{self.id}','{self.account_holder}', '{self.first_name}','{self.last_name}','{self.iban}','{self.rent}','{self.phone}')"
