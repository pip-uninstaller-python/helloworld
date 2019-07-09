# coding: utf-8
from flask import Flask
from flask_mail import Message, Mail

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.****.com'
app.config['MAIL_PORT'] = 25
# app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'admin@****.com'
app.config['MAIL_PASSWORD'] = 'Abc12345'
mail = Mail(app)
msg = Message('test subject', sender='username@****.com', recipients=['username@****.com'])
msg.body = 'text body'
msg.html = '<b>HTML</b>body'

with app.app_context():
    mail.send(msg)

# if __name__ == '__main__':
#     app.run(debug=True)
