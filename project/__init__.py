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
#---------------------------------------------------------------------------------------------
# description: 1. First we have imported the Flask
#              2. Next we have created the instance of the class as app
#              2. then, we used app (object instance of type Flask) to configure Bootstrap, static files, and Email.
# (C) 2023 Andrei Rosca, Verona, Italy
# Released under BSD-3-Clause license
# email andreirosca92@gmail.com
# date 2023-04-23 21:40:51
# ---------------------------------------------------------------------------------------------



#imported the Flask class
from flask import Flask
import os 
from flask import url_for
from flask_bootstrap import Bootstrap5
from flask_mail import Mail
from flask_wtf import CSRFProtect
import secrets


#An instance of this class will be our WSGI application.
# initialize Flask with config 
app = Flask(__name__, static_url_path='',  static_folder= 'static',template_folder='templates')

# configuring email settings for flask
foo = secrets.token_urlsafe(16)
app.secret_key = foo
app.config['MAIL_SERVER']='sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '8bed310edf0817'
app.config['MAIL_PASSWORD'] = '3d1673e8c21d6b'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

# initialize class Mail
mail = Mail(app)

# initialize class Bootstrap5
Bootstrap5(app)



# Flask-WTF requires this line
csrf = CSRFProtect(app)

