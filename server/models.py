# models.py

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# Naming convention to prevent migration issues with Alembic (optional but recommended)
metadata = MetaData(
    naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
    }
)

# Initialize SQLAlchemy with custom metadata
db = SQLAlchemy(metadata=metadata)

# Define the Employee model
class Employee(db.Model):
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Employee id={self.id}, name={self.name}, salary={self.salary}>"
