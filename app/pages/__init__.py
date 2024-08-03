from app.pages.home import Home
from app.pages.project import ProjectDetailed
from app.pages.projects import Projects
from app.pages.skills import Skills


class Pages:

    def __init__(self):
        self.home = Home()
        self.projects = Projects()
        self.project = ProjectDetailed()
        self.skills = Skills()
