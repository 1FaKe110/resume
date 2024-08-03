from flask import flash, redirect, render_template, Blueprint, request, url_for
from loguru import logger

from app import db
from models import AboutMe, Project, ProjectStage, Skill
from config import Config


class Projects:

    def __init__(self):
        self.page = Blueprint('projects', __name__)

    @classmethod
    def render_page(cls):
        projects = Project.query.all()
        return render_template('pages/projects/projects.html', projects=projects)
