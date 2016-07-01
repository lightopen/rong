from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import FileField, SubmitField, StringField, PasswordField

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = "no"

class SignupForm(Form):
    username = StringField("姓名：", default='孙立荣')
    
    id = StringField("身份证号：")
    phone = StringField("手机号：")
    password = PasswordField("密码：")
    submit = SubmitField("注册")

@app.route("/", methods=["GET", "PSOT"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        pass
    return render_template("signup.html", form=form)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
