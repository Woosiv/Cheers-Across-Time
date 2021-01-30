from flask import blueprint

auth = blueprint('auth', __name__)

# Login Page
@auth.route('/login', methods=['POST'])
def login():
    #if request.method == 'POST':
    user = request.form['username']
    password = request.form['password']
    if verifyLogin(user, password):
        print('correct user login')
        return redirect(url_for('homepage', username = user))
    else:
        print('failed login')
        return redirect(url_for('login'))
    #else:
        #return app.send_static_file('login.html')

@auth.rout('/signup')
def signup():
    pass


