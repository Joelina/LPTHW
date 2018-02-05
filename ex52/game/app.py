from flask import Flask, session, request
from flask import url_for, redirect, render_template
import pickle
import map

app = Flask(__name__)

@app.route('/game', methods=['GET'])
def game_get():
    if 'scene' in session:
        thescene = map.SCENES[session['scene']]
        return render_template('show_scene.html', scene=thescene, paths = thescene.get_paths())
    else:
        return redirect(url_for('index'))

@app.route('/game', methods=['POST'])
def game_post():
    userinput = request.form.get('userinput')
    if 'scene' in session:
        if userinput is None:
            return render_template('show_scene.html', scene = currentscene, message = "You have to enter something.")
        else:
            currentscene = map.SCENES[session['scene']]
            nextscene = currentscene.go(userinput)
            if nextscene is None:
                return render_template('show_scene.html', scene = currentscene, message = "Wrong input.")
            else:
                session['scene'] = nextscene.urlname
                return render_template('show_scene.html', scene = nextscene, paths = nextscene.get_paths())
    else:
        return redirect(url_for('index'))


@app.route('/login', methods = ['GET'])
def login():
    if 'user' in session:
        return redirect(url_for('start'))
    else:
        return render_template('login.html')

@app.route('/login', methods = ['POST'])
def userdata():
    users = []
    username = request.form.get('username')
    password = request.form.get('password')
    with open('user_list.txt', 'r') as f:
        users = pickle.loads(f.read())
        print users
    try:
        users[username]
    except KeyError:
        return render_template('login.html', message = 'no such user')
    else:
        if users[username] == password:
            session['user'] = username
            return redirect(url_for('index'))
        else:
            return render_template('login.html', message = 'wrong password')

@app.route('/logout', methods = ['GET'])
def logout():
    if 'user' in session:
        del session['user']
        return render_template('logged_out.html')

@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def mk_newUser():
    user = request.form.get('username')
    password = request.form.get('password')
    data = {user:password}
    with open('user_list.txt', 'r+') as f:
        try:
            users = pickle.loads(usrfile.read())
            usrfile.seek(0)
            usrfile.truncate()
        except:
            users = {}
        users.update(data)
        pickle.dump(users,f)
    return render_template('register.html', message = "Registration successful.")

@app.route('/save', methods=['GET'])
def save():

    thescene = map.SCENES[session['scene']]
    data = {session['user']:thescene}
    saves = {}

    with open('user_saves.txt', 'a+') as f:
        try:
            saves = pickle.loads(f.read)
        except:
            pass
        saves[session['user']]=thescene
        f.seek(0)
        f.truncate()
        pickle.dump(saves,f)

    return redirect(url_for('game_get'))

@app.route('/load', methods=['GET'])
def load():
    thescene = map.SCENES[session['scene']]
    message = 'Nothing to load.'
    with open('user_saves.txt', 'r') as f:
        try:
            saves = pickle.loads(f.read())
            thescene = saves[session['user']]
            session['scene']=thescene.urlname
            message = 'Previous game loaded.'
        except:
            pass
        return redirect(url_for('game_get'))

#This url initializes the session with starting values
@app.route('/')
def index():
    if 'user' in session:
        session['scene'] = map.START.urlname
        return redirect(url_for('game_get'))
    else:
        return redirect(url_for('login'))

app.secret_key = '538GcoQ6Lh4df12XP7z'

if __name__ == "__main__":
    app.run()
