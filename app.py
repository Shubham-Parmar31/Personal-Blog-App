from flaskblog import create_app
from flaskblog.config import Config
from flaskblog import db


app =create_app()


if __name__=="__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)