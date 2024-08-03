from flask import flash, redirect, render_template, Blueprint, request, url_for
from loguru import logger

from app import db
from models import AboutMe, Project, ProjectStage, Skill
from config import Config


class Home:

    def __init__(self):
        self.page = Blueprint('home', __name__)

    @classmethod
    def render_page(cls):
        about_me = AboutMe.query.first()
        return render_template('pages/home/home.html', about_me=about_me)
