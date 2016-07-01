from flask import Flask
form flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import FileField, SubmitField, StringField, PasswordField

app = Flask(__name__)
bootstrap = Bootstrap(app)



class SignupForm(Form):
    username = StringField("用户名：")
    
    id = StringField("身份证号：")
    phone = StringField("手机号：")
    password = PasswordField("密码：")
    submit = SubmitField("注册：")

@app.route("/", methods=["GET", "PSOT"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        pass
    return render_template("signup.html", form=form)
