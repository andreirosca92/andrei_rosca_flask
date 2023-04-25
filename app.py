# -----------------------------------------------------------------------------------------
# BSD-3-Clause Source License
#
# Copyright 2010 Pallets
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
# 3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
# OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# ---------------------------------------------------------------------------------------------
# description: root file contains routing page and instance of class Flask for start the app
# (C) 2023 Andrei Rosca, Verona, Italy
# Released under BSD-3-Clause license
# email andreirosca92@gmail.com
# date 2023-04-23 21:40:51
# ---------------------------------------------------------------------------------------------


from flask import render_template, redirect, url_for
from project import app
from flask import send_from_directory
from project import mail
from flask_mail import Message
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

key_random = {}


class NameForm(FlaskForm):
    name = StringField("Full name", validators=[DataRequired(), Length(6, 40)])
    email = StringField("Email address", validators=[DataRequired(), Length(6, 80)])
    tel_number = StringField("Phone number", validators=[DataRequired(), Length(8, 15)])
    message = StringField("Message", validators=[DataRequired(), Length(8, 500)])
    submit = SubmitField("Send")


# create a routing home page
@app.route("/")
def index():
    return render_template("main.html")


# app name
@app.errorhandler(404)
# inbuilt function which takes error as parameter
def page_not_found(e):
    # defining function
    return render_template("404.html"), 404


# create a routing about page
@app.route("/about")
def about():
    return render_template("about.html")


# create a routing contact page
@app.route("/contact", methods=["GET", "POST"])
def contact():
    # call class NameForm for construct form data
    form = NameForm()
    if form.validate_on_submit():
        # reading data from the form and assign it to local variables.
        name = form.name.data
        email = form.email.data
        tel_number = form.tel_number.data
        message = form.message.data

        # generate a temporary key
        # key = Fernet.generate_key()
        # #
        # fernet=Fernet(key)
        # #encrypt the name
        # name_hash=fernet.encrypt(name.encode())
        # #encrypt the message
        # message_hash=fernet.encrypt(message.encode())
        # assign key to global variable dict key_random
        key_random[name] = message

        # build email and send it
        msg = Message(name, sender=email, recipients=["andreirosca92@gmail.com"])
        msg.body = message + "\n" + "Tel: " + tel_number
        mail.send(msg)

        # empty the form field
        form.name.data = ""
        form.email.data = ""
        form.tel_number.data = ""
        form.message.data = ""
        # redirect to send_email functions
        # return redirect(url_for('send_email',name_hash=name_hash, message_hash=message_hash))
        return redirect(url_for("send_email"))
    else:
        # render contact page
        return render_template("contact.html", form=form)


# create a routing pdf page
@app.route("/about/pdf/<path:filename>", methods=["GET", "POST"])
def download(filename):
    return send_from_directory(directory="pdf", filename=filename)


# create a routing send_email page
@app.route("/contact/send_email", methods=["GET", "POST"])
def send_email():
    #    load the key
    #    key = key_random.get('key1')
    #    fernet = Fernet(key)
    #    # decrypt the message
    #    message=fernet.decrypt(message_hash).decode()
    #    # decrypt the name
    #    name=fernet.decrypt(name_hash).decode()
    #    destroying temporary key
    for key, value in key_random.items():
        name, message = key, value
    key_random.clear()

    # render send_email page
    return render_template("send_email.html", name=name, message=message)


if __name__ == "__main__":
    # run the app
    app.run(debug=True)
