# app.py
from flask_cors import CORS

from app import create_app
from app.pages import Pages
from config import Config

pages = Pages()
app = create_app()
CORS(app)


@app.route('/')
def home():
    return pages.home.render_page()


@app.route('/projects')
def projects():
    return pages.projects.render_page()


@app.route('/projects/<project_id>/')
def project(project_id):
    return pages.project.render_page(project_id)


@app.route('/skills')
def skills():
    return pages.skills.render_page()


@app.route('/status')
def status():
    return "200"


def main():
    app.register_blueprint(pages.home.page)
    app.register_blueprint(pages.projects.page)
    app.register_blueprint(pages.project.page)
    app.register_blueprint(pages.skills.page)

    app.run(
        debug=Config.Server.DEBUG,
        host=Config.Server.host,
        port=Config.Server.port
    )


if __name__ == '__main__':
    main()
