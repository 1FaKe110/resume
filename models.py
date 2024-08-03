from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class AboutMe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    phone = db.Column(db.String(63), nullable=False)
    telegram = db.Column(db.String(63))
    photo_url = db.Column(db.String(255))


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    short_description = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.Boolean, default=False)
    image = db.Column(db.Text)


class ProjectStage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    short_description = db.Column(db.String(255), nullable=False)
    image = db.Column(db.Text, nullable=False)


class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    icon = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=False)
