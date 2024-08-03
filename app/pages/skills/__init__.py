from flask import flash, redirect, render_template, Blueprint, request, url_for
from loguru import logger

from app import db
from models import AboutMe, Project, ProjectStage, Skill
from config import Config


class Skills:

    def __init__(self):
        self.page = Blueprint('skills', __name__)

    @classmethod
    def render_page(cls):
        return render_template('pages/skills/skills.html')
