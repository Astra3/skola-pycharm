from subprocess import Popen, PIPE

from flask import Flask, render_template, request, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.html5 import IntegerField, DecimalField
from wtforms.validators import DataRequired, EqualTo


class Field(FlaskForm):
    address = StringField("Ping adresa", validators=[DataRequired()])
    c = IntegerField("Počet pingů", default=4, validators=[DataRequired()])
    i = DecimalField("Interval pingů", default=1, validators=[DataRequired()])
    sub = SubmitField("Potvrdit", validators=[DataRequired()])


app = Flask(__name__)
app.config["SECRET_KEY"] = "18f06f42c8fb790fc698dc479932a5fa"


@app.route("/", methods=["GET"])
def main():
    form = Field(request.args, meta={"csrf": False})
    if form.validate():
        ping = Popen(["ping", "-i", str(form.i.data).replace(".", ","), "-c", str(form.c.data),
                      str(form.address.data)], stdout=PIPE, stderr=PIPE)
        ping.wait()
        stdout = ping.stdout.readlines()
        err = ping.stderr.readlines()
        output = ""
        for i in stdout:
            output += i.decode().replace("\n", "<br>")
        try:
            if b', 0%' in stdout[-2]:
                text = {"text": "PING DOKONČEN ÚSPĚŠNĚ", "color": "green"}
            else:
                text = {"text": "PING ZAZNAMENAL ZTRÁTY", "color": "red"}
        except IndexError:
            for i in err:
                output += i.decode().replace("\n", "<br>")
            text = {"text": "PING SELHAL", "color": "red"}

        return render_template("ping.html", output=output, text=text, title="Ping proběhl", form=form)
    else:
        return render_template("ask.html", form=form, title="Ping")


if __name__ == '__main__':
    app.run(debug=True)
