from flask import flash, redirect, render_template, Blueprint, request, url_for
from loguru import logger

from app import db
from models import AboutMe, Project, ProjectStage, Skill
from config import Config


class ProjectDetailed:

    def __init__(self):
        self.page = Blueprint('project', __name__)

    @classmethod
    def render_page(cls, project_id):
        project = Project.query.filter_by(id=project_id).first()
        if project is None:
            flash('Проект не найден', 'error_outline')
            return redirect(url_for('projects'))

        stages = ProjectStage.query.filter_by(project_id=project_id).all()
        return render_template('pages/project/project.html',
                               project=project,
                               stages=stages)
