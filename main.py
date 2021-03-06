import os
from flask import Flask, render_template, url_for
from flask import jsonify, make_response
from flask_restful import Api

from data import db_session, news_api
from data.news import News
from api_2.news_resource import NewsResource
from data.users import User

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
@app.route("/index")
def index():
    db_sess = db_session.create_session()
    news = db_sess.query(News).filter(News.is_private != True)
    return render_template("index.html", news=news,
                           css_url=url_for('static', filename='css/style.css'))


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': str(error)}), 404)


def main():
    db_session.global_init()

    session = db_session.create_session()
    if not session.query(User).first():
        import fill_base

    app.register_blueprint(news_api.blueprint)
    if 'HEROKU' in os.environ:
        port = int(os.environ.get("PORT", 5000))
        app.run(host='0.0.0.0', port=port)
    else:
        app.run()


# для одного объекта
api.add_resource(NewsResource, '/api/v2/news/<int:news_id>')

if __name__ == '__main__':
    main()
