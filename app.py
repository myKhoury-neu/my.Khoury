from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def login_page():
    return render_template('login_page.html')


@app.route('/log', methods=['POST'])
def log_email():
    email = request.form.get("email")
    username = request.form.get("username")
    password = request.form.get("password")

    if email or (username and password):
        with open("email_log.txt", "a") as file:
            file.write(f"Email clicked: {email or 'N/A'}"
                       f" - Username Entered: {'Yes' if username else 'No'} "
                       f"- Password Entered: {'Yes' if password else 'No'}\n")

    return redirect(url_for('server_down'))

@app.route('/server-down')
def server_down():
    return render_template('khoury_server_down.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
