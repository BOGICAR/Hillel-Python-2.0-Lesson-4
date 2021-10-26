from flask import Flask, render_template, request, make_response, session

app = Flask(__name__)

app.secret_key = 'jfkjfdjkdfj'


@app.route('/')
def index():
    visit_counter = 0
    if session.get('visited'):
        visit_counter = session['visited']
    else:
        session['visited'] = 0
    response = make_response((render_template('index.html', visit=visit_counter)))
    session['visited'] += 1
    return response


@app.route('/login', methods=["GET", "POST"])
def log_in():
    if request.method == "GET":
        return """
        <form action="http://localhost:5000/login", method="POST">
            <input name="username">
            <input type="submit">
        </form>
        """
    elif request.method == 'POST':
        username = request.form['username']
        return f"User logged into a system like {username}"


@app.route('/logout')
def logout():
    session.pop('username', None)
    return render_template("logout.html")


if __name__ == '__main__':
    app.run(debug=True)
