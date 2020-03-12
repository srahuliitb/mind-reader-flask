from flask import Flask, request, render_template, session, url_for, redirect
from game import *
from flask_session import Session


mind_reader = ShannonExpert()

app = Flask(__name__, static_folder='public', template_folder='views')
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['SECRET_KEY'] = 'the random string'
#app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
Session(app)

@app.route("/", methods=["GET", "POST"])
def start():
    if session.get("gameDetails") is None:
        session["gameDetails"]={
            "user_score":0,
            "comp_score":0,
            "user_input_list":[],
            "comp_guess_list":[]
        }
    if request.method == "GET":
        return render_template('index.html', GameDetails=session["gameDetails"])
    
    if request.method == "POST":
        user_input = int(request.form.get('submit_button'))
        session["gameDetails"]['user_input_list'].append(user_input)
        comp_guess = mind_reader.predict()
        session["gameDetails"]['comp_guess_list'].append(comp_guess)
        
        current = user_input
        mind_reader.update(current)
        
        if user_input == comp_guess: 
            session["gameDetails"]['comp_score'] += 1     
        
        else:
            session["gameDetails"]['user_score'] += 1

        return redirect (url_for('start'))

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r



@app.route('/reset')
def reset():
    session["gameDetails"]['user_score'] = 0
    session["gameDetails"]['comp_score'] = 0
    session["gameDetails"]['user_input_list'] = []
    session["gameDetails"]['comp_guess_list'] = []
    return redirect(url_for('start'))


if (__name__ == "__main__"):
    app.run(debug=True, port=3000, host='0.0.0.0')
