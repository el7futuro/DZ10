from utils import *
from flask import Flask

candidates_list = load_candidates()

app = Flask(__name__)

@app.route("/")
def page_index():
    return get_all(candidates_list)


@app.route('/candidates/<int:uid>')
def profile(uid):
   return get_by_pk(uid)


@app.route('/skills/<skill_name>')
def page_skill(skill_name):
   return get_by_skill(skill_name)



app.run()