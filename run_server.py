from my_app.config import settings, assets

from flask import Flask

# set up the flask app

app = Flask(__name__, static_folder= "my_app/static",
            template_folder="my_app/templates")
assets.init_assets(app)


def setup_logging(logging_path, level):
    '''Setups logging in app'''
    from logging.handlers import RotatingFileHandler
    from logging import getLogger, getLevelName
    file_handler = RotatingFileHandler(logging_path)
    file_handler.setLevel(getLevelName(level))
    loggers = [app.logger, getLogger('sqlalchemy')]
    for logger in loggers:
        logger.addHandler(file_handler)

if __name__ == "__main__":

    app.run(debug=app.debug, port=5001)
    setup_logging(logging_path=settings.LOGGING_PATH,
                  level=settings.LOGGING_LEVEL)
