from api import create_app
from config import FLASK_RUN_HOST, FLASK_RUN_PORT

app = create_app()

if __name__ == '__main__':
    app.logger.info("Application is started")
    app.run(host=FLASK_RUN_HOST, port=FLASK_RUN_PORT)