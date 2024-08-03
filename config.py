import os


class Config:
    class Server:
        DEBUG = True
        host = '0.0.0.0'
        port = 1111

    class Nginx:
        domain = 'site.ru'
        docker_ip = '172.17.0.2'
        port = 1111

    # class Telegram:
    #     BOT_TOKEN = '7339257100:AAHzCA_15zsOzsqEOboCn9ll9U3C53k2iqU'
    #     CHAT_ID = '-4173800485'
    #     ENABLED = True

    ROOT_DIR = os.getcwd()
    SECRET_KEY = '9b63ce8c63674a7e80d95d3e2704d4a2'
    SQLALCHEMY_DATABASE_URI = rf"sqlite:///{os.path.abspath(os.path.join(ROOT_DIR, 'database.db'))}"
